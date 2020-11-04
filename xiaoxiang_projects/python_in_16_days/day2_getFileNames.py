# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=71

'''
 Day 2 批量处理文件名称（上）
'''

import os
path=r'C:\Users\Maggie\Desktop\Udemy-desktop\xiaoxiangxueyuan'
name=os.listdir(path)
for i in name:
    print(i)