import json

# 示例数据，可以替换为你的实际json
json_data = [
    {
        "ids": "032e060a2d174b34b8936d0f89525034",
        "names": "上海浦东八佰伴",
        "numbers": "pdbbb"
    },
    {
        "ids": "04ad3eeba6934593a897ecafb710de3f",
        "names": "飞洲国际校区",
        "numbers": "fzgj"
    },
    {
        "ids": "13a6e2c0248b42d697b6323ea08f8b4b",
        "names": "上海交大附中",
        "numbers": "jdfz"
    }
]

def find_ids_by_name(data, name):
    result = []
    def search(obj):
        if isinstance(obj, dict):
            if obj.get("names") == name and "ids" in obj:
                result.append(obj["ids"])
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    search(v)
        elif isinstance(obj, list):
            for item in obj:
                search(item)
    search(data)
    return result

if __name__ == "__main__":
    name = input("请输入要查找的name: ")
    ids = find_ids_by_name(json_data, name)
    if ids:
        print(f"name为{name}的ids有: {ids}")
    else:
        print(f"未找到name为{name}的ids")
