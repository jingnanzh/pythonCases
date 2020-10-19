'''
    作者：jing
    日期；2020-08-13

'''
def main():
    '''
        主函数
    '''
    y_or_n = input('是否退出程序(y/n)： ')
    while y_or_n =='n':
        # input 得到字符串
        # gender = input('性别: ')
        # weight = float(input('体重(kg): '))
        # height = float(input('height(cm): '))
        # age = int(input('age: '))
        print('please give information, 用空格分隔:')
        input_str = input('gender, weight, height, age ')
        str_list = input_str.split(' ') #以空格分隔字符串

        try:
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age =  int(str_list[3])
            if gender == '男':
                bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
            elif gender == '女':
                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
            else:
                bmr = -1

            if bmr != -1:
                print('gender: {}, weight: {}, height: {}, age:{}'.format(gender, weight, height, age))
                print('您的基础代谢率{}（大卡）'.format(bmr))
            else:
                print('暂不支持该性别')
        except ValueError:
            print('请输入正确信息')
        except:
            print('程序异常')




        print() #默认这个是一个空行
        y_or_n = input('是否退出程序(y/n)： ')

if __name__=="__main__":
    main()