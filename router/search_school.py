# 查学校
import json
import hashlib
import uuid
import time
import requests
from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.get("/search_school/")
# @router.get("/search_schoolAAAAA/") # 改的是docs显示的名字，不影响功能~~~
async def search_school(school_name: str = Query('济南一中')) -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/common/school/page"
    request_params = {
        "names": school_name,
        "type": "seniorHighSchool",
        "pageNum": 1,
        "pageSize": 20,
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    status_code, content = crm_builder.make_request(url, request_params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}

