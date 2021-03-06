# Stubs for kubernetes.client.models.v1beta1_ingress_rule (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1IngressRule:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    host: Any = ...
    http: Any = ...
    def __init__(self, host: Optional[Any] = ..., http: Optional[Any] = ...) -> None: ...
    @property
    def host(self): ...
    @host.setter
    def host(self, host: Any) -> None: ...
    @property
    def http(self): ...
    @http.setter
    def http(self, http: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
