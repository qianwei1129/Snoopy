import ephem
import sxtwl
from datetime import datetime, timedelta


def get_dahan_year(year):
    """
    获取对应每年大寒的时间，并格式化为年月日的形式
    :param year: 年份
    :return: 返回大寒的日期，格式为"YYYY-MM-DD"
    """
    start_date = f"{year}/2/3"
    spring_equinox = ephem.next_vernal_equinox(start_date)
    lichun_date = ephem.Date(spring_equinox - 45 - 15)

    formatted_lichun_date_year = int(lichun_date.datetime().strftime('%Y'))
    formatted_lichun_date_month = int(lichun_date.datetime().strftime('%m'))
    formatted_lichun_date_date = int(lichun_date.datetime().strftime('%d'))

    day = sxtwl.fromSolar(formatted_lichun_date_year, formatted_lichun_date_month, formatted_lichun_date_date)
    if day.hasJieQi():
        return formatted_lichun_date_month, formatted_lichun_date_date
    else:
        lichun_date = ephem.Date(spring_equinox - 45 - 14)
        formatted_lichun_date_year = int(lichun_date.datetime().strftime('%Y'))
        formatted_lichun_date_month = int(lichun_date.datetime().strftime('%m'))
        formatted_lichun_date_date = int(lichun_date.datetime().strftime('%d'))
        day = sxtwl.fromSolar(formatted_lichun_date_year, formatted_lichun_date_month, formatted_lichun_date_date)
        if day.hasJieQi():
            return formatted_lichun_date_month, formatted_lichun_date_date
        else:
            lichun_date = ephem.Date(spring_equinox - 45 - 16)
            formatted_lichun_date_year = int(lichun_date.datetime().strftime('%Y'))
            formatted_lichun_date_month = int(lichun_date.datetime().strftime('%m'))
            formatted_lichun_date_date = int(lichun_date.datetime().strftime('%d'))
            day = sxtwl.fromSolar(formatted_lichun_date_year, formatted_lichun_date_month, formatted_lichun_date_date)
            return formatted_lichun_date_month, formatted_lichun_date_date


def get_lichun_year(year):
    """
    获取对应每年立春的时间，并格式化为年月日的形式
    :param year: 年份
    :return: 返回立春的日期，格式为"YYYY-MM-DD"
    """
    start_date = f"{year}/2/3"
    spring_equinox = ephem.next_vernal_equinox(start_date)
    lichun_date = ephem.Date(spring_equinox - 45)
    formatted_lichun_date_year = int(lichun_date.datetime().strftime('%Y'))
    formatted_lichun_date_month = int(lichun_date.datetime().strftime('%m'))
    formatted_lichun_date_date = int(lichun_date.datetime().strftime('%d'))


    day = sxtwl.fromSolar(formatted_lichun_date_year, formatted_lichun_date_month, formatted_lichun_date_date)
    if day.hasJieQi():
        return formatted_lichun_date_month, formatted_lichun_date_date
    else:
        lichun_date = ephem.Date(spring_equinox - 45 - 1)
        formatted_lichun_date_year = int(lichun_date.datetime().strftime('%Y'))
        formatted_lichun_date_month = int(lichun_date.datetime().strftime('%m'))
        formatted_lichun_date_date = int(lichun_date.datetime().strftime('%d'))
        day = sxtwl.fromSolar(formatted_lichun_date_year, formatted_lichun_date_month, formatted_lichun_date_date)
        if day.hasJieQi():
            return formatted_lichun_date_month, formatted_lichun_date_date
        else:
            lichun_date = ephem.Date(spring_equinox - 45 + 1)
            formatted_lichun_date_year = int(lichun_date.datetime().strftime('%Y'))
            formatted_lichun_date_month = int(lichun_date.datetime().strftime('%m'))
            formatted_lichun_date_date = int(lichun_date.datetime().strftime('%d'))
            day = sxtwl.fromSolar(formatted_lichun_date_year, formatted_lichun_date_month, formatted_lichun_date_date)
            return formatted_lichun_date_month, formatted_lichun_date_date


def get_main_qi_lichun(lichun_month, lichun_day, query_month, query_day):
    """
    用于计算主气
    :param lichun_month: 立春对应的月
    :param lichun_day: 立春对应的天
    :param query_month: 研究的月
    :param query_day: 研究的天
    :return: 主气
    """
    main_qi = ['厥阴风木', '少阴君火', '少阳相火', '太阴湿土', '阳明燥金', '太阳寒水']

    lichun_date = datetime(year=datetime.now().year, month=lichun_month, day=lichun_day)

    query_date = datetime(year=datetime.now().year, month=query_month, day=query_day)

    step_qi_dates = [lichun_date + timedelta(days=i * 60) for i in range(6)]

    for i, step_date in enumerate(step_qi_dates):
        if query_date < step_date:
            return main_qi[i - 1] if i > 0 else main_qi[-1]

    return main_qi[-1]


def get_main_qi_dahan(lichun_month, lichun_day, query_month, query_day):
    """
    用于计算主气
    :param lichun_month: 立春对应的月
    :param lichun_day: 立春对应的天
    :param query_month: 研究的月
    :param query_day: 研究的天
    :return: 主气
    """
    main_qi = ['厥阴风木', '少阴君火', '少阳相火', '太阴湿土', '阳明燥金', '太阳寒水']

    lichun_date = datetime(year=datetime.now().year, month=lichun_month, day=lichun_day)

    query_date = datetime(year=datetime.now().year, month=query_month, day=query_day)

    step_qi_dates = [lichun_date + timedelta(days=i * 60) for i in range(6)]

    for i, step_date in enumerate(step_qi_dates):
        if query_date < step_date:
            return main_qi[i - 2] if i > 0 else main_qi[-1]

    return main_qi[-1]


