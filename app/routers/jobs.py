from fastapi import APIRouter


router_jobs = APIRouter()


@router_jobs.post("/submit")
async def submit_jobs():
    return {"Hello": "World, jobs"}
