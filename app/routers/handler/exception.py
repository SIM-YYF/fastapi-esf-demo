from typing import Any

from fastapi import HTTPException
from fastapi.exception_handlers import (
    request_validation_exception_handler,
)
from starlette.requests import Request
from starlette.responses import JSONResponse


class K2HTTPException(HTTPException):
    def __init__(
            self, status_code: int, message: Any = None, info: Any = None, code: int = -1, headers: dict = None
    ) -> None:
        super().__init__(status_code=status_code, detail=message)
        self.headers = headers
        self.info = info
        self.code = code


async def custom_http_exception_handler(request: Request, exc: K2HTTPException):
    print(f"---- OMG! An HTTP error!: {exc}")
    print(f"---- OMG! An HTTP request!: {request}")
    headers = getattr(exc, "headers", None)
    if headers:
        return JSONResponse(
            {"message": exc.detail, "info": exc.info, "code": exc.code}, status_code=exc.status_code, headers=headers
        )
    else:
        return JSONResponse(
            {"message": exc.detail, "info": exc.info, "code": exc.code}, status_code=exc.status_code
        )


async def validation_exception_handler(request: Request, exc):
    return await request_validation_exception_handler(request, exc)
