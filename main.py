from fastapi import FastAPI
import sys
import os
from typing import Dict, Any
import json

# 将search_school.py所在目录添加到系统路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from save_data import CRMRequestBuilder, get_token

app = FastAPI()

@app.get("/search_school/")
async def search_school(school_name: str) -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/common/school/page"
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}

    request_params = {
        "names": school_name,
        "type": "seniorHighSchool",
        "pageNum": 1,
        "pageSize": 20,
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }

    status_code, content = crm_builder.make_request(url, request_params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}

@app.get("/get_clue/")
async def get_clue(mobile: str) -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/clue/globle"
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}

    request_params = {
        "customername": "",
        "mobile": mobile,
        "qq": "",
        "wechat": "",
        "pageNum": 1,
        "pageSize": 20,
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }

    status_code, content = crm_builder.make_request(url, request_params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}

@app.post("/save_clue/")
async def save_clue(data: Dict[str, Any]) -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/clue/save"
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}

    status_code, content = crm_builder.make_request(url, data, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}