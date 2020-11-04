# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=71

'''
 按模版批量生成Word文件（上）
 筛快速合并Excel表格文件。
'''

import os
import pandas as pd

path = 'C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/Python认知打卡课课程资料包/资料代码整理/四五关代码/第四关代码/名单表格/'
file_names = os.listdir(path)

# this is an empty data frame
file_merge= pd.DataFrame()

for name in file_names:
    df=pd.read_excel(path+name)
    file_merge=file_merge.append(df)

file_merge.to_excel(path+'file_merge.xlsx',index = None)