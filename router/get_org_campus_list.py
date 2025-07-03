# org_campus_list.py
# 获取校区列表
import requests
import uuid
import time
import hashlib
from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.get("/get_org_campus_list/")
async def get_org_campus_list():
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/common/org_campus/list"
    params = {
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    status_code, content = crm_builder.make_request(url, params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}
