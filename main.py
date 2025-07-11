# main.py
from fastapi import FastAPI, Request
from router import get_market_activity, get_market_person, save_clue, get_clue, get_dict_tree, get_org_campus_list, get_org_business_list, get_schooltype_dict_tree, get_offline_ad_source_dict_tree, get_relation_dict_tree, get_leads_status_dict_tree, get_user_query, get_reseller_choose, search_school,validate_mobile,import_clue,get_import_record
import sys
import os
import httpx
from fastapi.routing import APIRoute
import logging
import json
from utils import extract_fields_get_market_activity, extract_fields, extract_fields_get_user_query, extract_fields_get_org_business_list, extract_fields_get_user_query, extract_fields_get_reseller_choose

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    title="CRM数据合并服务",
    description="用于管理和合并CRM相关数据的API服务",
    version="1.0.0"
)

app.include_router(get_dict_tree.router) # DONE
app.include_router(get_org_campus_list.router) # DONE
app.include_router(get_org_business_list.router)
app.include_router(get_schooltype_dict_tree.router)
app.include_router(get_offline_ad_source_dict_tree.router)
app.include_router(get_relation_dict_tree.router)
app.include_router(get_leads_status_dict_tree.router)
app.include_router(get_user_query.router)
app.include_router(get_reseller_choose.router)
app.include_router(get_clue.router) # DONE
app.include_router(search_school.router) # DONE
app.include_router(get_market_person.router) # DONE
app.include_router(get_market_activity.router) # DONE
app.include_router(import_clue.router)
app.include_router(save_clue.router)
app.include_router(validate_mobile.router)
app.include_router(get_import_record.router)






