import ephem

def get_dahan_date(year):
    """
    获取对应每年大寒的时间，并格式化为年月日的形式
    :param year: 年份
    :return: 返回立春的日期，格式为"YYYY-MM-DD"
    """
    start_date = f"{year}/2/3"
    spring_equinox = ephem.next_vernal_equinox(start_date)
    lichun_date = ephem.Date(spring_equinox - 45 - 15)
    formatted_lichun_date_year = lichun_date.datetime().strftime('%Y')
    formatted_lichun_date_month = lichun_date.datetime().strftime('%m')
    formatted_lichun_date_date = lichun_date.datetime().strftime('%d')

    return formatted_lichun_date_month, formatted_lichun_date_date

# 示例用法
year = 2024
dahan_date = get_dahan_date(year)
print(f"{year}年大寒的日期是：{dahan_date}")
