from fastapi import APIRouter

router_operators = APIRouter()


@router_operators.post("/dry-run")
async def dry_run():
    return {"Hello": "World, operators"}
