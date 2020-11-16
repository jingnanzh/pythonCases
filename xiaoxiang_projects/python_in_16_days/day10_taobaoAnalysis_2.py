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
import seaborn as sns
import numpy as np
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
# print(pv_hour)

# 每小时uv
uv_hour = data.groupby('小时')['用户身份'].nunique()
# print(uv_hour)

# 连接两个表
pv_uv_hour = pd.concat([pv_hour, uv_hour], axis = 1)
pv_uv_hour.columns = ['pv_hour', 'uv_hour']
# print(pv_uv_hour)

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

# 用户行为分析
# 总计点击情况:原数据中记录了用户行为类型字段：用户行为类型，包括点击、收藏、加入购物车、支付四种行为，
# 分别用数字1、2、3、4表示，那产生每种行为类型的用户有多少呢？
type_1 = data[data['用户行为类型']==1]["用户身份"].count()
type_2 = data[data['用户行为类型']==2]["用户身份"].count()
type_3 = data[data['用户行为类型']==3]["用户身份"].count()
type_4 = data[data['用户行为类型']==4]["用户身份"].count()
print("点击用户：",type_1)
print("收藏用户：",type_2)
print("添加购物车用户：",type_3)
print("支付用户：",type_4)

# 创建一个透视表比较一下日期维度下的用户行为数据，然后再将数据绘制在图像中，运用的还是matplotlib模块。

#日维度
pv_date_type = pd.pivot_table(data,index='日期',
                             columns='用户行为类型',
                             values='用户身份',
                             aggfunc=np.size)
pv_date_type.columns = ["点击","收藏","加入购物车","支付"]
print(pv_date_type.head())
# 绘图如下
plt.figure(figsize=(16,10))
sns.lineplot(data=pv_date_type[['收藏', '加入购物车', '支付']])

plt.tight_layout()
plt.savefig("不同日期不同用户行为的PV变化趋势.pdf",dpi=300)
plt.show()


# 时间维度
pv_hour_type = pd.pivot_table(data,index='小时',
                             columns='用户行为类型',
                             values='用户身份',
                             aggfunc=np.size)
pv_hour_type.columns = ["点击","收藏","加入购物车","支付"]
print(pv_hour_type)
# 绘图如下
plt.figure(figsize=(16,10))
sns.lineplot(data=pv_hour_type[['收藏', '加入购物车', '支付']])

# 产生点击行为的用户数量级较大，与其它数据放在同一个坐标系中不方便我们发现数据的波动幅度，所以这里我们只绘制了收藏、加入购物车、支付的用户数据。
# pv_hour_type["点击"].plot(c="pink",linewidth=5,label="点击",secondary_y=True)
# plt.legend(loc="best")

plt.tight_layout()
# plt.savefig("不同小时不同用户行为的PV变化趋势.pdf",dpi=300)
plt.show()

# 人均消费次数: 用每日的【付费总次数/付费总人数】即可。
total_custome = data[data['用户行为类型'] == 4].groupby(["日期","用户身份"])["用户行为类型"].count()\
                .reset_index().rename(columns={"用户行为类型":"消费次数"})
total_custome
total_custome2 = total_custome.groupby("日期").sum()["消费次数"]/\
                 total_custome.groupby("日期").count()["消费次数"]
print(total_custome2.head(10))
# 绘图如下, 用折线图看一下分析结果：
x = len(total_custome2.index.astype(str))
y = total_custome2.index.astype(str)

plt.plot(total_custome2.values)
plt.xticks(range(0,14),[y[i] for i in range(0,x,1)],rotation=90) #range此处应该是14
plt.title("每天的人均消费次数")

plt.tight_layout()
#plt.savefig("每天的人均消费次数.pdf",dpi=300)
plt.show()


# 活跃用户人均消费次数，用【付费总次数/活跃用户数】即可。
data["operation"] = 1
aa = data.groupby(["日期","用户身份",'用户行为类型'])["operation"].count().\
     reset_index().rename(columns={"operation":"总计"})
print("aa.head(10)",aa.head(10))
aa1 = aa.groupby("日期").apply(lambda x: x[x["用户行为类型"]==4]["总计"].sum()/x["用户身份"].nunique())
print("aa1.head(10)",aa1.head(10))
# 绘图如下
x = len(aa1.index.astype(str))
y = aa1.index.astype(str)

plt.plot(aa1.values)
plt.xticks(range(0,14),[y[i] for i in range(0,x)],rotation=90)
plt.title("每天的活跃用户消费次数")

plt.tight_layout()
#plt.savefig("每天的活跃用户消费次数.pdf",dpi=300)
plt.show()

# 付费率（PUR，Pay User Rate）是指统计周期内，付费账号数占活跃账号数的比例。
# 付费率
rate = aa.groupby("日期").apply(lambda x: x[x["用户行为类型"]==4]["总计"].count()/x["用户身份"].nunique())
rate.head(10)
# 绘图如下
x = len(rate.index.astype(str))
y = rate.index.astype(str)

plt.plot(rate.values)
plt.xticks(range(0,14),[y[i] for i in range(0,x,1)],rotation=90)
plt.title("付费率分析")

plt.tight_layout()
# plt.savefig("付费率分析",dpi=300)
plt.show()

