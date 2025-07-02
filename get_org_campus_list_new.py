# houtai/get_org_campus_list_new.py
import requests
import uuid
import time
import hashlib
from typing import Dict, Any

class CRMRequestBuilder:
    def __init__(self, app_secret: str = "HEeY89y(E_XbHaH7z0krYTq_K4YrQ~g+bh"):
        self.app_secret = app_secret
        self.app_id = "NC-CRM"
        self.crm_version = "1.0.2"

    def process_request_data(self, data: Dict[str, Any]) -> str:
        filtered_data = {}
        for key, value in data.items():
            if value == "" or isinstance(value, (dict, list)):
                continue
            filtered_data[key] = value
        return "&".join([f"{key}={filtered_data[key]}" for key in sorted(filtered_data.keys())])

    def generate_signature(self, data: Dict[str, Any], timestamp: str, nonce: str) -> str:
        processed_data = self.process_request_data(data)
        return hashlib.md5(f"{self.app_secret}{timestamp}{processed_data}{nonce}{self.app_secret}".encode('utf-8')).hexdigest().upper()

    def build_headers(self, token: str, platform_userids: str, timestamp: str = None, nonce: str = None, sign: str = None) -> Dict[str, str]:
        timestamp = timestamp or str(int(time.time() * 1000))
        nonce = nonce or str(uuid.uuid4())
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-TW;q=0.5",
            "authorization": f"Bearer {token}",
            "content-type": "application/json",
            "crm-version": self.crm_version,
            "platform-orgshow": "0",
            "platform-userids": platform_userids,
            "priority": "u=1, i",
            "referer": "https://testcrm.xhd.cn/",
            "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
            "x-auth-app": self.app_id,
            "x-auth-nonce": nonce,
            "x-auth-timestamp": timestamp
        }
        if sign:
            headers["x-auth-sign"] = sign
        return headers

    def make_request(self, url: str, params: Dict[str, Any], token: str, platform_userids: str):
        timestamp = str(int(time.time() * 1000))
        nonce = str(uuid.uuid4())
        sign = self.generate_signature(params, timestamp, nonce)
        headers = self.build_headers(token, platform_userids, timestamp, nonce, sign)
        try:
            response = requests.get(url, headers=headers, params=params)
            return response.status_code, response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
        except Exception as e:
            return 500, {"error": str(e)}


def get_token():
    try:
        response = requests.post(
            url='https://testsso.xhd.cn/auth/realms/newchannel-enterprise/protocol/openid-connect/token',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'client_id': 'crm-web',
                'grant_type': 'password',
                'username': 'jinlehui@xhd.cn',
                'password': 'Langcore6789'
            }
        )
        response.raise_for_status()
        return response.json().get('access_token')
    except Exception:
        return None


def get_org_campus_list_new():
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/common/org_campus/list"
    params = {
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }
    token = get_token()
    if not token:
        return {"status_code": 500, "response": {"error": "获取token失败"}}
    status_code, content = crm_builder.make_request(url, params, token, "4645a321f95b4bce992685253bf01147")
    return {"status_code": status_code, "response": content}