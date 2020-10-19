'''
作者：jing
日期：2020-08-12
功能：绘制多个五角星，使用迭代函数
'''
import turtle

def draw_branch(branch_length):
    '''
    # 绘制一个分支
    '''
    if branch_length > 5:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        print('向前 ', branch_length)
        turtle.right(20)
        print('右转 20')
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        turtle.right(20)
        print('右转 20')
        turtle.backward(branch_length)
        print('向后 ', branch_length)



def main():
    '''
    主函数
    '''

    turtle.left(90)
    # 向下移动画笔
    turtle.penup()
    turtle.backward(250)
    turtle.pendown()
    turtle.pencolor('blue')
    draw_branch(180)
    turtle.exitonclick()


if __name__=='__main__':
    main()