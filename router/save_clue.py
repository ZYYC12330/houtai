# 录入数据
import json
import hashlib
import uuid
import time
import requests
from typing import Dict, Any
from fastapi import APIRouter, Body
from router.crm_utils import CRMRequestBuilder, get_token
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional, Tuple

# # sample 
# class SaveClueRequest(BaseModel):
#     orgids: str = Field("a7f0cd9c706c4673ad76bd36dc1f3249", description="组织ID")
#     names: str = Field("你好", description="姓名")
#     mobile: str = Field("11341994238", description="手机号")
#     source: str = Field("consultdesk", description="来源")
#     campusids: str = Field("032e060a2d174b34b8936d0f89525066", description="校区ID")
#     businessids: List[str] = Field(["0958da4d98a643a6a117ee3f24c924e0"], description="业务ID列表")
#     gender: str = Field("unknown", description="性别")
#     studentstate: str = Field("student", description="学生状态")
#     schooltype: str = Field("seniorHighSchool", description="学校类型")

def create_crm_clue(
    data: Dict[str, Any],
    token: Optional[str] = None,
    platform_userids: str = "4645a321f95b4bce992685253bf01147",
    api_url: str = "https://testcrm.xhd.cn/api/clue/save",
    auto_fetch_token: bool = True
) -> Tuple[int, Dict[str, Any]]:
    """创建CRM线索
    
    Args:
        data: 线索数据
        token: 认证token，如果为空则自动获取
        platform_userids: 平台用户ID
        api_url: API请求URL
        auto_fetch_token: 当token为空时是否自动获取token
        
    Returns:
        状态码和响应内容
    """
    # 检查必要参数
    required_fields = ["orgids", "names", "mobile"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return 400, {"error": f"缺少必要的字段: {', '.join(missing_fields)}"}
    
    # 如果token为空且允许自动获取，则获取token
    if not token and auto_fetch_token:
        token = get_token()
        if not token:
            return 500, {"error": "获取token失败"}
    
    # 检查token是否存在
    if not token:
        return 401, {"error": "缺少认证token"}
    
    # 使用类中现有的方法生成签名和headers
    crm_builder = CRMRequestBuilder()
    timestamp = str(int(time.time() * 1000))
    nonce = str(uuid.uuid4())
    sign = crm_builder.generate_signature(data, timestamp, nonce)
    headers = crm_builder.build_headers(token, platform_userids, timestamp, nonce, sign)
    
    # 发送POST请求而不是GET请求
    try:
        response = requests.post(api_url, headers=headers, json=data, timeout=30)
        return response.status_code, response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
    except Exception as e:
        return 500, {"error": str(e)}


router = APIRouter()




@router.post("/save_clue/")
async def save_clue(request_data: Dict[str, Any] = Body(...)) -> Dict[str, Any]:
    status_code ,content = create_crm_clue(request_data)
    return {"status_code": status_code, "response": content}

'''
{
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
        "names": "你好",
        "mobile": "11341994238",
        "source": "consultdesk",
        "campusids": "032e060a2d174b34b8936d0f89525066",
        "businessids": ["0958da4d98a643a6a117ee3f24c924e0"],
        "gender": "unknown",
        "studentstate": "student",
        "schooltype": "seniorHighSchool"
    }

'''