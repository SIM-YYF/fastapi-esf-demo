from fastapi import APIRouter
from fastapi import Depends
from app.routers.depends import common, jobs
from app.models.jobs import Jobs

router_jobs = APIRouter()


@router_jobs.post("/submit/{job_id}",
                  dependencies=[Depends(common.verify_key)],
                  name='提交作业')
async def submit_jobs(job_id: str = None, b_jobs: Jobs = Depends(jobs.post_body)):
    print(job_id)
    print(b_jobs)
    return {"Hello": "World, jobs"}


@router_jobs.post("/submit1",
                  dependencies=[Depends(common.verify_key), Depends(common.paging_parameters)],
                  name='提交作业1')
async def submit_jobs1(paging: dict = None):
    print(paging)
    return {"Hello": "World, jobs"}


@router_jobs.post("/submit2", name='提交作业2')
async def submit_jobs2(dep_query_file: str = Depends(jobs.query_or_cookie_extractor)):
    print('ad_dep =', dep_query_file)
    return {"Hello": "World, jobs"}


@router_jobs.post("/submi3",
                  dependencies=[Depends(common.verify_key), Depends(jobs.checker)],
                  name='提交作业3')
async def submit_jobs3(paging: dict = None):
    print(paging)
    return {"Hello": "World, jobs"}
