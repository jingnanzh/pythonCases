# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=71

'''
 Day 3 批量处理文件名称（下）
 筛选PDF和doc文档，将结果写入文件。
'''

import os
import pandas

path=r'C:\Users\Maggie\Desktop\Udemy-desktop\xiaoxiangxueyuan'
name=os.listdir(path)
print(name)

result = []

for i in name:
    if i.endswith('.docx') or i.endswith((".pdf")):
        result.append(i)

result_table = pandas.DataFrame(result)

#将获取的文档名称储存到计算器硬盘中。utf-8-sig编码可以避免名称有中文时存在乱码
result_table.to_csv('pdfDocName.csv',encoding = 'utf-8-sig')