'''
    作者：jing
    日期；2020-08-13

'''
def main():
    '''
        主函数
    '''
    gender = '男gg'
    weight = 70
    height = 175
    age = 25

    if gender == '男':
        bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
    elif gender == '女':
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1

    if bmr != -1:
        print('基础代谢率（大卡）', bmr)
    else:
        print('暂不支持该性别')

if __name__=="__main__":
    main()