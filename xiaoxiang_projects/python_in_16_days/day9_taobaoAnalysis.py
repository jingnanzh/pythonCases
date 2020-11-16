# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=12#

'''
 对淘宝的用户行为数据分析可以为决策提供有力支撑，一起解读数据分析常见专题分析：
 流量指标分析，用户行为分析，漏斗流失分析和用户价值分析。
 流量指标分析
 用户行为分析
 漏斗流失分析
 用户价值RFM分析
'''
# 导入相关库
import pandas as pd
from matplotlib import pyplot as plt
# import seaborn as sns
# import numpy as np
import warnings
# 有时候运行代码时会有很多warning输出，像提醒新版本之类的，如果不想这些乱糟糟的输出，可以使用如下代码
warnings.filterwarnings('ignore')

# if need to display chinese in the graph:
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读入数据
data = pd.read_csv('C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/Python认知打卡课课程资料包/资料代码整理/数据分析/淘宝用户消费行为数据分析/taobao_consume.csv')
head = data.head() #first 5 rows
#查看数据统计信息(具体得到了哪些指标,最大值，平均值，标准差…)
print(data.describe())

print(head)      #first 5 rows
print(data.shape)  #row column 的值
print(data.info()) #可以看到每个Column对应有多少个非空的数据，data type

# 计算每列缺失率
data.apply(lambda x:sum(x.isnull())/len(x))
# print("缺失率",data.apply(lambda x:sum(x.isnull())/len(x)))
# 删除地理位置列: 地理位置数据缺失率72%，缺失率比较高，所以我们决定粗暴地把这列删除。
data.drop(['地理位置'], axis = 1, inplace = True)

# 处理日期数据为 日 小时
data['日期'] = data['行为发生时间'].str[0:-3]
data['小时'] = data['行为发生时间'].str[-2:]

# 将time、date列都变为标准日期格式，将hour列变为int格式经过这样一番操作，
# 原数据中就添加了两列：日期、小时，分别记录下单日期和小时。
data['行为发生时间'] = pd.to_datetime(data['行为发生时间'])
# print(data['行为发生时间'])
data['日期'] = pd.to_datetime(data['日期'])
data['小时'] = data["小时"].astype(int)
# print(data.dtypes)

# 按下单时间排一下序。
# 按照time列升序排序
data.sort_values(by="行为发生时间",ascending=True,inplace=True)
# print(data.head())

# 排序之后看到最左侧的数据索引也跟着做了调整，看起来十分凌乱，非常麻烦不好处理，
# 我们可以删除原索引，重新生成一组有序索引。
# 删除原索引:
data.reset_index(drop=True,inplace=True)
# print(data.head())

# 对时间数据做一个概览, 用unique()函数获取到日期这一列下有多少个不同元素。
data['日期'].unique() #结果显示记录的是从11月24日开始到12月7日结束的用户消费行为数据。
                     #result: 14
# 流量指标 pv, uv:
# pv：page view的缩写，指的是页面总浏览量。每个用户每刷新一次网页，就会增加一次pv。
# uv：unique visitor的缩写，指的是独立访客
# pv>=uv

# 两周的总pv
total_pv = data['用户身份'].count()
# print(total_pv) #458612 （总访问数）

# 两周的总uv
total_uv = data['用户身份'].nunique()
# print(total_uv) #8072 (8072个访客）

# 日期维度下（每日）的pv和uv，只需要先按照日期把数据分组，然后同样进行上面的操作。
# 每日pv
pv_daily = data.groupby('日期')['用户身份'].count()
# print(pv_daily)

# 每日uv
uv_daily = data.groupby('日期')['用户身份'].nunique()
# print(uv_daily)

# 先把所需要的数据——每日pv,uv连接在同一个表里：
# 连接两个表
pv_uv_daily = pd.concat([pv_daily, uv_daily], axis = 1)
pv_uv_daily.columns = ['pv', 'uv']
# print(pv_uv_daily)

# 我们分别为pv和uv数据绘制折线图，让它们在同一子图中显示，subplot()函数就实现了这个功能。
# 同时还可以自由设置绘制结果的线条颜色，图片大小等。
# 绘图

plt.figure(figsize=(16,10))
plt.subplot(211)
plt.plot(pv_daily,c="g") #color = green
plt.title("每天页面的总访问量(PV)")
plt.subplot(212)
plt.plot(uv_daily,c="r")  #color = red
plt.title("每天页面的独立访客数(UV)")
#plt.suptitle("PV和UV的变化趋势")
plt.tight_layout()
plt.savefig("PV和UV的变化趋势.pdf",dpi=300) #
plt.show()

# 每小时pv
pv_hour = data.groupby('小时')['用户身份'].count()
print(pv_hour)

# 每小时uv
uv_hour = data.groupby('小时')['用户身份'].nunique()
print(uv_hour)

# 连接两个表
pv_uv_hour = pd.concat([pv_hour, uv_hour], axis = 1)
pv_uv_hour.columns = ['pv_hour', 'uv_hour']
print(pv_uv_hour)

# 绘制图像
plt.figure(figsize=(16,10))
pv_uv_hour["pv_hour"].plot(c="steelblue",label="每个小时的页面总访问量")
plt.ylabel("页面访问量")
pv_uv_hour["uv_hour"].plot(c="red",label="每个小时的页面独立访客数",secondary_y=True)
plt.ylabel("页面独立访客数")
plt.xticks(range(0,24),pv_uv_hour.index)
plt.legend(loc="best")
plt.grid(True)
plt.tight_layout()
#plt.savefig("每个小时的PV和UV的变化趋势",dpi=300)
plt.show()  #从图中可以看出，晚上22：00-凌晨5：00，页面的访问用户数量和访问量逐渐降低，
# 该时间段很多人都处在休息之中。而从早上6：00-10：00用户数量逐渐呈现上升趋势，
# 10：00-18：00有一个比较平稳的状态，这个时间段是正常的上班时间。
# 但是18：00以后，一直到晚上22：00，用户剧烈激增，一直达到一天中访问用户数的最大值。
# 参考这份数据结果，业务相关同学就可以针对用户的活跃时间段，例如18：00-22:00，采取一些促销活动。

