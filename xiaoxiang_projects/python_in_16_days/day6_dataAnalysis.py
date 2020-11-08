# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=7#

'''
 数据分析流程与常用模块
 2011-2020年各个城市的房价数据在Excel表格中，
 如何让它清晰直观地呈现出房价随时间发展的情况呢？现在就用Python试试看。
'''
import matplotlib.pyplot as plt
import imageio
import pandas as pd

#读取表格数据
frames = []
df = pd.read_excel('C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/Python认知打卡课课程资料包/资料代码整理/data_source_house.xlsx', index_col='年份')

# 数据上限
xlim_num = 60000
# 横坐标绘制跨度
xlim_interval = 20000
# 循环每年
for year in df.index:
    # 获取行数据
    row_data_list = df.loc[year]
    # 按价格排序
    row_data_list.sort_values(ascending = True, inplace=True)
    # 设置外观相关信息
    font = {'family': 'SimHei',
            'style': 'normal',
            'weight': 'normal',
            'color': '#FFFFFF',
            'size': 20,
     }
    plt.rcParams['figure.figsize'] = (16.0, 9.0)
    plt.rcParams['axes.facecolor'] = '#0D0434'
    plt.rcParams['savefig.facecolor'] = '#0D0434'
    plt.rcParams['xtick.color'] = '#FFFFFF'
    plt.rcParams['ytick.color'] = '#FFFFFF'
    plt.rcParams['axes.edgecolor'] = '#FFFFFF'
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.tick_params(labelsize=20)
    plt.xlim((0, int(xlim_num)))
    plt.xticks(range(0, xlim_num, xlim_interval))
    # 绘制每个柱子种的数字
    for index, data in enumerate(row_data_list):
        plt.text(int(xlim_num) / 10, index, str(data), ha='left', va='center', fontdict=font)
    # 绘制柱形图，将图片存到文件 year.png
    plt.barh(row_data_list.index, row_data_list, height=0.35, facecolor='#2C43C2', edgecolor='white')
    plt.title(str(year), fontdict=font)
    plt.savefig('%s.png' % str(year))
    plt.close('all')
    # 将生成好的图片数据再读出，存储到图片帧列表frames中
    im = imageio.imread('%s.png' % str(year))
    frames.append(im)
    # 将所有png图片拼成gif动画，设定每秒一帧播放，就能清晰地统计出城市房价的发展情况
    imageio.mimsave('data_gif.gif', frames, 'GIF', duration=round(1, 2))