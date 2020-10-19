'''
    developer: Wendy
    date: Aug 29,2020
    version: 8.0
    function: csv
'''

import requests
#先运行 pip install beautifulsoup4
from bs4 import BeautifulSoup
import csv

def get_city_aqi(city_pinyin):
    '''
        get city aqi value
    '''
    url = 'http://www.pm25s.com/' + city_pinyin
    r = requests.get(url,timeout=30)
    #此处需要确保安装了lxml，‘pip install lxml’，否则报错
    soup = BeautifulSoup(r.text,'lxml')
    # print(soup)
    #找到该value所在的节点,用text取值时加上strip()可以去掉多余的空格：
    #没找到怎么把value2也能find的方法：
    city_aqi = soup.find('div',{'class': "value1"}).text
    return city_aqi

def get_all_cities():
    '''
        获取所有城市
    '''
    url = 'http://www.pm25s.com/'
    city_list=[]
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    city_div = soup.find('div',{'class': "state"})
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href']
        city_list.append((city_name,city_pinyin))
    return city_list

def main():
    city_list = get_all_cities()
    header = ['city','aqi']

    with open('china_city_aqi.csv','w',encoding='utf-8', newline = '') as f:
        writer =  csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            # if (i+1)%10==0:
            #     print('Has handled {} records. (Total records: {})'.format(i+1,len(city_list))
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            print(city_name,city_aqi)
            # row = [city_name]+city_aqi
            # 必须在列表里，否则是单个字母输出
            row = [city_name] + [city_aqi]
            writer.writerow(row)

if __name__=='__main__':
    main()