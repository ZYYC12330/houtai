# houtai/get_org_business_list.py
import requests
from typing import Dict, Any
from fastapi import APIRouter, Query
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.get("/search_school/")

async def get_org_business_list(token: str, user_ids: str = "4645a321f95b4bce992685253bf01147") -> Dict[str, Any]:
    url = "https://testcrm.xhd.cn/api/common/org_business/list?orgids=a7f0cd9c706c4673ad76bd36dc1f3249"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-TW;q=0.5",
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
        "crm-version": "1.0.2",
        "platform-orgshow": "0",
        "platform-userids": user_ids,
        "priority": "u=1, i",
        "referer": "https://testcrm.xhd.cn/",
        "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "x-auth-app": "NC-CRM",
        "x-auth-nonce": "f8c13b74-08a6-4478-bf8a-6c0a97ac469e",
        "x-auth-sign": "8CE484C38298636181BBDBFF872B4E88",
        "x-auth-timestamp": "1751445091033"
    }
    try:
        response = requests.get(url, headers=headers)
        return {"status_code": response.status_code, "response": response.json()}
    except Exception as e:
        return {"status_code": 500, "response": {"error": str(e)}}