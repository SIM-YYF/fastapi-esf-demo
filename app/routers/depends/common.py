from fastapi import Header, Query, HTTPException, Depends, Cookie


async def validate_token_header(x_token: str = Header(default='xx', description='header-1'),
                                y_token: str = Header(default='yy', description='header-2')):
    print('验证x_toke === > ', x_token)
    print('验证y_toke === > ', y_token)
    # if x_token != "fake-super-secret-token":
    #     raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_token(x_token: str = Header(default='fake-super-secret-token')):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(default='fake-super-secret-key')):
    print('验证key =  ', x_key)
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


async def paging_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}



