from datetime import datetime, timedelta
from calculate_qi import get_lichun_year, get_dahan_year


def calculate_main_yun(sui_yun):
    elements_sequence = ['木', '火', '土', '金', '水']
    yun_mapping = {'木': '角', '火': '徵', '土': '宫', '金': '商', '水': '羽'}

    element = sui_yun[0]
    status = '太' if '太过' in sui_yun else '少'

    start_index = elements_sequence.index(element)
    main_yun = [status + yun_mapping[elements_sequence[start_index]]]

    # 从岁运元素开始，按照太少相生原则计算其他运
    for i in range(1, (elements_sequence.index("水") - elements_sequence.index(element) + 1)):
        next_status = '少' if main_yun[-1].startswith('太') else '太'
        next_element_index = (start_index + i) % 5
        next_element = elements_sequence[next_element_index]
        main_yun.append(next_status + yun_mapping[next_element])

    for i in range(0, 5 - len(main_yun)):
        next_status = '少' if main_yun[0].startswith('太') else '太'
        next_element_index = start_index - (i + 1)
        next_element = next_status + yun_mapping[elements_sequence[next_element_index]]
        main_yun.insert(0, next_element)

    return main_yun


def calculate_guest_yun(sui_yun):
    """
    计算客运
    :param sui_yun: 输入岁运
    :return: 返回客运
    """
    elements = ['木', '火', '土', '金', '水']
    yun_mapping = {'木': '角', '火': '徵', '土': '宫', '金': '商', '水': '羽'}

    element, status = sui_yun[0], sui_yun[2:4]
    strength = '太' if status == '太过' else '少'
    start_index = elements.index(element)

    guest_yun = [strength + yun_mapping[element]]
    for i in range(1, (elements.index('水') - elements.index(element) + 1)):
        next_index = (start_index + i) % 5
        next_strength = '太' if guest_yun[-1].startswith('少') else '少'
        guest_yun.append(next_strength + yun_mapping[elements[next_index]])

    for i in range((elements.index('水') - elements.index(element) + 1), 5):
        if i == 4:
            next_index = (start_index + i) % 5
            next_strength = '太' if guest_yun[0].startswith('少') else '少'
            guest_yun.append(next_strength + yun_mapping[elements[next_index]])
        else:
            if len(guest_yun) == 1:
                next_strength = '少' if guest_yun[0].startswith('少') else '太'
                guest_yun.append(next_strength + yun_mapping[elements[0]])
            else:
                next_index = (start_index + i) % 5
                next_strength = '太' if guest_yun[+1].startswith('少') else '少'
                guest_yun.append(next_strength + yun_mapping[elements[next_index]])

    return guest_yun


def calculate_yun(year, lichun_month, lichun_day, query_month, query_day, sui_yun):
    lichun_date = datetime(year=year, month=lichun_month, day=lichun_day)
    query_date = datetime(year=year, month=query_month, day=query_day)

    main_yun_sequence = calculate_main_yun(sui_yun)
    guest_yun_sequence = calculate_guest_yun(sui_yun)

    step_yun_dates = [lichun_date + timedelta(days=i * 60) for i in range(5)]

    for i, step_date in enumerate(step_yun_dates):
        if query_date <= step_date:
            if i == 0:
                return main_yun_sequence[-1], guest_yun_sequence[-1], 5
            else:
                return main_yun_sequence[i - 1], guest_yun_sequence[i - 1], i

    return main_yun_sequence[-1], guest_yun_sequence[-1], 5


def get_yun(year, month, day, sui_yun, start = "lichun"):
    if(start == "lichun"):
        lichun_month, lichun_day = get_lichun_year(year)
    else:
        lichun_month, lichun_day = get_dahan_year(year)
    lichun_month = int(lichun_month)
    lichun_day = int(lichun_day)

    main_yun, guest_yun, ji_zhi_yun = calculate_yun(year, lichun_month, lichun_day, month, day, sui_yun)
    return(main_yun, guest_yun, ji_zhi_yun)


if __name__ == '__main__':

    year = 2024
    month = 1
    day = 19

    sui_yun = "火运不及"

    print(get_yun(year, month, day, sui_yun, start="lichun"))