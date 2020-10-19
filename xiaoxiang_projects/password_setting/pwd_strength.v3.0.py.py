'''
    作者：    jing
    date：   2020- 80- 16
    version：1.0
    function:determine if a pwd is strong
    version: 1.1
    function:limit try time
    version: 3.0
    function:保存密码和强度值到文件中,加上读取文件, 定义一个class
'''
class PasswordTool:
    '''
        密码工具类
    '''
    def __init__(self, password):
        # 类的属性：
        self.password = password
        self.strength_level = 0
    # 类的方法：
    def process_password(self):
        # 长度大于8
        if len(self.password) > 8:
            self.strength_level += 1
        else:
            print('password must longer than 8 digits')

        # 包含数字：
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('password must contain number')

        # 包含字母：
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('password must contain letter')

    def check_number_exist(self):
        '''
            判断是否含有数字,如果有返回true,退出函数
        '''
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        '''
            判断是否含有字符,如果有返回true,退出函数
        '''
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

class FileTool:
    '''
        文件工具类
    '''
    def __init__(self,filepath):
        self.filepath = filepath
    def write_to_file(self, line):
        f = open(self.filepath,'a') #append
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath,'r') #read
        lines = f.readlines()
        f.close()
        return lines



def main():
    '''
        主函数 
    '''

    try_time = 5
    file_path = 'password.txt'
    # 文件工具实例化：
    file_tool = FileTool(file_path)

    while try_time > 0:

        password = input("please type in the password: ")
        # 实例化对象
        # 封装encapsule：
        password_tool = PasswordTool(password)
        password_tool.process_password()

        # # 写文件：
        # f = open('password.txt', 'a')
        # f.write('password is: {}, strength is {}\n'.
        #         format(password, password_tool.strength_level))
        # f.close()

        # 使用文件工具写文件：
        line = 'password is: {}, strength is {}\n'.format(password, password_tool.strength_level)
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('password is ok')
            # 密码合格，跳出程序
            break
        else:
            print('password is not strong')
            # 密码不合格，尝试次数减一
            try_time -= 1

        print()

    if try_time <= 0:
        print('尝试过多，设置密码失败')
    #读操作
    lines = file_tool.read_from_file()
    print(lines)

if __name__ == '__main__':
    main()
