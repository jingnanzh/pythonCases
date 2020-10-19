'''
    作者：Jing
    date：2020-08-15
    功能：计算第几天，需要分辨是否闰年
          使用字典 dictionary
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

    #dictionary：
    month_day_dictionary = {1:31,
                            2:28,
                            3:31,
                            4:30,
                            5:31,
                            6:30,
                            7:31,
                            8:31,
                            9:30,
                            10:31,
                            11:30,
                            12:31
    }

    days = 0
    days += day
    for i in range(1,month):
        days += month_day_dictionary[i]

    if is_leap_year(year) and month >2:
        days+=1

    print('今天是{}年的第{}天'.format(year,days))

if __name__=='__main__':
    main()