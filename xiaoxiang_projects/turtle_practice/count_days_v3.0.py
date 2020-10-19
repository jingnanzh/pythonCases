'''
    作者：Jing
    date：2020-08-15
    功能：计算第几天，需要分辨是否闰年
          使用集合set
'''
from datetime import datetime

def is_leap_year(year):
    '''
        判断是否闰年，是返回True，不是返回False
    '''
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    input_date_str = input('请输入日期（yyyy/mm/dd): ')
    input_date =  datetime.strptime(input_date_str,'%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    #30天的月份集合：
    _30_day_month_set = {4,6,9,11}
    _31_day_month_set = {1,3,5,7,8,10,12}

    days = 0
    days += day
    for i in range(1,month):
        if i in _30_day_month_set:
            days +=30
        elif i in _31_day_month_set:
            days +=31
        else:
            if is_leap_year(year):
                days+=29
            else:
                days +=28

    print('今天是{}年的第{}天'.format(year,days))

if __name__=='__main__':
    main()