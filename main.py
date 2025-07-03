# main.py
from fastapi import FastAPI
from router import save_clue, get_dict_tree, get_org_campus_list, get_org_business_list, get_schooltype_dict_tree, get_offline_ad_source_dict_tree, get_relation_dict_tree, get_leads_status_dict_tree, get_user_query, get_reseller_choose, search_school
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    title="CRM数据合并服务",
    description="用于管理和合并CRM相关数据的API服务",
    version="1.0.0"
)

app.include_router(get_dict_tree.router)
app.include_router(get_org_campus_list.router)
app.include_router(get_org_business_list.router)
app.include_router(get_schooltype_dict_tree.router)
app.include_router(get_offline_ad_source_dict_tree.router)
app.include_router(get_relation_dict_tree.router)
app.include_router(get_leads_status_dict_tree.router)
app.include_router(get_user_query.router)
app.include_router(get_reseller_choose.router)
app.include_router(save_clue.router)

app.include_router(search_school.router)





# # 封装获取 token 和处理错误的函数
# def with_token(func):
#     async def wrapper(*args, **kwargs):
#         token = get_token()
#         if not token:
#             return {"status_code": 500, "response": {"error": "获取token失败"}}
#         return await func(token, *args, **kwargs)
#     return wrapper



# @app.get("/get_clue/")
# async def get_clue(mobile: str) -> Dict[str, Any]:
#     crm_builder = CRMRequestBuilder()
#     url = "https://testcrm.xhd.cn/api/clue/globle"
#     request_params = {
#         "customername": "",set http_proxy=http://127.0.0.1:7890 & set https_proxy=http://127.0.0.1:7890
#         "mobile": mobile,
#         "qq": "",
#         "wechat": "",
#         "pageNum": 1,
#         "pageSize": 20,
#         "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249"
#     }
#     token = get_token()
#     if not token:
#         return {"status_code": 500, "response": {"error": "获取token失败"}}
#     status_code, content = crm_builder.make_request(url, request_params, token, "4645a321f95b4bce992685253bf01147")
#     return {"status_code": status_code, "response": content}

# @app.post("/save_clue/")
# async def save_clue(data: Dict[str, Any]) -> Dict[str, Any]:
#     crm_builder = CRMRequestBuilder()
#     url = "https://testcrm.xhd.cn/api/clue/save"
#     token = get_token()
#     if not token:
#         return {"status_code": 500, "response": {"error": "获取token失败"}}
#     status_code, content = crm_builder.make_request(url, data, token, "4645a321f95b4bce992685253bf01147")
#     return {"status_code": status_code, "response": content}

# # @app.get("/get_dict_tree/")
# # @with_token
# # async def get_dict_tree_api(token: str) -> Dict[str, Any]:
# #     result = get_dict_tree(token)
# #     return result

# @app.get("/get_org_campus_list/")
# async def api_get_org_campus_list() -> Dict[str, Any]:
#     result = get_org_campus_list()
#     return result

# @app.get("/get_org_business_list/")
# @with_token
# async def api_get_org_business_list(token: str) -> Dict[str, Any]:
#     result = get_org_business_list(token)
#     return result

# @app.get("/get_schooltype_dict_tree/")
# @with_token
# async def api_get_schooltype_dict_tree(token: str) -> Dict[str, Any]:
#     result = get_schooltype_dict_tree(token)
#     return result

# @app.get("/get_offline_ad_source_dict_tree/")
# @with_token
# async def api_get_offline_ad_source_dict_tree(token: str) -> Dict[str, Any]:
#     result = get_offline_ad_source_dict_tree(token)
#     return result

# @app.get("/get_relation_dict_tree/")
# @with_token
# async def api_get_relation_dict_tree(token: str) -> Dict[str, Any]:
#     result = get_relation_dict_tree(token)
#     return result

# @app.get("/get_leads_status_dict_tree/")
# @with_token
# async def api_get_leads_status_dict_tree(token: str) -> Dict[str, Any]:
#     result = get_leads_status_dict_tree(token)
#     return result

# @app.get("/get_org_campus_list_new/")
# async def api_get_org_campus_list_new() -> Dict[str, Any]:
#     result = get_org_campus_list_new()
#     return result

# @app.get("/get_user_query/")
# @with_token
# async def api_get_user_query(token: str) -> Dict[str, Any]:
#     result = get_user_query(token)
#     return result

# @app.get("/get_reseller_choose/")
# async def api_get_reseller_choose() -> Dict[str, Any]:
#     result = get_reseller_choose()
#     return result