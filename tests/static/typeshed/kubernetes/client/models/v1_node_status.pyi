# Stubs for kubernetes.client.models.v1_node_status (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import V1NodeAddress, V1NodeCondition, V1NodeConfigStatus, V1NodeDaemonEndpoints, V1ContainerImage, V1NodeSystemInfo, V1AttachedVolume
from typing import Any, Dict, List, Optional

class V1NodeStatus:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    addresses: Any = ...
    allocatable: Any = ...
    capacity: Any = ...
    conditions: Any = ...
    config: Any = ...
    daemon_endpoints: Any = ...
    images: Any = ...
    node_info: Any = ...
    phase: Any = ...
    volumes_attached: Any = ...
    volumes_in_use: Any = ...
    def __init__(self, addresses: Optional[Any] = ..., allocatable: Optional[Any] = ..., capacity: Optional[Any] = ..., conditions: Optional[Any] = ..., config: Optional[Any] = ..., daemon_endpoints: Optional[Any] = ..., images: Optional[Any] = ..., node_info: Optional[Any] = ..., phase: Optional[Any] = ..., volumes_attached: Optional[Any] = ..., volumes_in_use: Optional[Any] = ...) -> None: ...
    @property
    def addresses(self) -> Optional[List[V1NodeAddress]]: ...
    @addresses.setter
    def addresses(self, addresses: Optional[List[V1NodeAddress]]) -> None: ...
    @property
    def allocatable(self) -> Optional[Dict[str, str]]: ...
    @allocatable.setter
    def allocatable(self, allocatable: Optional[Dict[str, str]]) -> None: ...
    @property
    def capacity(self) -> Optional[Dict[str, str]]: ...
    @capacity.setter
    def capacity(self, capacity: Optional[Dict[str, str]]) -> None: ...
    @property
    def conditions(self) -> Optional[List[V1NodeCondition]]: ...
    @conditions.setter
    def conditions(self, conditions: Optional[List[V1NodeCondition]]) -> None: ...
    @property
    def config(self) -> Optional[V1NodeConfigStatus]: ...
    @config.setter
    def config(self, config: Optional[V1NodeConfigStatus]) -> None: ...
    @property
    def daemon_endpoints(self) -> Optional[V1NodeDaemonEndpoints]: ...
    @daemon_endpoints.setter
    def daemon_endpoints(self, daemon_endpoints: Optional[V1NodeDaemonEndpoints]) -> None: ...
    @property
    def images(self) -> Optional[List[V1ContainerImage]]: ...
    @images.setter
    def images(self, images: Optional[List[V1ContainerImage]]) -> None: ...
    @property
    def node_info(self) -> Optional[V1NodeSystemInfo]: ...
    @node_info.setter
    def node_info(self, node_info: Optional[V1NodeSystemInfo]) -> None: ...
    @property
    def phase(self) -> Optional[str]: ...
    @phase.setter
    def phase(self, phase: Optional[str]) -> None: ...
    @property
    def volumes_attached(self) -> Optional[List[V1AttachedVolume]]: ...
    @volumes_attached.setter
    def volumes_attached(self, volumes_attached: Optional[List[V1AttachedVolume]]) -> None: ...
    @property
    def volumes_in_use(self) -> Optional[List[str]]: ...
    @volumes_in_use.setter
    def volumes_in_use(self, volumes_in_use: Optional[List[str]]) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
