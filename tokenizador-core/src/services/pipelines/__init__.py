from typing import Annotated
from fastapi import Depends
from src.services.pipelines.pipeline_v1 import PipelineV1

def build_pipeline_v1():
    return PipelineV1()

PipelineV1Dep = Annotated[PipelineV1, Depends(build_pipeline_v1)]
