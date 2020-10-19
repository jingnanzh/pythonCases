'''
    作者：    jing
    date：   2020- 80- 16
    version：1.0
    function:determine if a pwd is strong
    version: 1.1
    function:limit try time
    version: 2.0
    function:保存密码和强度值到文件中,加上读取文件
    read(): 整个文档是一个字符串
    readline()：下一行
    readlines():全部内容是一个列表
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

    # try_time = 5
    # while try_time > 0:
    #
    #     password = input("please type in the password: ")
    #
    #     # 密码强度变量
    #     strength_level = 0
    #
    #     # 长度大于8
    #     if len(password) > 8:
    #         strength_level += 1
    #     else:
    #         print('password must longer than 8 digits')
    #
    #     # 包含数字：
    #     if check_number_exist(password):
    #         strength_level += 1
    #     else:
    #         print('password must contain number')
    #
    #     # 包含字母：
    #     if check_letter_exist(password):
    #         strength_level += 1
    #     else:
    #         print('password must contain letter')
    #
    #     # 写文件：
    #     f = open('password.txt', 'a')
    #     f.write('password is: {}, strength is {}\n'.
    #             format(password, strength_level))
    #     f.close()

        # if strength_level == 3:
        #     print('password is ok')
        #     # 密码合格，跳出程序
        #     break
        # else:
        #     print('password is not strong')
        #     # 密码不合格，尝试次数减一
        #     try_time -= 1
    #     print()
    #
    # if try_time <= 0:
    #     print('尝试过多')

    # 读取文件：
    f = open('password.txt','r')
    # 1. read:
    # content = f.read()
    # print(content)
    # 2. readline:
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)
    # 3. readlines:
    # lines = f.readlines()
    # print(lines)
    # 4. 全部：
    # method 1:
    # for line in f:
    #     print(line)
    # method 2:
    for line in f.readlines():
        print('read: {}'.format(line))

    f.close()



if __name__ == '__main__':
    main()
