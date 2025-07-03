# 录入数据
import json
import hashlib
import uuid
import time
import requests
from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
# sample 
class SaveClueRequest(BaseModel):
    orgids: str = Field("a7f0cd9c706c4673ad76bd36dc1f3249", description="组织ID")
    names: str = Field("你好", description="姓名")
    mobile: str = Field("11341994238", description="手机号")
    source: str = Field("consultdesk", description="来源")
    campusids: str = Field("032e060a2d174b34b8936d0f89525066", description="校区ID")
    businessids: List[str] = Field(["0958da4d98a643a6a117ee3f24c924e0"], description="业务ID列表")
    gender: str = Field("unknown", description="性别")
    studentstate: str = Field("student", description="学生状态")
    schooltype: str = Field("seniorHighSchool", description="学校类型")

router = APIRouter()

@router.post("/save_clue/")
async def save_clue(request_data: SaveClueRequest) -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/clue/save"
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}

    status_code, content = crm_builder.make_request(url, request_data.model_dump(), token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}

