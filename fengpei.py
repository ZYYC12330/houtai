



def allocate_staff(table_name: str, date: str) -> str:
    """
    分配人员函数
    :param table_name: 分配表名称
    :param date: 分配日期 (YYYY-MM-DD)
    :return: 分配的人员姓名
    """
    # 1. 获取分配记录
    record = db.query("SELECT * FROM AllocationRecords WHERE table_name = %s AND allocation_date = %s", 
                     (table_name, date))

    if not record:
        raise ValueError(f"未找到{table_name}在{date}的分配记录")

    staff_list = json.loads(record['staff_list'])
    current_index = record['current_index']

    # 2. 轮询分配
    staff = staff_list[current_index]

    # 3. 更新索引 (循环)
    new_index = (current_index + 1) % len(staff_list)

    # 4. 更新数据库
    db.execute("UPDATE AllocationRecords SET current_index = %s WHERE id = %s", 
              (new_index, record['id']))

    return staff


# def allocate_staff(table_name: str, date: str) -> str:
#     """
#     分配人员函数
#     :param table_name: 分配表名称
#     :param date: 分配日期 (YYYY-MM-DD)
#     :return: 分配的人员姓名
#     """
#     # 1. 获取分配记录
#     record = db.query("SELECT * FROM allocation_records WHERE table_name = %s AND allocation_date = %s", 
#                      (table_name, date))

#     if not record:
#         raise ValueError(f"未找到{table_name}在{date}的分配记录")

#     staff_list = json.loads(record['staff_list'])
#     current_index = record['current_index']

#     # 2. 轮询分配
#     staff = staff_list[current_index]

#     # 3. 更新索引 (循环)
#     new_index = (current_index + 1) % len(staff_list)

#     # 4. 更新数据库
#     db.execute("UPDATE allocation_records SET current_index = %s WHERE id = %s", 
#               (new_index, record['id']))

#     return staff


# # 分配人员
# assigned_person = allocate_staff("大学市区考研分配表", "2025-07-01")
# print(f"分配结果: {assigned_person}")

# # 连续分配5次
# for _ in range(5):
#     person = allocate_staff("大学拼多多考研分配表", "2025-07-02")
#     print(f"第{_+1}次分配: {person}")