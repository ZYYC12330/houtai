#  是否存在于其他学校

from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.get("/validate_mobile/")
async def validate_mobile(mobile: str) -> Dict[str, Any]:
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/common/field/valid"
    request_params = {
        "customerids": "",
        "value": mobile,
        "type":"mobile",
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }
    
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    status_code, content = crm_builder.make_request(url, request_params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}