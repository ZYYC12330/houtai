import json
import hashlib
import uuid
import time
import requests
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
            "accept": "application/json",
            "authorization": f"Bearer {token}",
            "content-type": "application/json",
            "crm-version": self.crm_version,
            "platform-userids": platform_userids,
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
            response = requests.get(url, headers=headers, params=params, timeout=30)
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

def main():
    crm_builder = CRMRequestBuilder()
    url = "https://testcrm.xhd.cn/api/common/school/page"
    token = get_token()
    if not token:
        print("状态码: 500")
        print('响应内容: {"error": "获取token失败"}')
        return
    
    # 注意：这里对URL中的中文进行了URL编码
    request_params = {
        "names": "东北林业",  # 对应URL中的编码 %E4%B8%9C%E5%8C%97%E6%9E%97%E4%B8%9A
        "type": "seniorHighSchool",
        "pageNum": 1,
        "pageSize": 20,
        "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
    }
    
    status_code, content = crm_builder.make_request(url, request_params, token, "4645a321f95b4bce992685253bf01147")
    
    print(f"状态码: {status_code}")
    print(f"响应内容: {json.dumps(content, indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    main()