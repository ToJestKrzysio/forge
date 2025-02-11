"""
4xx client error responses according to
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses
"""

from typing import Any, Optional

from fastapi import HTTPException

Detail = Any
Headers = Optional[dict[str, str]]


class BadRequestException(HTTPException):
    """HTTP 400 Bad Request"""

    def __init__(self, detail: Detail = "Bad Request", headers: Headers = None) -> None:
        super().__init__(400, detail, headers)


class UnauthorizedException(HTTPException):
    """HTTP 401 Unauthorized"""

    def __init__(self, detail: Detail = "Unauthorized", headers: Headers = None) -> None:
        super().__init__(401, detail, headers)


class PaymentRequiredException(HTTPException):
    """HTTP 402 Payment Required"""

    def __init__(self, detail: Detail = "Payment Required", headers: Headers = None) -> None:
        super().__init__(402, detail, headers)


class ForbiddenException(HTTPException):
    """HTTP 403 Forbidden"""

    def __init__(self, detail: Detail = "Forbidden", headers: Headers = None) -> None:
        super().__init__(403, detail, headers)


class NotFoundException(HTTPException):
    """HTTP 404 Not Found"""

    def __init__(self, detail: Detail = "Not Found", headers: Headers = None) -> None:
        super().__init__(404, detail, headers)


class MethodNotAllowedException(HTTPException):
    """HTTP 405 Method Not Allowed"""

    def __init__(self, detail: Detail = "Method Not Allowed", headers: Headers = None) -> None:
        super().__init__(405, detail, headers)


class NotAcceptableException(HTTPException):
    """HTTP 406 Not Acceptable"""

    def __init__(self, detail: Detail = "Not Acceptable", headers: Headers = None) -> None:
        super().__init__(406, detail, headers)


class ProxyAuthenticationRequiredException(HTTPException):
    """HTTP 407 Proxy Authentication Required"""

    def __init__(self, detail: Detail = "Proxy Authentication Required", headers: Headers = None) -> None:
        super().__init__(407, detail, headers)


class RequestTimeoutException(HTTPException):
    """HTTP 408 Request Timeout"""

    def __init__(self, detail: Detail = "Request Timeout", headers: Headers = None) -> None:
        super().__init__(408, detail, headers)


class ConflictException(HTTPException):
    """HTTP 409 Conflict"""

    def __init__(self, detail: Detail = "Conflict", headers: Headers = None) -> None:
        super().__init__(409, detail, headers)


class GoneException(HTTPException):
    """HTTP 410 Gone"""

    def __init__(self, detail: Detail = "Gone", headers: Headers = None) -> None:
        super().__init__(410, detail, headers)


class LengthRequiredException(HTTPException):
    """HTTP 411 Length Required"""

    def __init__(self, detail: Detail = "Length Required", headers: Headers = None) -> None:
        super().__init__(411, detail, headers)


class PreconditionFailedException(HTTPException):
    """HTTP 412 Precondition Failed"""

    def __init__(self, detail: Detail = "Precondition Failed", headers: Headers = None) -> None:
        super().__init__(412, detail, headers)


class ContentTooLargeException(HTTPException):
    """HTTP 413 ContentTooLarge"""

    def __init__(self, detail: Detail = "Content Too Large", headers: Headers = None) -> None:
        super().__init__(413, detail, headers)


class URITooLongException(HTTPException):
    """HTTP 414 URI Too Long"""

    def __init__(self, detail: Detail = "URI Too Long", headers: Headers = None) -> None:
        super().__init__(414, detail, headers)


class UnsupportedMediaTypeException(HTTPException):
    """HTTP 415 Unsupported Media Type"""

    def __init__(self, detail: Detail = "Unsupported Media Type", headers: Headers = None) -> None:
        super().__init__(415, detail, headers)


class RangeNotSatisfiableException(HTTPException):
    """HTTP 416 Range Not Satisfiable"""

    def __init__(self, detail: Detail = "Range Not Satisfiable", headers: Headers = None) -> None:
        super().__init__(416, detail, headers)


class ExpectationFailedException(HTTPException):
    """HTTP 417 Expectation Failed"""

    def __init__(self, detail: Detail = "Expectation Failed", headers: Headers = None) -> None:
        super().__init__(417, detail, headers)


class IMATeapotException(HTTPException):
    """HTTP 418 I'm a Teapot"""

    def __init__(self, detail: Detail = "I'm a Teapot", headers: Headers = None) -> None:
        super().__init__(418, detail, headers)


class MisdirectedRequestException(HTTPException):
    """HTTP 421 Misdirected Request"""

    def __init__(self, detail: Detail = "Misdirected Request", headers: Headers = None) -> None:
        super().__init__(421, detail, headers)


class UnprocessableContentException(HTTPException):
    """HTTP 422 Unprocessable Content"""

    def __init__(self, detail: Detail = "Unprocessable Content", headers: Headers = None) -> None:
        super().__init__(422, detail, headers)


class LockedException(HTTPException):
    """HTTP 423 Locked"""

    def __init__(self, detail: Detail = "Locked", headers: Headers = None) -> None:
        super().__init__(423, detail, headers)


class FailedDependencyException(HTTPException):
    """HTTP 424 Failed Dependency"""

    def __init__(self, detail: Detail = "Failed Dependency", headers: Headers = None) -> None:
        super().__init__(424, detail, headers)


class TooEarlyException(HTTPException):
    """HTTP 425 Too Early"""

    def __init__(self, detail: Detail = "Too Early", headers: Headers = None) -> None:
        super().__init__(425, detail, headers)


class UpgradeRequiredException(HTTPException):
    """HTTP 426 Upgrade Required"""

    def __init__(self, detail: Detail = "Upgrade Required", headers: Headers = None) -> None:
        super().__init__(426, detail, headers)


class PreconditionRequiredException(HTTPException):
    """HTTP 428 Precondition Required"""

    def __init__(self, detail: Detail = "Precondition Required", headers: Headers = None) -> None:
        super().__init__(428, detail, headers)


class TooManyRequestsException(HTTPException):
    """HTTP 429 Too Many Requests"""

    def __init__(self, detail: Detail = "Too Many Requests", headers: Headers = None) -> None:
        super().__init__(429, detail, headers)


class RequestHeaderFieldsTooLargeException(HTTPException):
    """HTTP 431 Request Header Fields Too Large"""

    def __init__(self, detail: Detail = "Request Header Fields Too Large", headers: Headers = None) -> None:
        super().__init__(431, detail, headers)


class UnavailableForLegalReasonsException(HTTPException):
    """HTTP 451 Unavailable For Legal Reasons"""

    def __init__(self, detail: Detail = "Unavailable For Legal Reasons", headers: Headers = None) -> None:
        super().__init__(451, detail, headers)