def calculate_guest_qi(year, si_tian_zhi_qi, zai_quan_zhi_qi):
    """
    用于获取全年的客气分布
    :param year: 年份
    :return: 全年客气分布
    """
    base_guest_qi_sequence = ['厥阴风木', '少阴君火', '太阴湿土', '少阳相火', '阳明燥金', '太阳寒水']

    si_tian_index = base_guest_qi_sequence.index(si_tian_zhi_qi)
    zai_quan_index = base_guest_qi_sequence.index(zai_quan_zhi_qi)

    guest_qi = base_guest_qi_sequence[:]
    guest_qi[2] = base_guest_qi_sequence[si_tian_index]
    guest_qi[5] = base_guest_qi_sequence[zai_quan_index]

    remaining_qi = [qi for i, qi in enumerate(base_guest_qi_sequence) if i not in [si_tian_index, zai_quan_index]]

    guest_qi[1] = base_guest_qi_sequence[si_tian_index - 1]
    guest_qi[0] = base_guest_qi_sequence[si_tian_index - 2]
    guest_qi[3] = base_guest_qi_sequence[zai_quan_index - 2]
    guest_qi[4] = base_guest_qi_sequence[zai_quan_index - 1]

    return guest_qi


def get_guest_qi(year, lichun_month, lichun_day, query_month, query_day, si_tian_zhi_qi, zai_quan_zhi_qi):
    """
    用于计算给定日期的客气
    :param year: 年份
    :param lichun_month: 立春对应的月
    :param lichun_day: 立春对应的天
    :param query_month: 查询的月
    :param query_day: 查询的天
    :return: 客气
    """
    guest_qi_sequence = calculate_guest_qi(year, si_tian_zhi_qi, zai_quan_zhi_qi)

    lichun_date = datetime(year=year, month=lichun_month, day=lichun_day)
    query_date = datetime(year=year, month=query_month, day=query_day)

    step_qi_dates = [lichun_date + timedelta(days=i * 60) for i in range(6)]

    for i, step_date in enumerate(step_qi_dates):
        if query_date <= step_date:
            if i == 0:
                return guest_qi_sequence[-1], 6
            else:
                return guest_qi_sequence[i - 1], i

    return guest_qi_sequence[-1], 6


def get_di_zhi(year, query_month, query_day, lichun_month, lichun_day):
    """
    用于获取对应年份的地支
    :param lichun_day:
    :param lichun_month:
    :param query_day:
    :param query_month:
    :param year: 年份
    :return: 年对应的地支
    """
    di_zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

    lichun_date = datetime(year=year, month=lichun_month, day=lichun_day)
    query_date = datetime(year=year, month=query_month, day=query_day)

    if query_date < lichun_date:
        return di_zhi[(year - 4) % 12 - 1]
    else:
        return di_zhi[(year - 4) % 12]


def get_si_tian_zhi_qi(di_zhi):
    """
    用于获取司天之气的信息
    :param di_zhi: 地支
    :return: 年份对应的司天之气
    """
    si_tian_mapping = {
        '子': '少阴君火', '丑': '太阴湿土', '寅': '少阳相火', '卯': '阳明燥金', '辰': '太阳寒水', '巳': '厥阴风木',
        '午': '少阴君火', '未': '太阴湿土', '申': '少阳相火', '酉': '阳明燥金', '戌': '太阳寒水', '亥': '厥阴风木'
    }
    return si_tian_mapping[di_zhi]


def get_zai_quan_zhi_qi(di_zhi):
    """
    用于获取在泉之气的新信息
    :param di_zhi: 地支
    :return: 年份对应的在泉之气
    """
    zai_quan_mapping = {
        '子': '阳明燥金', '丑': '太阳寒水', '寅': '厥阴风木', '卯': '少阴君火', '辰': '太阴湿土', '巳': '少阳相火',
        '午': '阳明燥金', '未': '太阳寒水', '申': '厥阴风木', '酉': '少阴君火', '戌': '太阴湿土', '亥': '少阳相火'
    }
    return zai_quan_mapping[di_zhi]


def get_qi(year, month, day, start = "lichun"):
    if(start == "lichun"):
        lichun_month, lichun_day = get_lichun_year(year)
    else:
        lichun_month, lichun_day = get_dahan_year(year)

    di_zhi = get_di_zhi(year, month, day, lichun_month, lichun_day)

    si_tian_zhi_qi = get_si_tian_zhi_qi(di_zhi)
    zai_quan_zhi_qi = get_zai_quan_zhi_qi(di_zhi)

    main_qi = get_main_qi_lichun(lichun_month, lichun_day, month, day)
    guest_qi = get_guest_qi(year, lichun_month, lichun_day, month, day, si_tian_zhi_qi, zai_quan_zhi_qi)

    return(main_qi, guest_qi[0], guest_qi[1], si_tian_zhi_qi, zai_quan_zhi_qi)


if __name__ == '__main__':
    year = 2023
    month = 4
    day = 3

    print(get_qi(year, month, day, start="lichun"))
