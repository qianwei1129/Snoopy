from calculate_qi import get_qi, get_lichun_year
from calculate_yun import get_yun
from datetime import datetime
from calculate_relationship import determine_relation


def get_tian_gan(year, query_month, query_day):
    """
    用于获取对应年份的天干
    :param year: 年份
    :return: 年对应的天干
    """
    tian_gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

    lichun_month, lichun_day = get_lichun_year(year)

    lichun_date = datetime(year=year, month=lichun_month, day=lichun_day)
    query_date = datetime(year=year, month=query_month, day=query_day)

    if query_date < lichun_date:
        return tian_gan[(year - 4) % 10 - 1]
    else:
        return tian_gan[(year - 4) % 10]


def get_di_zhi(year, query_month, query_day):
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

    lichun_month, lichun_day = get_lichun_year(year)

    lichun_date = datetime(year=year, month=lichun_month, day=lichun_day)
    query_date = datetime(year=year, month=query_month, day=query_day)

    if query_date < lichun_date:
        return di_zhi[(year - 4) % 12 - 1]
    else:
        return di_zhi[(year - 4) % 12]


def get_sui_yun(tian_gan):
    """
    用于获取对应年份的岁运
    :param tian_gan: 年份对应的天干
    :return: 年份的岁运
    """
    yun_dict = {'甲': '土运太过', '乙': '金运不及', '丙': '水运太过', '丁': '木运不及', '戊': '火运太过',
                '己': '土运不及', '庚': '金运太过', '辛': '水运不及', '壬': '木运太过', '癸': '火运不及'}
    return yun_dict[tian_gan]


def get_yun_qi_tong_hua(tian_gan_di_zhi):
    """
    用于获取运气同化相关信息
    :param tian_gan_di_zhi: 年份对应的天干地支
    :return: 年份对应的运气同化信息
    """
    yun_qi_mapping = {
        '丁卯': '岁会', '庚午': '同天符', '辛未': '同岁会', '壬申': '同天符', '癸酉': '同岁会', '甲戌': '岁会同天符',
        '丙子': '岁会', '戊寅': '天符', '乙酉': '太一天符', '丙戌': '天符', '丁亥': '天符', '戊子': '天符',
        '己丑': '太一天符', '庚子': '同天符', '辛丑': '同岁会', '壬寅': '同天符', '癸卯': '同岁会', '甲辰': '岁会同天符',
        '乙卯': '天符', '丙辰': '天符', '丁巳': '天符', '戊午': '太一天符', '己未': '太一天符', '癸亥': '同岁会'
    }

    return yun_qi_mapping.get(tian_gan_di_zhi, '0')  # 如果没有特殊情况，则返回'无特殊运气同化'


def get_yun_qi_yi_hua(tian_gan_di_zhi):
    """
    用于获取运气异化相关信息
    :param tian_gan_di_zhi: 年份对应的天干地支
    :return: 年份对应的运气异化信息
    """
    yun_qi_mapping = {
        '甲子': '顺化', '乙丑': '顺化', '丙寅': '不和', '丁卯': '天刑', '戊辰': '天刑',
        '己巳': '天刑', '庚午': '天刑', '辛未': '天刑', '壬申': '小逆', '癸酉': '不和',
        '甲戌': '不和', '乙亥': '不和', '丙子': '不和', '丁丑': '不和', '己卯': '小逆',
        '庚辰': '小逆', '辛巳': '小逆', '壬午': '小逆', '癸未': '小逆', '甲申': '顺化',
        '辛卯': '顺化', '壬辰': '顺化', '癸巳': '顺化', '甲午': '顺化', '乙未': '顺化',
        '丙申': '不和', '丁酉': '天刑', '戊戌': '天刑', '己亥': '天刑', '庚子': '天刑',
        '辛丑': '天刑', '壬寅': '小逆', '癸卯': '不和', '甲辰': '不和', '乙巳': '不和',
        '丙午': '不和', '丁未': '不和', '己酉': '小逆', '庚戌': '小逆', '辛亥': '小逆',
        '壬子': '小逆', '癸丑': '小逆', '甲寅': '顺化', '辛酉': '顺化', '壬戌': '顺化', '癸亥': '顺化'
    }

    return yun_qi_mapping.get(tian_gan_di_zhi, '0')  # 如果没有特殊情况，则返回'无特殊运气异化'


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


def get_si_tian_zai_quan(si_tian_zhi_qi, zai_quan_zhi_qi):
    elements = ['木', '火', '土', '金', '水']

    for element in elements:
        if element in si_tian_zhi_qi:
            temp_1 = element
            break

    for element in elements:
        if element in zai_quan_zhi_qi:
            temp_2 = element
            break

    return temp_1 + temp_2


def get_yun_qi_xiang_he(gan_zhi):
    # 定义天干地支与其对应结果的字典
    gan_zhi_dict = {
        '甲子': '强土火燥', '乙丑': '弱金湿寒', '丙寅': '强水火风', '丁卯': '弱木燥火',
        '戊辰': '强火寒湿', '己巳': '弱土风火', '庚午': '强金火燥', '辛未': '弱水湿寒',
        '壬申': '强木火风', '癸酉': '弱火燥火', '甲戌': '强土寒湿', '乙亥': '弱金风火',
        '丙子': '强水火燥', '丁丑': '弱木湿寒', '戊寅': '强火火风', '己卯': '弱土燥火',
        '庚辰': '强金寒湿', '辛巳': '弱水风火', '壬午': '强木火燥', '癸未': '弱火湿寒',
        '甲申': '强土火风', '乙酉': '弱金燥火', '丙戌': '强水寒湿', '丁亥': '弱木风火',
        '戊子': '强火火燥', '己丑': '弱土湿寒', '庚寅': '强金火风', '辛卯': '弱水燥火',
        '壬辰': '强木寒湿', '癸巳': '弱火风火', '甲午': '强土火燥', '乙未': '弱金湿寒',
        '丙申': '强水火风', '丁酉': '弱木燥火', '戊戌': '强火寒湿', '己亥': '弱土风火',
        '庚子': '强金火燥', '辛丑': '弱水湿寒', '壬寅': '强木火风', '癸卯': '弱火燥火',
        '甲辰': '强土寒湿', '乙巳': '弱金风火', '丙午': '强水火燥', '丁未': '弱木湿寒',
        '戊申': '强火火风', '己酉': '弱土燥火', '庚戌': '强金寒湿', '辛亥': '弱水风火',
        '壬子': '强木火燥', '癸丑': '弱火湿寒', '甲寅': '强土火风', '乙卯': '弱金燥火',
        '丙辰': '强水寒湿', '丁巳': '弱木风火', '戊午': '强火火燥', '己未': '弱土湿寒',
        '庚申': '强金火风', '辛酉': '弱水燥火', '壬戌': '强木寒湿', '癸亥': '弱火风火'
    }

    result = gan_zhi_dict.get(gan_zhi, "未知组合")
    return result


def calculate(year, month, day):

    tian_gan = get_tian_gan(year, month, day)

    main_qi, guest_qi, ji_zhi_qi, si_tian_zhi_qi, zai_quan_zhi_qi = \
        get_qi(year, month, day)
    main_yun, guest_yun, ji_zhi_yun = \
        get_yun(year, month, day, sui_yun=get_sui_yun(tian_gan))

    return(main_qi, guest_qi, ji_zhi_qi,
           main_yun, guest_yun, ji_zhi_yun,
           si_tian_zhi_qi, zai_quan_zhi_qi)


if __name__ == '__main__':
    print(calculate(2023, 4, 3))


