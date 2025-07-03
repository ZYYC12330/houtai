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
from get_org_campus_list_new import get_org_campus_list_new  # 导入新函数
from get_user_query import get_user_query  # 导入新函数
from get_reseller_choose import get_reseller_choose  # 导入新函数

app = FastAPI()

# 封装获取 token 和处理错误的函数
def with_token(func):
    async def wrapper(*args, **kwargs):
        token = get_token()
        if not token:
            return {"status_code": 500, "response": {"error": "获取token失败"}}
        return await func(token, *args, **kwargs)
    return wrapper

@app.get("/search_school/")
async def search_school(school_name: str) -> Dict[str, Any]:
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

@app.get("/get_clue/")
async def get_clue(mobile: str) -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/clue/globle"
    request_params = {
        "customername": "",
        "mobile": mobile,
        "qq": "",
        "wechat": "",
        "pageNum": 1,
        "pageSize": 20,
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
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
@with_token
async def get_dict_tree_api(token: str) -> Dict[str, Any]:
    result = get_dict_tree(token)
    return result

@app.get("/get_org_campus_list/")
async def api_get_org_campus_list() -> Dict[str, Any]:
    result = get_org_campus_list()
    return result

@app.get("/get_org_business_list/")
@with_token
async def api_get_org_business_list(token: str) -> Dict[str, Any]:
    result = get_org_business_list(token)
    return result

@app.get("/get_schooltype_dict_tree/")
@with_token
async def api_get_schooltype_dict_tree(token: str) -> Dict[str, Any]:
    result = get_schooltype_dict_tree(token)
    return result

@app.get("/get_offline_ad_source_dict_tree/")
@with_token
async def api_get_offline_ad_source_dict_tree(token: str) -> Dict[str, Any]:
    result = get_offline_ad_source_dict_tree(token)
    return result

@app.get("/get_relation_dict_tree/")
@with_token
async def api_get_relation_dict_tree(token: str) -> Dict[str, Any]:
    result = get_relation_dict_tree(token)
    return result

@app.get("/get_leads_status_dict_tree/")
@with_token
async def api_get_leads_status_dict_tree(token: str) -> Dict[str, Any]:
    result = get_leads_status_dict_tree(token)
    return result

@app.get("/get_org_campus_list_new/")
async def api_get_org_campus_list_new() -> Dict[str, Any]:
    result = get_org_campus_list_new()
    return result

@app.get("/get_user_query/")
@with_token
async def api_get_user_query(token: str) -> Dict[str, Any]:
    result = get_user_query(token)
    return result

@app.get("/get_reseller_choose/")
async def api_get_reseller_choose() -> Dict[str, Any]:
    result = get_reseller_choose()
    return result