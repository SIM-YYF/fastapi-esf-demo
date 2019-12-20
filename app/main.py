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
from app.routers.handlers import event, exception
from app.routers.jobs import router_jobs
from app.routers.middlewares.http_midware import HttpMiddleWare
from app.routers.operators import router_operators

api = FastAPI(debug=True, title='backend-esf-interpreter', description='backend-esf-interpreter')

api.add_event_handler('startup', event.start_up)
api.add_event_handler('shutdown', event.shut_down)

# cors
api.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 压缩数据
api.add_middleware(GZipMiddleware)
# http请求监控
api.add_middleware(HttpMiddleWare)
# 全局自定义HTTP异常
api.add_exception_handler(StarletteHTTPException, exception.custom_http_exception_handler)
# 全局请求验证异常
api.add_exception_handler(RequestValidationError, exception.validation_exception_handler)
# 添加路由-jobs
api.include_router(router_jobs,
                   prefix="/esf/v1/jobs",
                   tags=["jobs"],
                   dependencies=[Depends(validate_token_header)]
                   )
# 添加路由-operators
api.include_router(router_operators,
                   prefix="/esf/v1/operators",
                   tags=["operators"],
                   dependencies=[Depends(validate_token_header)]
                   )

if __name__ == "__main__":
    uvicorn.run(api, port=8806, loop='uvloop', log_level='trace', debug=True)
