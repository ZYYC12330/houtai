import requests

data = {
    "orgids": "a7f0cd9c706c4673ad76bd36dc1f3249",
    "names": "测试",
    "mobile": "13410870301",
    "source": "reseller",
    "resellername": "无推荐人",
    "resellerids": "a62cebf9a4504e25a3433a75ae952420",
    "activityname": "",
    "activityids": "",
    "referrername": "",
    "referrerids": "",
    "campusids": "d5fd3130f86749ccb14e2db0e6db13ad",
    "businessids": ["be674afb31154d51a0152440f8b851f7"],
    "usernames": "",
    "userids": "f8d3a32387024182b52545be4cd59ea7",
    "marketnames": "",
    "marketuserids": "2dc6df8e3b6c4531bca5fd91188fac64",
    "offlineadsource": "",
    "gender": "unknown",
    "telphone": "",
    "wechat": "",
    "qq": "",
    "email": "",
    "fathermobile": "",
    "mothermobile": "",
    "advancestatus": "",
    "relation": "",
    "studentstate": "student",
    "schooltype": "seniorHighSchool",
    "schoolname": "南宫高中",
    "schoolenrollment": "",
    "professionname": "",
    "companyname": "",
    "positionname": "",
    "note": "【测试\n13410870301\n渠道代理\n无推荐人\n上海徐家汇校区\n大学四级×\n鲁鹏飞(135**1105)\n安稳】"
}

response = requests.post("http://localhost:8000/save_clue/", json=data)
print(response.json())