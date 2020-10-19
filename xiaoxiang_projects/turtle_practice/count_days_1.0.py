'''
    作者：Jing
    date：2020-08-15
    功能：计算第几天，需要分辨是否闰年
'''
from datetime import datetime
def main():
    input_date_str = input('请输入日期（yyyy/mm/dd): ')
    input_date =  datetime.strptime(input_date_str,'%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    #计算之前的月数的天数和当月天数
    days_in_month_tup = (31,28,31,30,31,30,31,31,30,31,30,31)
    days = days_in_month_tup[: month-1]
    sum_days = sum(days) + day
    print(sum_days)

    # 判断闰年,月数要大于2：
    if (year % 400 == 0) or ((year %4 == 0) and (year % 100 !=0)):
        if month >2:
            sum_days +=1
    print('今天是第{}天'.format(sum_days))

if __name__=='__main__':
    main()