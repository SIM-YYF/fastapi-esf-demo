import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class HttpMiddleWare(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp):
        super(HttpMiddleWare, self).__init__(app=app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        response.headers.update({'access-control-allow-origin': '*'})
        return response
