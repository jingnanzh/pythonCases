'''
    developer: Wendy
    date: Aug 29,2020
    version: 10.0
    function: 数据清洗 pandas 处理缺失数据，填充数据
'''

import pandas as pd
import matplotlib.pyplot as plt


def main():
    aqi_data =  pd.read_csv('china_city_aqi.csv')
    # print('基本信息：')
    # print(aqi_data.info())

    # print('数据预览；')
    # print(aqi_data.head()) #print first 5 rows

    #数据清洗，只保留aqi>0的数据
    # filter_condition = aqi_data['aqi']>0
    # clean_aqi_data = aqi_data[filter_condition]
    # 或者一步到位:
    # clean_aqi_data = aqi_data[aqi_data['aqi']>0]

    #如果是数字可以max,min,mean
    # print('最大值', clean_aqi_data['aqi'].max)
    # print('最小值', clean_aqi_data['aqi'].min)
    # print('均值', clean_aqi_data['aqi'].mean)
    #排序top10
    # top10_cities = clean_aqi_data.sort_values(by= ['aqi']).head(10)
    # print('空气质量最好的十个城市：')
    # print(top10_cities)

    # bottom10_cities = clean_aqi_data.sort_values(by= ['aqi']).tail(10)
    # bottom10_cities = clean_aqi_data.sort_values(by=['aqi'],ascending=False).head(10)
    # print('空气质量最差的十个城市：')
    # print(bottom10_cities)

    # 保存到csv文件：
    # top10_cities.to_csv('top10_aqi.csv',index = False) #不带索引号保存到一个文件

    # 数据可视化；
    # top50_cities = clean_aqi_data.sort_values(by= ['aqi']).head(50)
    top50_cities = clean_aqi_data.sort_values(by=['aqi']).head(50)

    # 如果aqi 有数值可以用下面的code画出图：
    top50_cities.plot(kind='bar',x='city',y='aqi',title='城市空气质量图',
                      figsize=(20,10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()



    # print(aqi_data['city']) #print the first column
    print(aqi_data[['city','aqi']]) #print multiple columns

if __name__=='__main__':
    main()