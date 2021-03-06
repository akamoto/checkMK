# Stubs for kubernetes.client.models.v1beta1_ingress_tls (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1IngressTLS:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    hosts: Any = ...
    secret_name: Any = ...
    def __init__(self, hosts: Optional[Any] = ..., secret_name: Optional[Any] = ...) -> None: ...
    @property
    def hosts(self): ...
    @hosts.setter
    def hosts(self, hosts: Any) -> None: ...
    @property
    def secret_name(self): ...
    @secret_name.setter
    def secret_name(self, secret_name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
