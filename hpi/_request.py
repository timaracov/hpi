class HttpHeader:
    ...


class HttpBody:
    ...


class HttpRequest:
    def __init__(
        self,
        path: str,
        method: str,
        headers: list[HttpHeader],
        body: HttpBody,
        version: str = "1.1",
    ):
        ...

    @staticmethod
    def from_bytes(request_raw: bytes):  # -> "HttpRequest":
        path = HttpRequest._extract_path(request_raw)
        method = HttpRequest._extract_method(request_raw)
        headers = HttpRequest._extract_headers(request_raw)
        body = HttpRequest._extract_body(request_raw)

        return HttpRequest(path, method, headers, body)

    def to_bytes(self) -> bytes:
        return b""

    @staticmethod
    def _extract_path(request_raw: bytes) -> str:
        return ""

    @staticmethod
    def _extract_method(request_raw: bytes) -> str:
        return ""

    @staticmethod
    def _extract_headers(request_raw: bytes) -> list[HttpHeader]:
        return []

    @staticmethod
    def _extract_body(request_raw: bytes) -> HttpBody:
        return HttpBody()
