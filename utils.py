
    
def extract_fields(obj, fields=("ids", "names", "numbers"), collected=None):
    if collected is None:
        collected = []
    if isinstance(obj, dict):
        # 如果当前dict有全部目标字段，则收集
        if all(f in obj for f in fields):
            collected.append({f: obj[f] for f in fields})
        # 递归遍历所有value
        for v in obj.values():
            if isinstance(v, (dict, list)):
                extract_fields(v, fields, collected)
    elif isinstance(obj, list):
        for item in obj:
            extract_fields(item, fields, collected)
    return collected

#  {
#         "ids": "022f81c23ae04d299030ea33ee4c5bd2",
#         "version": "",
#         "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
#         "businessids": "0958da4d98a643a6a117ee3f24c924e0",
#         "status": "1",
#         "businessname": "SSAT"
#       },
#       {
#         "ids": "06d53ae59d82432f9ec61508bda953c8",
#         "version": "",
#         "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
#         "businessids": "f39f28b9b7b343a9a2a570fb9d9532b8",
#         "status": "1",
#         "businessname": "SAT"
#       },
def extract_fields_get_org_business_list(obj, fields=("ids", "businessids", "businessname"), collected=None):
    if collected is None:
        collected = []
    if isinstance(obj, dict):
        # 如果当前dict有全部目标字段，则收集
        if all(f in obj for f in fields):
            collected.append({f: obj[f] for f in fields})
        # 递归遍历所有value
        for v in obj.values():
            if isinstance(v, (dict, list)):
                extract_fields_get_org_business_list(v, fields, collected)
    elif isinstance(obj, list):
        for item in obj:
            extract_fields_get_org_business_list(item, fields, collected)
    return collected

#  {
#         "ids": "5186a7839f494a3f9e3a8b4aa1d1c61e",
#         "status": "1",
#         "username": "hanjian",
#         "departmentids": null,
#         "stationids": null,
#         "email": "hanjian@xhd.cn",
#         "mobile": "135****7270",
#         "names": "韩健",
#         "usertype": "market",
#         "createtime": null,
#         "updateuserids": null,
#         "updatetime": null,
#         "showall": 0,
#         "businessshow": "0",
#         "sourceshow": "1",
#         "onlinecontractshow": "0",
#         "tqid": null,
#         "classtypeshow": null,
#         "echelon": null,
#         "orgshow": "0",
#         "updatepassword": null,
#         "photo": "",
#         "maincampusids": null,
#         "orgids": "",
#         "roleids": "",
#         "super": false
#       },
def extract_fields_get_user_query(obj, fields=("username", "names", "mobile", "email"), collected=None):
    if collected is None:
        collected = []
    if isinstance(obj, dict):
        # 如果当前dict有全部目标字段，则收集
        if all(f in obj for f in fields):
            collected.append({f: obj[f] for f in fields})
        # 递归遍历所有value
        for v in obj.values():
            if isinstance(v, (dict, list)):
                extract_fields_get_user_query(v, fields, collected)
    elif isinstance(obj, list):
        for item in obj:
            extract_fields_get_user_query(item, fields, collected)
    return collected

#  {
#           "ids": "7ef38b6abe324144b3dc4c4bca1ba90a",
#           "version": 0,
#           "type": "0",
#           "status": "1",
#           "names": "合肥留学王老师",
#           "contactname": null,
#           "gender": "unknown",
#           "mobile": null,
#           "telphone": null,
#           "wechat": null,
#           "qq": null,
#           "email": null,
#           "parentids": null,
#           "country": null,
#           "province": null,
#           "city": null,
#           "district": null,
#           "address": null,
#           "companyname": null,
#           "positionname": null,
#           "createuserids": "f1b0a0250280462cbac6a6ec117a431b",
#           "createtime": "2017-11-02 11:05:44",
#           "updateuserids": null,
#           "updatetime": null,
#           "note": null,
#           "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
#           "marketuserids": "",
#           "orgnames": "新航道上海学校",
#           "marketusernames": null,
#           "isUse": true,
#           "gendernames": "未知"

#           /get_reseller_choose/

def extract_fields_get_reseller_choose(obj, fields=("ids", "names"), collected=None):
    if collected is None:
        collected = []
    if isinstance(obj, dict):
        # 如果当前dict有全部目标字段，则收集
        if all(f in obj for f in fields):
            collected.append({f: obj[f] for f in fields})
        # 递归遍历所有value
        for v in obj.values():
            if isinstance(v, (dict, list)):
                extract_fields(v, fields, collected)
    elif isinstance(obj, list):
        for item in obj:
            extract_fields(item, fields, collected)
    return collected
