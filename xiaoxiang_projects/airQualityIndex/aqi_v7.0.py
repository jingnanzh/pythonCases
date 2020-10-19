'''
    developer: Wendy
    date: Aug 29,2020
    version: 7.0
    function: Beautiful soup
'''

import requests
#先运行 pip install beautifulsoup4
from bs4 import BeautifulSoup

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
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        # print(city_pinyin)
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name,city_aqi)

if __name__=='__main__':
    main()