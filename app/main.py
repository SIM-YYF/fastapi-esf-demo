import time

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from app import common
from app.routers.depends.common import validate_token_header
from app.routers.handler import event, exception
from app.routers.jobs import router_jobs
from app.routers.operators import router_operators


api = FastAPI(debug=True, title='backend-esf-interpreter', description='backend-esf-interpreter')

api.add_event_handler('startup', event.start_up)
api.add_event_handler('shutdown', event.shut_down)

api.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.add_middleware(GZipMiddleware)

api.add_exception_handler(StarletteHTTPException, exception.custom_http_exception_handler)
api.add_exception_handler(RequestValidationError, exception.validation_exception_handler)

api.include_router(router_jobs,
                   prefix="/esf/v1/jobs",
                   tags=["jobs"],
                   dependencies=[Depends(validate_token_header)]
                   )
api.include_router(router_operators,
                   prefix="/esf/v1/operators",
                   tags=["operators"],
                   dependencies=[Depends(validate_token_header)]
                   )


@api.middleware("http")
async def add_process_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers.update({'access-control-allow-origin': '*'})
    return response


if __name__ == "__main__":
    uvicorn.run(api, port=8806, loop='uvloop', log_level='debug')
