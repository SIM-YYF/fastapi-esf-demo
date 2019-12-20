from fastapi import Body, Depends

from app.models.jobs import Jobs


async def dep_job_bods(x_body: dict = Body(default={'name': 'esf'}, description='作业提交body体')):
    print('----dep job bodys', x_body)


def query_extractor(sub_q: str = 'sub_qxxx'):
    return sub_q


def query_or_cookie_extractor(
        sub_q: str = Depends(query_extractor), last_query: str = 'not sub_q'
):
    if not sub_q:
        return last_query
    return sub_q


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, ad_dep: str = ""):
        if ad_dep:
            return self.fixed_content in ad_dep
        return False


checker = FixedContentQueryChecker("bar")


def post_body(jobsx: Jobs = Body(default=None, embed=True, description='提交作业实体body')):
    print('xxxxxxx jobs =', type(jobsx))
    print('xxxxxxx jobs =', jobsx)
    return jobsx
