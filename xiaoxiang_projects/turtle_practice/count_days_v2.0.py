'''
    作者：Jing
    date：2020-08-15
    功能：计算第几天，需要分辨是否闰年
         用list
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

    #计算之前的月数的天数和当月天数
    days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        days_in_month_list[1]=29
    days = days_in_month_list[: month-1]
    sum_days = sum(days) + day
    print('今天是{}年的第{}天'.format(year,sum_days))

if __name__=='__main__':
    main()