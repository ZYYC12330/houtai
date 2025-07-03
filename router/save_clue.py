# 录入数据
import json
import hashlib
import uuid
import time
import requests
from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.post("/save_clue/")
async def save_clue():
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/clue/save"
    token = get_token()
    if not token:
        print("状态码: 500")
        print('响应内容: {"error": "获取token失败"}')
        return

    # sample 
    request_data = {
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
        "names": "你好",
        "mobile": "11341994238",
        "source": "consultdesk",
        "campusids": "032e060a2d174b34b8936d0f89525066",
        "businessids": ["0958da4d98a643a6a117ee3f24c924e0"],
        "gender": "unknown",
        "studentstate": "student",
        "schooltype": "seniorHighSchool",
    }
    
    status_code, content = crm_builder.make_request(url, request_data, token, "4645a321f95b4bce992685253bf01147")
    
    print(f"状态码: {status_code}")
    print(f"响应内容: {json.dumps(content, indent=2, ensure_ascii=False)}")

