'''
    作者：    jing
    date：   2020- 80- 16
    version：1.0
    function:determine if a pwd is strong
    version: 1.1
    function:limit try time
'''
def check_number_exist(password):
    '''
        判断是否含有数字,如果有返回true,退出函数
    '''

    has_number =  False

    for c in password:
        if c.isnumeric():
            has_number = True
            break
        return has_number

def check_letter_exist(password):
    '''
        判断是否含有字符,如果有返回true,退出函数
    '''
    has_letter = False
    for c in password:
        if c.isalpha():
            has_letter = True
            break
    return has_letter

def main():
    '''
        主函数 
    '''

    try_time = 5
    while try_time > 0:

        password = input("please type in the password: ")

        # 密码强度变量
        strength_level = 1

        # 长度大于8
        if len(password) > 8:
            strength_level += 1
        else:
            print('password must longer than 8 digits')

        # 包含数字：
        if check_number_exist(password):
            strength_level += 1
        else:
            print('password must contain number')

        # 包含字母：
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('password must contain letter')

        if strength_level == 3:
            print('password is ok')
            # 密码合格，跳出程序
            break
        else:
            print('password is not strong')
            # 密码不合格，尝试次数减一
            try_time -= 1

        print()

        if try_time <= 0:
            print('尝试过多')




if __name__ == '__main__':
    main()
