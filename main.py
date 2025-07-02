# main.py
from fastapi import FastAPI
import sys
import os
from typing import Dict, Any
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from search_school import CRMRequestBuilder, get_token
from get_dict_tree import get_dict_tree
from org_campus_list import get_org_campus_list  # 导入新函数
from get_org_business_list import get_org_business_list  # 导入新函数
from get_schooltype_dict_tree import get_schooltype_dict_tree
from get_offline_ad_source_dict_tree import get_offline_ad_source_dict_tree  # 导入新函数
from get_relation_dict_tree import get_relation_dict_tree 
from get_leads_status_dict_tree import get_leads_status_dict_tree

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


@app.get("/get_dict_tree/")
async def get_dict_tree_api() -> Dict[str, Any]:
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    result = get_dict_tree(token)
    return result


@app.get("/get_org_campus_list/")
async def api_get_org_campus_list() -> Dict[str, Any]:
    result = get_org_campus_list()
    return result


@app.get("/get_org_business_list/")
async def api_get_org_business_list() -> Dict[str, Any]:
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    result = get_org_business_list(token)
    return result


@app.get("/get_schooltype_dict_tree/")
async def api_get_schooltype_dict_tree() -> Dict[str, Any]:
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    result = get_schooltype_dict_tree(token)
    return result


@app.get("/get_offline_ad_source_dict_tree/")
async def api_get_offline_ad_source_dict_tree() -> Dict[str, Any]:
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    result = get_offline_ad_source_dict_tree(token)
    return result



@app.get("/get_relation_dict_tree/")
async def api_get_relation_dict_tree() -> Dict[str, Any]:
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    result = get_relation_dict_tree(token)
    return result


@app.get("/get_leads_status_dict_tree/")
async def api_get_leads_status_dict_tree() -> Dict[str, Any]:
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    result = get_leads_status_dict_tree(token)
    return result