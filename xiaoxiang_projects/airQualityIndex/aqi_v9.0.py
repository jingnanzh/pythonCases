'''
    developer: Wendy
    date: Aug 29,2020
    version: 9.0
    function: 数据处理 pandas
'''

import pandas as pd



def main():
    aqi_data =  pd.read_csv('china_city_aqi.csv')
    # print('基本信息：')
    # print(aqi_data.info())
    #
    # print('数据预览；')
    # print(aqi_data.head()) #print first 5 rows

    #如果是数字可以max,min,mean
    # print('最大值', aqi_data['aqi'].max)
    # print('最小值', aqi_data['aqi'].min)
    # print('均值', aqi_data['aqi'].mean)
    #排序top10
    # top10_cities = aqi_data.sort_values(by= ['aqi']).head(10)
    # print('空气质量最好的十个城市：')
    # print(top10_cities)

    # bottom10_cities = aqi_data.sort_values(by= ['aqi']).tail(10)
    # bottom10_cities = aqi_data.sort_values(by=['aqi'],ascending=False).head(10)
    # print('空气质量最差的十个城市：')
    # print(bottom10_cities)

    # 保存到csv文件：
    # top10_cities.to_csv('top10_aqi.csv',index = False) #不带索引号的保存到一个文件



    # print(aqi_data['city']) #print the first column
    print(aqi_data[['city','aqi']]) #print multiple columns

if __name__=='__main__':
    main()