# 查电话
import json
import hashlib
import uuid
import time
import requests
from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.get("/get_phone/")
async def get_phone():
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/clue/globle"
    token = get_token()
    if not token:
        print("状态码: 500")
        print('响应内容: {"error": "获取token失败"}')
        return
    
    request_params = {
        "customername": "",
        "mobile": "16638117957",
        "qq": "",
        "wechat": "",
        "pageNum": 1,
        "pageSize": 20,
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }
    
    status_code, content = crm_builder.make_request(url, request_params, token, "4645a321f95b4bce992685253bf01147")
    
    print(f"状态码: {status_code}")
    print(f"响应内容: {json.dumps(content, indent=2, ensure_ascii=False)}")
