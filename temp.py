# 定义五行相生相克关系
generate_relations = {
    '木': '火',
    '火': '土',
    '土': '金',
    '金': '水',
    '水': '木'
}

overcome_relations = {
    '木': '土',
    '土': '水',
    '水': '火',
    '火': '金',
    '金': '木'
}

# 从字符串中识别五行元素
def extract_element_from_string(qi):
    for element in generate_relations.keys():
        if element in qi:
            return element
    return None  # 如果没有找到任何元素

# 判断主气与客气之间的关系
def determine_relation(main_qi, guest_qi):
    # 提取主气与客气的五行元素
    main_element = extract_element_from_string(main_qi)
    guest_element = extract_element_from_string(guest_qi)

    if not main_element or not guest_element:
        return "未知的主气或客气"

    # 相生或相同
    if main_element == guest_element or generate_relations[guest_element] == main_element:
        return '相得'
    # 相克
    elif overcome_relations[main_element] == guest_element:
        return '不相得逆'
    elif overcome_relations[guest_element] == main_element:
        return '不相得顺'

    return '不相得'


# 示例使用
main_qi = '少阳相火'
guest_qi = '少阴君火'
relation = determine_relation(main_qi, guest_qi)
print(f"主气'{main_qi}'与客气'{guest_qi}'之间的关系是：{relation}")
