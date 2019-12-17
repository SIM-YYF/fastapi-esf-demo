from fastapi import Header, HTTPException


async def validate_token_header(x_token: str = Header(default='x_token_value')):
    print('验证toke === > ', x_token)
    # if x_token != "fake-super-secret-token":
    #     raise HTTPException(status_code=400, detail="X-Token header invalid")


async def paging_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
