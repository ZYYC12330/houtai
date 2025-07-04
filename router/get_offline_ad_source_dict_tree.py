# houtai/get_offline_ad_source_dict_tree.py
# 校园餐桌广告
import requests
from typing import Dict, Any
from fastapi import APIRouter, Query, Depends
from router.crm_utils import CRMRequestBuilder, get_token

router = APIRouter()

@router.get("/get_offline_ad_source_dict_tree/")

async def get_offline_ad_source_dict_tree(token: str = Depends(get_token), user_ids: str = "4645a321f95b4bce992685253bf01147") -> Dict[str, Any]:
    url = "https://testcrm.xhd.cn/api/common/dict/tree?numbers=offlineAdSource&orgids=a7f0cd9c706c4673ad76bd36dc1f3249"
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
        "x-auth-nonce": "b764fce4-f1a0-43e3-d22c-ce429d3182ec",
        "x-auth-sign": "1603951A186AF1724249CEE9F01B2C54",
        "x-auth-timestamp": "1751446094470"
    }
    try:
        response = requests.get(url, headers=headers)
        return {"status_code": response.status_code, "response": response.json()}
    except Exception as e:
        return {"status_code": 500, "response": {"error": str(e)}}