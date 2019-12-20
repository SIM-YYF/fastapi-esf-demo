from typing import List, Dict

from pydantic import BaseModel


class Tag(BaseModel):
    taskId: str


class Input(BaseModel):
    inputParamName: str


class Jobs(BaseModel):
    name: str
    description: str = None
    tags: Tag = None
    inputs: List[Input] = None