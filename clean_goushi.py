import json

# 读取 JSON 文件
with open('goushi.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 定义一个递归函数来展平嵌套结构
def flatten_nodes(nodes):
    flattened = []
    for node in nodes:
        # 复制当前节点，去除 children 字段
        new_node = {key: value for key, value in node.items() if key != 'children'}
        flattened.append(new_node)
        # 递归处理子节点
        if 'children' in node:
            flattened.extend(flatten_nodes(node['children']))
    return flattened

all_flattened_data = []

# 遍历 results 中的每个结果
for result in data.get('results', []):
    fields = result.get('fields')
    if isinstance(fields, dict) and 'response' in fields and 'data' in fields['response']:
        data_list = fields['response']['data']
        # 展平 data 中的节点
        flattened_data = flatten_nodes(data_list)
        all_flattened_data.extend(flattened_data)
    elif isinstance(fields, list):
        # 如果 fields 是列表，直接展平
        all_flattened_data.extend(flatten_nodes(fields))

# 将处理后的数据保存到新的 JSON 文件
with open('flattened_goushi.json', 'w', encoding='utf-8') as output_file:
    json.dump(all_flattened_data, output_file, ensure_ascii=False, indent=4)

print("所有 data 和 children 已展平并保存到 flattened_goushi.json 文件中。")