@app.get("/extract_all_fields/", tags=["tools"])
async def extract_all_fields(request: Request):
    """
    针对每个API接口自定义处理规则，提取'ids'、'names'、'numbers'等字段。
    """

    base_url = f"https{str(request.base_url).rstrip("/").lstrip("https").lstrip("http")}"
    results = []
    empty_fields_msgs = []  # 新增：用于收集fields为空的接口信息
    empty_response_msgs = []  # 新增：收集响应为空的接口信息

    async with httpx.AsyncClient() as client:
        # 1. search_school
        try:
            resp = await client.get(f"{base_url}/search_school/", params={"school_name": "济南一中"})
            data = resp.json()
            fields = extract_fields(data)
            if not fields:
                empty_fields_msgs.append("/search_school/ 的 fields 为空！")
            results.append({"path": "/search_school/", "fields": fields})
        except httpx.TimeoutException:
            results.append({"path": "/search_school/", "error": "请求超时"})
        except httpx.ConnectError:
            results.append({"path": "/search_school/", "error": "连接失败"})
        except Exception as e:
            print(e)
            results.append({"path": "/search_school/", "error": str(e)})

        # 2. get_clue
        try:
            resp = await client.get(f"{base_url}/get_clue/", params={"mobile": "12345678901"})
            data = resp.json()
            fields = extract_fields(data)
            if not fields:
                empty_fields_msgs.append("/get_clue/ 的 fields 为空！")
            results.append({"path": "/get_clue/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_clue/", "error": str(e)})

        # # 3. save_clue (POST)
        # try:
        #     resp = await client.post(f"{base_url}/save_clue/", json={
        #         "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
        #         "names": "测试线索",
        #         "mobile": "12345678901",
        #         "source": "consultdesk",
        #         "campusids": "032e060a2d174b34b8936d0f89525066",
        #         "businessids": ["0958da4d98a643a6a117ee3f24c924e0"],
        #         "gender": "unknown",
        #         "studentstate": "student",
        #         "schooltype": "seniorHighSchool"
        #     })
        #     data = resp.json()
        #     fields = extract_fields(data)
        #     if not fields:
        #         empty_fields_msgs.append("/save_clue/ 的 fields 为空！")
        #     results.append({"path": "/save_clue/", "fields": fields})
        # except Exception as e:
        #     results.append({"path": "/save_clue/", "error": str(e)})

        # 4. get_dict_tree
        try:
            resp = await client.get(f"{base_url}/get_dict_tree/")
            data = resp.json()
            fields = extract_fields(data)

            if not fields:
                empty_fields_msgs.append("/get_dict_tree/ 的 fields 为空！")
            results.append({"path": "/get_dict_tree/", "fields": data})
        except Exception as e:
            results.append({"path": "/get_dict_tree/", "error": str(e)})

        # 5. get_org_campus_list
        try:
            resp = await client.get(f"{base_url}/get_org_campus_list/")
            data = resp.json()
            fields = extract_fields(data)

            if not fields:
                empty_fields_msgs.append("/get_org_campus_list/ 的 fields 为空！")
            results.append({"path": "/get_org_campus_list/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_org_campus_list/", "error": str(e)})

        # 6. get_org_business_list
        try:
            resp = await client.get(f"{base_url}/get_org_business_list/")
            data = resp.json()
            fields = extract_fields_get_org_business_list(data)

            if not fields:
                empty_fields_msgs.append("/get_org_business_list/ 的 fields 为空！")
            results.append({"path": "/get_org_business_list/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_org_business_list/", "error": str(e)})

        # 7. get_schooltype_dict_tree
        try:
            resp = await client.get(f"{base_url}/get_schooltype_dict_tree/")
            if not resp.text.strip():
                empty_response_msgs.append("/search_school/ 返回空字符串！")
                print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
                
            data = resp.json()
            fields = extract_fields(data)
            if not fields:
                empty_fields_msgs.append("/get_schooltype_dict_tree/ 的 fields 为空！")
            results.append({"path": "/get_schooltype_dict_tree/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_schooltype_dict_tree/", "error": str(e)})

        # 8. get_offline_ad_source_dict_tree
        try:
            resp = await client.get(f"{base_url}/get_offline_ad_source_dict_tree/")
            data = resp.json()
            fields = extract_fields(data)
            if not fields:
                empty_fields_msgs.append("/get_offline_ad_source_dict_tree/ 的 fields 为空！")
            results.append({"path": "/get_offline_ad_source_dict_tree/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_offline_ad_source_dict_tree/", "error": str(e)})

        # 9. get_relation_dict_tree
        try:
            resp = await client.get(f"{base_url}/get_relation_dict_tree/")
            data = resp.json()
            fields = extract_fields(data)
            if not fields:
                empty_fields_msgs.append("/get_relation_dict_tree/ 的 fields 为空！")
            results.append({"path": "/get_relation_dict_tree/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_relation_dict_tree/", "error": str(e)})

        # 10. get_leads_status_dict_tree
        try:
            resp = await client.get(f"{base_url}/get_leads_status_dict_tree/")
            data = resp.json()
            fields = extract_fields(data)
            if not fields:
                empty_fields_msgs.append("/get_leads_status_dict_tree/ 的 fields 为空！")
            results.append({"path": "/get_leads_status_dict_tree/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_leads_status_dict_tree/", "error": str(e)})

        # 11. get_user_query
        try:
            resp = await client.get(f"{base_url}/get_user_query/")
            data = resp.json()
            fields = extract_fields_get_user_query(data)
            if not fields:
                empty_fields_msgs.append("/get_user_query/ 的 fields 为空！")
            results.append({"path": "/get_user_query/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_user_query/", "error": str(e)})

        # 12. get_reseller_choose
        try:
            resp = await client.get(f"{base_url}/get_reseller_choose/")
            data = resp.json()
            fields = extract_fields_get_reseller_choose(data)
            if not fields:
                empty_fields_msgs.append("/get_reseller_choose/ 的 fields 为空！")
            results.append({"path": "/get_reseller_choose/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_reseller_choose/", "error": str(e)})

        # 13. get_market_person
        try:
            resp = await client.get(f"{base_url}/get_market_person/")
            data = resp.json()
            fields = extract_fields_get_user_query(data)
            if not fields:
                empty_fields_msgs.append("/get_market_person/ 的 fields 为空！")
            results.append({"path": "/get_market_person/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_market_person/", "error": str(e)})

        # 12. get_market_activity
        try:
            resp = await client.get(f"{base_url}/get_market_activity/")
            data = resp.json()
            fields = extract_fields_get_market_activity(data)
            if not fields:
                empty_fields_msgs.append("/get_market_activity/ 的 fields 为空！")
            results.append({"path": "/get_market_activity/", "fields": fields})
        except Exception as e:
            results.append({"path": "/get_market_activity/", "error": str(e)})













        logging.info(f"接口调用结果: {results}")

        # 写入json文件
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump({"results": results}, f, ensure_ascii=False, indent=2)
            print("写入完成😅")

        # 最后统一输出fields为空的接口
        if empty_fields_msgs:
            print("\n以下接口的 fields 为空：")
            for msg in empty_fields_msgs:
                print(msg)
        else:
            print("所有接口的 fields 都不为空！")

        return {"results": results}