# 漏斗分析
# 从页面点击到最终支付，中间每一步都会流失部分用户，
# 通过漏斗分析能让我们了解当前的转化状态，为增长提供基础。
# 先统计每种行为的总人数，为后续铺垫一下。
df_count = data.groupby("用户行为类型").size().reset_index().rename(columns={"用户行为类型":"环节",0:"人数"})
print(df_count)
type_dict = {
    1:"点击",
    2:"收藏",
    3:"加入购物车",
    4:"支付"
}
df_count["环节"] = df_count["环节"].map(type_dict)
print(df_count)
# 将收藏及加入购物车作为一步，统计每个步骤的人数
a = df_count.iloc[0]["人数"]
b = df_count.iloc[1]["人数"]
c = df_count.iloc[2]["人数"]
d = df_count.iloc[3]["人数"]
funnel = pd.DataFrame({"环节":["点击","收藏及加入购物车","支付"],"人数":[a,b+c,d]})

# 计算每个步骤的转化率
funnel["总体转化率"] = [i / funnel["人数"][0] for i in funnel["人数"]]
funnel["单一转化率"] = np.array([1.0, 2.0, 3.0])
for i in range(0, len(funnel["人数"])):
    if i == 0:
        funnel["单一转化率"][i] = 1.0
    else:
        funnel["单一转化率"][i] = funnel["人数"][i] / funnel["人数"][i - 1]

print("funnel", funnel)


# 绘制漏斗分析图
import plotly.express as px
import plotly.graph_objs as go

trace = go.Funnel(
    y=["点击", "收藏及加入购物车", "购买"],
    x=[funnel["人数"][0], funnel["人数"][1], funnel["人数"][2]],
    textinfo="value+percent initial",
    marker=dict(color=["deepskyblue", "lightsalmon", "tan"]),
    connector={"line": {"color": "royalblue", "dash": "solid", "width": 3}})
print("trace",trace) #a dictionary for Funnel with all parameters above
data1 = [trace]
print("data1",data1) #put funnel in a list
fig = go.Figure(data1) #create a webpge http://127.0.0.1:57577/ and show the figure
fig.show() #

# RFM 模型是数据分析中衡量客户价值和客户创利能力的一个重要模型。为什么叫做RFM模型呢？
# 因为我们会搜集用户三个方面的数据来综合评定用户的价值等级，而这三项数据分别就是这里的RFM：
# R（Recency）——最近一次购买的时间有多远
# F（Frequency）——最近一段时间内的消费频率
# M（Monetary）——最近一段时间内的消费金额

# 首先计算出我们需要的数据：最近一次购买时间有多远和最近一段时间的消费频率
from datetime import datetime
# 最近一次购买距离现在的天数
recent_buy = data[data["用户行为类型"]==4].groupby("用户身份")["日期"].\
             apply(lambda x:datetime(2014,12,20) - x.sort_values().iloc[-1]).reset_index().\
             rename(columns={"日期":"最近消费时间距现在"})
recent_buy["最近消费时间距现在"] = recent_buy["最近消费时间距现在"].apply(lambda x: x.days)
recent_buy[:10]
# 购买次数计算
buy_freq = data[data["用户行为类型"]==4].groupby("用户身份")["日期"].count().reset_index().\
          rename(columns={"日期":"消费频率"})
buy_freq[:10]

# 将上述两列数据，合并起来
rfm = pd.merge(recent_buy,buy_freq,on="用户身份")
rfm[:10]
# 给不同类型打分
r_bins = [0,5,10,15,20,50]
f_bins = [1,30,60,90,120,900]
rfm["消费时间打分"] = pd.cut(rfm["最近消费时间距现在"],bins=r_bins,labels=[5,4,3,2,1],right=False)
rfm["消费频率打分"] = pd.cut(rfm["消费频率"],bins=f_bins,labels=[1,2,3,4,5],right=False)
for i in ["消费时间打分","消费频率打分"]:
    rfm[i] = rfm[i].astype(float)
rfm.describe() #调用describe()函数我们得到消费时间和频率打分的平均值
# （第二行名称为mean的数据），
# 然后把各分值与得到的均值做比较，高于均值标注‘高’，低于它则标注‘低’。
# 综合时间和频率两项因素，最终得出综合值，以此判定用户的价值。

# 比较各分值与各自均值的大小
rfm["时间结果"] = np.where(rfm["消费时间打分"]>1.779783,"高","低")
rfm["频率结果"] = np.where(rfm["消费频率打分"]>1.000401,"高","低")
# 将r和f列的字符串合并起来
rfm["综合值"] = rfm["时间结果"].str[:] + rfm["频率结果"].str[:]
rfm.head()
# 根据打分结果，给用户贴上对应标签，计算出每个类型用户的数量，
# 业务负责的同学们就可以根据标签来区别用户。

# 自定义函数给用户贴标签
def trans_labels(x):
    if x == "高高":
        return "重要价值用户"
    elif x == "低高":
        return "重要唤回用户"
    elif x == "高低":
        return "重要深耕用户"
    else:
        return "重要挽回用户"
rfm["标签"] = rfm["综合值"].apply(trans_labels)
# 计算出每个标签的用户数量
rfm["标签"].value_counts() #可以看到，在这两周的用户群体中，
# 有1480位是重要深耕用户，有1012位重要挽回用户，1位重要价值用户，
# 负责业务的同学可以根据结果找到对应的用户，针对性的做一些运营手段

