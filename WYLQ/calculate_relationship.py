def extract_element_from_string(qi):
    generate_relations = {
        '木': '火',
        '火': '土',
        '土': '金',
        '金': '水',
        '水': '木'
    }

    for element in generate_relations.keys():
        if element in qi:
            return element
    return None


def determine_relation(main_qi, guest_qi):
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

    main_element = extract_element_from_string(main_qi)
    guest_element = extract_element_from_string(guest_qi)

    if not main_element or not guest_element:
        return "未知的主气或客气"

    if (main_element == guest_element or generate_relations[guest_element] == main_element or generate_relations[main_element] == guest_element) \
            and ('君火' in main_qi and '相火' in guest_qi):
        return '相得', '逆'

    elif (main_element == guest_element or generate_relations[guest_element] == main_element or generate_relations[main_element] == guest_element) and \
            ('相火' in main_qi and '君火' in guest_qi):
        return '相得', '顺'

    elif (main_element == guest_element or generate_relations[guest_element] == main_element or generate_relations[main_element] == guest_element) and \
            ('相火' not in main_qi or '君火' not in guest_qi):
        return '相得', None

    elif overcome_relations[main_element] == guest_element:
        return '不相得', '逆'

    elif overcome_relations[guest_element] == main_element:
        return '不相得', '顺'


if __name__ == '__main__':
    main_qi = '厥阴枫木'
    guest_qi = '少阳相火'
    relation = determine_relation(main_qi, guest_qi)
    print(f"主气'{main_qi}'与客气'{guest_qi}'之间的关系是：{relation}")
