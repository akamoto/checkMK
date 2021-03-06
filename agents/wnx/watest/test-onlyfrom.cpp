// test-onlyfrom.cpp
// also tested ipv6
// and ends there.
//
#include "pch.h"

#include "common/cfg_info.h"
#include "external_port.h"

#include "cfg.h"

#include "onlyfrom.h"

std::string network_list[] = {
    "2001:db8:abcd:0012::0/112",  // mask
                                  // 2001:0DB8:ABCD:0012:0000:0000:0000:0000
                                  // 2001:0DB8:ABCD:0012:0000:0000:0000:FFFF
    "192.168.1.1/24"              // mask
                                  // 192.168.1.0
                                  // 192.168.1.255
};
std::string loopback_list[] = {
    "::1",        // loopback ipv6
    "127.0.0.1",  // loopback ipv4
};
std::string address_list[] = {"2001:0DB8:ABCD:0012::AAAA",  // address ipv6
                              "192.168.1.13"};              // addressipv4

std::string address_out_list[] = {
    "2001:0DB8:ABCD:0012:0001:0001:0002:AAAA",  // address ipv6
    "192.168.2.13"};                            // addressipv4
namespace cma::cfg {
TEST(OnlyFromTest, Convert) {
    std::error_code ec;
    using namespace asio;
    {
        auto n_v6 = of::MapToV6Address(network_list[0]);
        EXPECT_TRUE(n_v6.empty());
    }
    {
        auto n_v4 = of::MapToV6Address(network_list[1]);
        EXPECT_TRUE(n_v4.empty());
    }
    {
        auto l_v6 = of::MapToV6Address(loopback_list[0]);
        EXPECT_TRUE(l_v6.empty());
    }
    {
        auto l_v4 = of::MapToV6Address(loopback_list[1]);
        EXPECT_FALSE(l_v4.empty());
        EXPECT_TRUE(of::IsAddressV6(l_v4));
        auto table = cma::tools::SplitString(l_v4, ":");
        EXPECT_TRUE(table.size() == 4);
        EXPECT_EQ(table.back(), loopback_list[1]);
    }

    {
        auto a_v6 = of::MapToV6Address(address_list[0]);
        EXPECT_TRUE(a_v6.empty());
    }
    {
        auto a_v4 = of::MapToV6Address(address_list[1]);
        EXPECT_FALSE(a_v4.empty());
        EXPECT_TRUE(of::IsAddressV6(a_v4));
        auto table = cma::tools::SplitString(a_v4, ":");
        EXPECT_TRUE(table.size() == 4);
        EXPECT_EQ(table.back(), address_list[1]);
    }

    {
        auto mapped_v6 = of::MapToV6Network(network_list[0]);
        EXPECT_TRUE(mapped_v6.empty());
    }
    {
        auto mapped_v4 = of::MapToV6Network(network_list[1]);
        EXPECT_FALSE(mapped_v4.empty());
        EXPECT_TRUE(of::IsNetworkV6(mapped_v4));
        auto table = cma::tools::SplitString(mapped_v4, ":");
        EXPECT_TRUE(table.size() == 4);
        EXPECT_EQ(table.back(), "192.168.1.0/120");
    }
}

TEST(OnlyFromTest, Validness) {
    std::error_code ec;
    using namespace asio;

    for (auto l : loopback_list) {
        EXPECT_TRUE(of::IsAddress(l));
        EXPECT_FALSE(of::IsNetwork(l));
    }
    for (auto a : address_list) {
        EXPECT_TRUE(of::IsAddress(a));
        EXPECT_FALSE(of::IsNetwork(a));
    }
    for (auto n : network_list) {
        EXPECT_TRUE(of::IsNetwork(n));
        EXPECT_FALSE(of::IsAddress(n));
    }

    EXPECT_TRUE(of::IsNetworkV6(network_list[0]));
    EXPECT_TRUE(of::IsAddressV6(address_list[0]));
    EXPECT_TRUE(of::IsAddressV6(loopback_list[0]));

    EXPECT_TRUE(of::IsNetworkV4(network_list[1]));
    EXPECT_TRUE(of::IsAddressV4(address_list[1]));
    EXPECT_TRUE(of::IsAddressV4(loopback_list[1]));

    EXPECT_TRUE(of::IsValid(address_list[0], address_list[0]));
    EXPECT_TRUE(of::IsValid(address_list[1], address_list[1]));

    EXPECT_TRUE(of::IsValid(loopback_list[0], loopback_list[0]));
    EXPECT_TRUE(of::IsValid(loopback_list[1], loopback_list[1]));

    EXPECT_TRUE(of::IsValid(address_out_list[0], address_out_list[0]));
    EXPECT_TRUE(of::IsValid(address_out_list[1], address_out_list[1]));

    EXPECT_FALSE(of::IsValid(address_list[0], address_list[1]));
    EXPECT_FALSE(of::IsValid(address_list[1], address_list[0]));
    EXPECT_FALSE(of::IsValid(loopback_list[0], loopback_list[1]));
    EXPECT_FALSE(of::IsValid(loopback_list[1], loopback_list[0]));
    EXPECT_FALSE(of::IsValid(address_out_list[0], address_out_list[1]));
    EXPECT_FALSE(of::IsValid(address_out_list[1], address_out_list[0]));

    EXPECT_FALSE(of::IsValid(address_list[0], address_out_list[0]));
    EXPECT_FALSE(of::IsValid(address_list[1], address_out_list[1]));

    EXPECT_TRUE(of::IsValid(network_list[0], address_list[0]));
    EXPECT_TRUE(of::IsValid(network_list[1], address_list[1]));

    EXPECT_FALSE(of::IsValid(network_list[0], address_out_list[0]));
    EXPECT_FALSE(of::IsValid(network_list[1], address_out_list[1]));

    EXPECT_FALSE(of::IsValid(loopback_list[0], loopback_list[1]))
        << "ipv4 loopback is good for ::1";
    EXPECT_FALSE(of::IsValid(loopback_list[1], loopback_list[0]));
}

TEST(OnlyFromTest, Base) {
    using namespace std::chrono;
    using namespace xlog::internal;

    ON_OUT_OF_SCOPE(cma::OnStart(cma::kTest));
    {
        auto yaml = GetLoadedConfig();
        yaml[groups::kGlobal][vars::kOnlyFrom] =
            YAML::Load("192.168.1.14/24 ::1 127.0.0.1");

        yaml[groups::kGlobal][vars::kIpv6] = YAML::Load("on\n");

        groups::global.loadFromMainConfig();
        auto only_froms = groups::global.getOnlyFrom();
        EXPECT_TRUE(only_froms.size() == 5);
        EXPECT_TRUE(of::IsNetworkV4(only_froms[0]));
        EXPECT_TRUE(of::IsNetworkV6(only_froms[1]));
        EXPECT_TRUE(of::IsAddressV6(only_froms[2]));
        EXPECT_TRUE(of::IsAddressV4(only_froms[3]));
        EXPECT_TRUE(of::IsAddressV6(only_froms[4]));

        EXPECT_TRUE(groups::global.isIpAddressAllowed("192.168.1.13"));
        EXPECT_TRUE(groups::global.isIpAddressAllowed("::FFFF:192.168.1.2"));
        EXPECT_FALSE(groups::global.isIpAddressAllowed("192.168.2.13"));
        EXPECT_FALSE(groups::global.isIpAddressAllowed("::FFFF:192.168.2.2"));
        EXPECT_TRUE(groups::global.isIpAddressAllowed("::1"));
        EXPECT_TRUE(groups::global.isIpAddressAllowed("127.0.0.1"));
        EXPECT_TRUE(groups::global.isIpAddressAllowed("::FFFF:127.0.0.1"));

        bool address_ok = true;
        int port = 64351;
        cma::world::ReplyFunc reply =
            [&address_ok](const std::string Ip) -> std::vector<uint8_t> {
            std::error_code ec;

            if (!groups::global.isIpAddressAllowed(Ip)) {
                XLOG::d("Invalid IP {}", Ip);
                return {};
            }

            auto data = reinterpret_cast<const uint8_t*>(Ip.data());
            std::vector<uint8_t> v(data, data + Ip.size());
            return v;
        };

        using namespace asio;
        // ipv4
        {
            cma::world::ExternalPort test_port(nullptr, port);  //
            auto ret = test_port.startIo(reply);                //
            ASSERT_TRUE(ret);

            try {
                io_context ios;

                ip::tcp::endpoint endpoint(ip::make_address("127.0.0.1"), port);

                asio::ip::tcp::socket socket(ios);

                socket.connect(endpoint);

                error_code error;
                char text[256];
                auto count = socket.read_some(asio::buffer(text), error);
                EXPECT_TRUE(count > 1);
                socket.close();
            } catch (const std::exception& e) {
                XLOG::l("Exception {} during connection to ", e.what());
            }
            test_port.shutdownIo();  //
        }

        // ipv6 connect
        {
            cma::world::ExternalPort test_port(nullptr, port);  //
            auto ret = test_port.startIo(reply);                //
            ASSERT_TRUE(ret);
            io_context ios;
            ip::tcp::endpoint endpoint(ip::make_address("::1"), port);

            asio::ip::tcp::socket socket(ios);

            socket.connect(endpoint);

            error_code error;
            char text[256];
            auto count = socket.read_some(asio::buffer(text), error);
            socket.close();
            EXPECT_TRUE(count > 1);
            test_port.shutdownIo();  //
        }

        // bad address
        {
            auto yaml = GetLoadedConfig();
            yaml[groups::kGlobal][vars::kOnlyFrom] =
                YAML::Load("192.168.1.14/24");

            groups::global.loadFromMainConfig();
            auto only_froms = groups::global.getOnlyFrom();
            EXPECT_TRUE(only_froms.size() == 2);
            cma::world::ExternalPort test_port(nullptr, port);  //
            auto ret = test_port.startIo(reply);                //
            ASSERT_TRUE(ret);
            io_context ios;
            ip::tcp::endpoint endpoint(ip::make_address("::1"), port);

            asio::ip::tcp::socket socket(ios);

            socket.connect(endpoint);

            error_code error;
            char text[256];
            auto count = socket.read_some(asio::buffer(text), error);
            socket.close();
            EXPECT_TRUE(count == 0);
            test_port.shutdownIo();  //
        }
    }
}

TEST(OnlyFromTest, Ipv6) {
    using namespace std::chrono;
    using namespace xlog::internal;

    ON_OUT_OF_SCOPE(cma::OnStart(cma::kTest));
    {
        auto yaml = GetLoadedConfig();
        yaml[groups::kGlobal][vars::kOnlyFrom] = YAML::Load("::1 127.0.0.1");
        yaml[groups::kGlobal][vars::kIpv6] = YAML::Load("on\n");

        groups::global.loadFromMainConfig();
        auto only_froms = groups::global.getOnlyFrom();
        EXPECT_TRUE(only_froms.size() == 3);
        EXPECT_TRUE(of::IsAddressV6(only_froms[0]));
        EXPECT_TRUE(of::IsAddressV4(only_froms[1]));
        EXPECT_TRUE(of::IsAddressV6(only_froms[2]));

        bool address_ok = true;
        int port = 64351;
        cma::world::ReplyFunc reply =
            [&address_ok](const std::string Ip) -> std::vector<uint8_t> {
            std::error_code ec;

            if (!groups::global.isIpAddressAllowed(Ip)) {
                XLOG::d("Invalid IP {}", Ip);
                return {};
            }

            auto data = reinterpret_cast<const uint8_t*>(Ip.data());
            std::vector<uint8_t> v(data, data + Ip.size());
            return v;
        };

        using namespace asio;
        // ipv4
        {
            cma::world::ExternalPort test_port(nullptr, port);  //
            auto ret = test_port.startIo(reply);                //
            ASSERT_TRUE(ret);

            try {
                io_context ios;

                ip::tcp::endpoint endpoint(ip::make_address("127.0.0.1"), port);

                asio::ip::tcp::socket socket(ios);

                socket.connect(endpoint);

                error_code error;
                char text[256];
                auto count = socket.read_some(asio::buffer(text), error);
                EXPECT_TRUE(count > 1);
                socket.close();
            } catch (const std::exception& e) {
                XLOG::l("Exception {} during connection to ", e.what());
            }
            test_port.shutdownIo();  //
        }

        // ipv6 connect
        {
            cma::world::ExternalPort test_port(nullptr, port);  //
            auto ret = test_port.startIo(reply);                //
            ASSERT_TRUE(ret);
            io_context ios;
            ip::tcp::endpoint endpoint(ip::make_address("::1"), port);

            asio::ip::tcp::socket socket(ios);

            socket.connect(endpoint);

            error_code error;
            char text[256];
            auto count = socket.read_some(asio::buffer(text), error);
            socket.close();
            EXPECT_TRUE(count > 1);
            test_port.shutdownIo();  //
        }

        {
            auto yaml = GetLoadedConfig();
            yaml[groups::kGlobal][vars::kOnlyFrom] =
                YAML::Load("::1 127.0.0.1");
            yaml[groups::kGlobal][vars::kIpv6] = YAML::Load("off\n");

            groups::global.loadFromMainConfig();
            auto only_froms = groups::global.getOnlyFrom();
            EXPECT_TRUE(only_froms.size() == 1);
            EXPECT_TRUE(of::IsAddressV4(only_froms[0]));

            //  ipv6 no connect
            {
                cma::world::ExternalPort test_port(nullptr, port);  //
                auto ret = test_port.startIo(reply);                //
                ASSERT_TRUE(ret);
                io_context ios;
                ip::tcp::endpoint endpoint(ip::make_address("::1"), port);

                asio::ip::tcp::socket socket(ios);

                EXPECT_ANY_THROW(socket.connect(endpoint));

                error_code error;
                char text[256];
                auto count = socket.read_some(asio::buffer(text), error);
                socket.close();
                EXPECT_TRUE(count == 0);
                test_port.shutdownIo();  //
            }

            //  ipv4 connected successfully
            {
                cma::world::ExternalPort test_port(nullptr, port);  //
                auto ret = test_port.startIo(reply);                //
                ASSERT_TRUE(ret);
                io_context ios;
                ip::tcp::endpoint endpoint(ip::make_address("127.0.0.1"), port);

                asio::ip::tcp::socket socket(ios);

                EXPECT_NO_THROW(socket.connect(endpoint));

                error_code error;
                char text[256];
                auto count = socket.read_some(asio::buffer(text), error);
                socket.close();
                EXPECT_TRUE(count > 0);
                test_port.shutdownIo();  //
            }
        }
    }
}
}  // namespace cma::cfg
