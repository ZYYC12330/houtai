import json
from typing import Dict, Any 


def map_input_data(input_path: str, mapping_path: str, output_path: str) -> None:
    """
    将 input_path 中的用户输入字段，按 mapping_path 映射表转换后保存到 output_path。
    """
    # 读取文件内容
    with open(input_path, 'r', encoding='utf-8') as f:
        input_data = json.load(f)['data']

    with open(mapping_path, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    # 构建映射字典
    name2id = {item['names']: item['ids'] for item in mapping if 'names' in item and 'ids' in item}
    name2number = {item['names']: item['numbers'] for item in mapping if 'names' in item and 'numbers' in item}
    businessname2id = {item['businessname']: item['businessids'] for item in mapping if 'businessname' in item}
    username2id = {item['names']: item['ids'] for item in mapping if item.get('usertype') == 'assistant'}
    marketname2id = {item['names']: item['ids'] for item in mapping if item.get('usertype') == 'market'}

    advancestatus_map = {
    "未处理": "undispose",
    "有效": "valid",
    "无效": "void",
    "关闭": "close"
    }  

    relation_map = {
    "本人": "oneself",
    "母亲": "mother",
    "父亲": "father"
    }

    studentstate_map = {
    "在校": "student",
    "在职": "onjob"
    }

    # 字段处理逻辑
    output: Dict[str, Any] = {
        'orgids': "a7f0cd9c706c4673ad76bd36dc1f3249",
        'names': input_data.get('names', ''),
        'mobile': input_data.get('mobile', ''),
        'source': name2number.get(input_data.get('source', ''), ''),
        'resellername': input_data.get('resellername', ''),
        'resellerids': name2id.get(input_data.get('resellername', ''), ''),
        'activityname': '',
        'activityids': '',
        'referrername': '',
        'referrerids': '',
        'campusids': name2id.get(input_data.get('campusids', ''), ''),
        'businessids': [
            businessname2id.get(b.strip(), "") for b in input_data.get('businessids', '').split(',') if b.strip()
        ],
        'usernames': '',
        'userids': username2id.get(input_data.get('usernames', ''), ''),
        'marketnames': '',
        'marketuserids': marketname2id.get(input_data.get('marketnames', ''), ''),
        'offlineadsource': name2number.get(input_data.get('offlineadsource', ''), ''),
        'gender': name2number.get(input_data.get('gender', ''), ''),

        'telphone': input_data.get('telphone', ''),
        'wechat': input_data.get('wechat', ''),
        'qq': input_data.get('qq', ''),
        'email': input_data.get('email', ''),
        'fathermobile': input_data.get('fathermobile', ''),
        'mothermobile': input_data.get('mothermobile', ''),
        'advancestatus': advancestatus_map.get(input_data.get('advancestatus', ''), ''),
        'relation': relation_map.get(input_data.get('relation', ''), ''),
        'studentstate': studentstate_map.get(input_data.get('studentstate', ''), ''),
        "schooltype": name2number.get(input_data.get('schooltype', ''), ''),
        'schoolname': input_data.get('schoolname', ''),
        'schoolenrollment': input_data.get('schoolenrollment', ''),
        'professionname': input_data.get('professionname', ''),
        'companyname': "",
        'positionname': "",
        'note': input_data.get('note', ''),




    }

    # 保存结果
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)

    print()
    print(f"映射转换完成，结果已保存到 {output_path}")

