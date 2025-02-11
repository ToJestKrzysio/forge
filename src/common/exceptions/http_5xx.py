"""
5xx client error responses according to
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses
"""

from typing import Any, Optional

from fastapi import HTTPException

Detail = Any
Headers = Optional[dict[str, str]]


class InternalServerErrorException(HTTPException):
    """HTTP 500 Internal Server Error"""

    def __init__(self, detail: Detail = "Internal Server Error", headers: Headers = None) -> None:
        super().__init__(500, detail, headers)


class NotImplementedException(HTTPException):
    """HTTP 501 Not Implemented"""

    def __init__(self, detail: Detail = "Not Implemented", headers: Headers = None) -> None:
        super().__init__(501, detail, headers)


class BadGatewayException(HTTPException):
    """HTTP 502 Bad Gateway"""

    def __init__(self, detail: Detail = "Bad Gateway", headers: Headers = None) -> None:
        super().__init__(502, detail, headers)


class ServiceUnavailableException(HTTPException):
    """HTTP 503 Service Unavailable"""

    def __init__(self, detail: Detail = "Service Unavailable", headers: Headers = None) -> None:
        super().__init__(503, detail, headers)


class GatewayTimeoutException(HTTPException):
    """HTTP 504 Gateway Timeout"""

    def __init__(self, detail: Detail = "Gateway Timeout", headers: Headers = None) -> None:
        super().__init__(504, detail, headers)


class HTTPVersionNotSupportedException(HTTPException):
    """HTTP 505 HTTP Version Not Supported"""

    def __init__(self, detail: Detail = "HTTP Version Not Supported", headers: Headers = None) -> None:
        super().__init__(505, detail, headers)


class VariantAlsoNegotiatesException(HTTPException):
    """HTTP 506 Variant Also Negotiates"""

    def __init__(self, detail: Detail = "Variant Also Negotiates", headers: Headers = None) -> None:
        super().__init__(506, detail, headers)


class InsufficientStorageException(HTTPException):
    """HTTP 507 Insufficient Storage"""

    def __init__(self, detail: Detail = "Insufficient Storage", headers: Headers = None) -> None:
        super().__init__(507, detail, headers)


class LoopDetectedException(HTTPException):
    """HTTP 508 Loop Detected"""

    def __init__(self, detail: Detail = "Loop Detected", headers: Headers = None) -> None:
        super().__init__(508, detail, headers)


class NotExtendedException(HTTPException):
    """HTTP 510 Not Extended"""

    def __init__(self, detail: Detail = "Not Extended", headers: Headers = None) -> None:
        super().__init__(510, detail, headers)


class NetworkAuthenticationRequiredException(HTTPException):
    """HTTP 511 Network Authentication Required"""

    def __init__(self, detail: Detail = "Network Authentication Required", headers: Headers = None) -> None:
        super().__init__(511, detail, headers)
