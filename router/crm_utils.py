import hashlib
import uuid
import time
import requests
from typing import Dict, Any, Optional

import requests
import logging

def get_token():
    """获取认证token"""
    url = 'https://testsso.xhd.cn/auth/realms/newchannel-enterprise/protocol/openid-connect/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'client_id': 'crm-web',
        'grant_type': 'password',
        'username': 'jinlehui@xhd.cn',
        'password': 'Langcore6789'
    }
    
    try:
        logging.debug(f"请求获取token: {url}")
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # 检查HTTP状态码
        
        token_data = response.json()
        access_token = token_data.get('access_token')
        
        if not access_token:
            raise ValueError("响应中未包含access_token字段")
            
        return access_token
        
    except requests.exceptions.HTTPError as e:
        # 处理HTTP错误（4xx, 5xx）
        logging.error(f"获取token失败，HTTP错误: {e}")
        logging.error(f"响应内容: {response.text}")
        raise RuntimeError(f"认证失败，HTTP状态码: {response.status_code}") from e
        
    except requests.exceptions.RequestException as e:
        # 处理网络连接错误
        logging.error(f"获取token失败，网络错误: {e}")
        raise RuntimeError("无法连接到认证服务器") from e
        
    except ValueError as e:
        # 处理无效响应格式
        logging.error(f"获取token失败，响应格式错误: {e}")
        raise RuntimeError("认证服务器返回无效响应") from e
        
    except Exception as e:
        # 处理其他未知错误
        logging.error(f"获取token失败，未知错误: {e}")
        raise RuntimeError("获取token时发生未知错误") from e

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
    
    def build_headers(self, token: str, platform_userids: str, timestamp: Optional[str] = None, nonce: Optional[str] = None, sign: Optional[str] = None) -> Dict[str, str]:
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