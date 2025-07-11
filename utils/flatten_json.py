import json
from typing import List, Dict, Union

def flatten_json_file(input_path: str, output_path: str) -> None:
    """
    从 input_path 读取嵌套 JSON 数据，展平所有 children 节点，并将结果写入 output_path。
    """
    
    # 读取 JSON 文件
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 定义递归函数展平 children
    def flatten_nodes(nodes: List[Dict]) -> List[Dict]:
        flattened = []
        for node in nodes:
            new_node = {k: v for k, v in node.items() if k != 'children'}
            flattened.append(new_node)
            if 'children' in node and isinstance(node['children'], list):
                flattened.extend(flatten_nodes(node['children']))
        return flattened

    all_flattened_data = []

    # 处理 results 中每个字段
    for result in data.get('results', []):
        fields = result.get('fields')
        if isinstance(fields, dict) and 'response' in fields and 'data' in fields['response']:
            data_list = fields['response']['data']
            all_flattened_data.extend(flatten_nodes(data_list))
        elif isinstance(fields, list):
            all_flattened_data.extend(flatten_nodes(fields))

    # 写入展平后的 JSON 文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(all_flattened_data, output_file, ensure_ascii=False, indent=4)

    print()
    print(f"\n所有 data 和 children 键值对已展平并保存到 {output_path}。")

# flatten_json_file('output.json', './utils/flattened_data.json')
