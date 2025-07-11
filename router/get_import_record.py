# 根据ID获取导入记录
import json
from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token
from pydantic import BaseModel, Field

class GetImportRecordRequest(BaseModel):
    ids: str = Field("c1a23d464df941ada6da81b04944d17c", description="导入记录ID")
    orgids: str = Field("a7f0cd9c706c4673ad76bd36dc1f3249", description="组织ID")

router = APIRouter()

@router.get("/get_import_record/")
async def get_import_record(
    ids: str = Query("c1a23d464df941ada6da81b04944d17c", description="导入记录ID"),
    orgids: str = Query("a7f0cd9c706c4673ad76bd36dc1f3249", description="组织ID")
) -> Dict[str, Any]:
    """
    根据ID获取导入记录
    """
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/clue/importrecord/by_id"
    
    # 获取token
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}

    # 构建请求参数
    params = {
        "ids": ids,
        "orgids": orgids
    }

    # 发送GET请求
    status_code, content = crm_builder.make_request(url, params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content} 