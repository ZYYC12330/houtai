# main.py
from fastapi import FastAPI, Request
from router import extract_all_fields, get_market_activity, get_market_person, save_clue, get_clue, get_dict_tree, get_org_campus_list, get_org_business_list, get_schooltype_dict_tree, get_offline_ad_source_dict_tree, get_relation_dict_tree, get_leads_status_dict_tree, get_user_query, get_reseller_choose, search_school,validate_mobile,import_clue,get_import_record
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
app.include_router(extract_all_fields.router)
