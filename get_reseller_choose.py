# houtai/get_reseller_choose.py
import requests
from typing import Dict, Any
from search_school import CRMRequestBuilder, get_token

def get_reseller_choose() -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/reseller/choose"
    params = {
        "names": "",
        "mobile": "",
        "contactname": "",
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
        "pageNum": 1,
        "pageSize": 20
    }
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    status_code, content = crm_builder.make_request(url, params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}