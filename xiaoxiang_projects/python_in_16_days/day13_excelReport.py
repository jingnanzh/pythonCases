# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=17

'''
    需要分别按照部门汇总合并周报表格，以做留存整理。
    统计每人月度完成情况，部门整体完成率，以及公司本月目标完成情况
'''

#在对周报进行操作前，我们想先查看一下共有哪些表格。定义一个函数，实现的功能是扫描指定路径下的表格文件。
import os
'''
获取文件夹的路径,该路径下的所有文件夹，以及所有文件
root    #当前目录路径  
dirs    #当前路径下所有子目录  
files   #当前路径下所有非目录子文件 
'''
def get_allfile_msg(file_dir):
    for _, _, files in os.walk(file_dir):
        return [file for file in files if file.endswith('.xls') or file.endswith('.xlsx')]

files = get_allfile_msg(r'C:\Users\Maggie\Desktop\Udemy-desktop\xiaoxiangxueyuan\Python认知打卡课课程资料包\资料代码整理\办公自动化\批量处理周报\excel\input')
print(files)

# pandas模块。查看一下财务部门6月7日周报的前五行内容。
import pandas as pd
# df = pd.read_excel(r'C:\Users\Maggie\Desktop\Udemy-desktop\xiaoxiangxueyuan\Python认知打卡课课程资料包\资料代码整理\办公自动化\批量处理周报\excel\input'+'\\2020-6-7财务部周报.xlsx')
# print(df.head())

df_all = pd.DataFrame()
# print(df_all) #空的列表
for file in files:
    df_all = pd.concat([df_all, pd.read_excel(r'C:\Users\Maggie\Desktop\Udemy-desktop\xiaoxiangxueyuan\Python认知打卡课课程资料包\资料代码整理\办公自动化\批量处理周报\excel\input'+'\\'+ file)])
# print(df_all) #新列表是所有文件的前五行

# 下面来查看一下这张大表中都包含哪些日期和部门：
# print(df_all['日期'].value_counts().index)
# print(df_all['部门'].value_counts().index)

df_sort = df_all.sort_values(by=['部门', '责任人']).reset_index(drop=True)
# print(df_sort)

# 将以上结果生成新的表格，命名为“个人任务完成情况”。
df_sort.to_excel('./excel/个人任务完成情况.xlsx', index=False)

# 根据‘是否完成’一列的数据，在原表格中新增一列，命名为‘是否完成bool’。
# 新加入的字段中，‘True’对应着’是否完成‘这列的‘是’，’False’对应‘否’。
df_sort['是否完成bool'] = df_sort['是否完成'].apply(lambda x:True if x=='是' else False)
# print(df_sort)

# 分组后计算延期数据
df_delay = 4 - df_sort.groupby(['部门', '责任人'])['是否完成bool'].sum()
# print(df_delay)

# 筛选出延期次数大于等于3的员工名单。
df_delay[df_delay>=3]
# print(df_delay[df_delay>=3])
# 哦莫，一目了然，上面几位同学，你们可能要被领导谈话了，请提前想好借口。

# 筛选出延期次数为0的员工名单就可以看到结果
df_ontime = df_delay[df_delay==0]
# print(df_ontime)
df_ontime_doc = df_ontime.to_excel('./excel/按时完成名单.xlsx')

df_final = pd.read_excel('./excel/按时完成名单.xlsx')
name_list = df_final['责任人'].value_counts()
name_list_doc = name_list.to_excel('./excel/按时完成名单1.xlsx')

# 部门任务完成情况
# 1.每周完成率
department_group = df_sort.groupby(['部门', '日期'])['是否完成bool']
df_department_complete_rate = department_group.sum()/department_group.count()
# print("df_department_complete_rate", df_department_complete_rate)

# 2.总完成率, 再来计算部门月度整体完成率：
department_group = df_sort.groupby(['部门'])['是否完成bool']
df_department_complete_rate = department_group.sum()/department_group.count()
# print("df_department_complete_rate", df_department_complete_rate)

# 公司每周完成率
week_group = df_sort.groupby(['日期'])['是否完成bool']
df_week_complete_rate = week_group.sum()/week_group.count()
# print(df_week_complete_rate)

# 下面再计算一下公司6月整体的任务完成率：
df_complete_rate = df_sort['是否完成bool'].sum()/df_sort['是否完成bool'].count()
print(df_complete_rate)

# 按部门生成工作表页
departments = df_sort['部门'].value_counts().index
writer = pd.ExcelWriter('./excel/按部门分页.xlsx')
for department in departments:
    df_dep = df_sort[df_sort['部门']==department].copy()
    df_dep.drop('是否完成bool', inplace=True, axis=1)
    df_dep.to_excel(writer, department, index=False)
writer.save()