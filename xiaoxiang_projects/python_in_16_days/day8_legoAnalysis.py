# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=12#

'''
 分析淘宝上售卖乐高玩具的商家总体销售情况
 针对销量最好的店铺做重点研究，分析他们的定价以及宣传策略，把结果用可视化效果图呈现出来，匹配合理化建议。
'''
# 导入包
# 导入包
import numpy as np
import pandas as pd
import time
import jieba
from pyecharts.charts import Bar, Line, Pie, Map, Page
from pyecharts import options as opts
from pyecharts.globals import SymbolType

# 读入数据
df = pd.read_excel('C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/Python认知打卡课课程资料包/资料代码整理/数据分析/解读乐高/数据/乐高淘宝数据.xlsx')
head = df.head() #first 5 rows
print(head)
print(df.shape)
print(df.info()) #可以看到商品名称，店铺名称，价格，付款数量以及地点这五个字段都对应有4044个非空的数据


# 去除重复值
df.drop_duplicates(inplace=True)
print(df.shape)

# 删除购买人数为空的记录
df = df[df['付款人数'].str.contains('人付款')]

# 重置索引
df = df.reset_index(drop=True)
df.info()

# ‘付款人数’这一列数据是数字文字相结合的形式，在后续分析中我们只需使用具体的数字，下面提取‘付款人数’这列的数字信息：
# purchase_num处理
df['付款人数'] = df['付款人数'].str.extract('(\d+)').astype('int') #\d+ = one or more digits.
print(df.head())

# 计算销售额
df['销售额'] = df['价格'] * df['付款人数']
print(df.head())

# location
df['省份'] = df['产地'].str.split(' ').str[0]
print(df.head())

# 乐高销量排名top10店铺 - 条形图
shop_top10 = df.groupby('店铺名称')['付款人数'].sum().sort_values(ascending=False).head(10)
print(shop_top10)

# 条形图
bar1 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar1.add_xaxis(shop_top10.index.tolist())
bar1.add_yaxis('', shop_top10.values.tolist())
bar1.set_global_opts(title_opts=opts.TitleOpts(title='乐高销量排名Top10淘宝店铺'),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
    visualmap_opts=opts.VisualMapOpts(max_=28669)
)
bar1.render()

# 乐高产地数量排名top10

province_top10 = df.省份.value_counts()[:10]
print(province_top10)

# 将统计结果绘制为条形图：
bar2 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar2.add_xaxis(province_top10.index.tolist())
bar2.add_yaxis('', province_top10.values.tolist())
bar2.set_global_opts(title_opts=opts.TitleOpts(title='乐高产地数量排名top10'),
                     visualmap_opts=opts.VisualMapOpts(max_=1000)
                    )
bar2.render()

# 国内各省份乐高销量分布图
province_num = df.groupby('省份')['付款人数'].sum().sort_values(ascending=False)
print(province_num[:5])

# 针对这种地区类型的统计结果，我们可以将它呈现在地图上。以颜色的深浅程度来区分不同地区的数据状况。
map1 = Map(init_opts=opts.InitOpts(width='1350px', height='750px'))
map1.add("", [list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())],
         maptype='china'
        )
map1.set_global_opts(title_opts=opts.TitleOpts(title='国内各产地乐高销量分布图'),
                     visualmap_opts=opts.VisualMapOpts(max_=172277),
                    )
map1.render()

# 天猫乐高价格分布
# 分箱
cut_bins = [0,50,100,200,300,500,1000,8888]
cut_labels = ['0~50元', '50~100元', '100~200元', '200~300元', '300~500元', '500~1000元', '1000元以上']
price_cut = pd.cut(df['价格'], bins=cut_bins, labels=cut_labels)
price_num = price_cut.value_counts()
print(price_num)

bar3 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar3.add_xaxis(['0~50元', '50~100元', '100~200元', '200~300元', '300~500元', '500~1000元', '1000元以上'])
bar3.add_yaxis('', [895, 486, 701, 288, 370, 411, 260])
bar3.set_global_opts(title_opts=opts.TitleOpts(title='不同价格区间的商品数量'),
                     visualmap_opts=opts.VisualMapOpts(max_=900))
bar3.render()

# 不同价格区间的销售额整体表现
# 添加列
df['价格标签'] = price_cut
cut_purchase = df.groupby('价格标签')['销售额'].sum()
print(cut_purchase)

# 绘制饼图可以清晰地看出各价格区间货品销售额在总体占比情况：
data_pair =  [list(z) for z in zip(cut_purchase.index.tolist(), cut_purchase.values.tolist())]
# 绘制饼图
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie1.add('', data_pair, radius=['35%', '60%'])
pie1.set_global_opts(title_opts=opts.TitleOpts(title='不同价格区间的销售额整体表现'),
                     legend_opts=opts.LegendOpts(orient='vertical', pos_top='15%', pos_left='2%'))
pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
pie1.set_colors(['#EF9050', '#3B7BA9', '#6FB27C', '#FFAF34', '#D8BFD8', '#00BFFF', '#7FFFAA'])
pie1.render()

# 玩一个词云图
def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []
    with open(r"C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/Python认知打卡课课程资料包/资料代码整理/数据分析/解读乐高/stop_words.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    # 添加关键词
    my_words = ['乐高', '悟空小侠', '大颗粒', '小颗粒']
    for i in my_words:
        jieba.add_word(i)
    # 分词
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)
    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i)>=2]
    return word_num_selected
text = get_cut_words(content_series=df['商品名称'])
text[:5]