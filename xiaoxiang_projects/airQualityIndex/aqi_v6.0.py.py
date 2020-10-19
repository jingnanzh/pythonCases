'''
    developer: Wendy
    date: Aug 29,2020
    version: 6.0
    function: Beautiful soup
'''

import requests
#先运行 pip install beautifulsoup4
from bs4 import BeautifulSoup

def get_city_aqi(city_pinyin):
    '''
        get city aqi value
    '''
    url = 'http://www.pm25s.com/' + city_pinyin + '.html'
    r = requests.get(url,timeout=30)

    #此处需要确保安装了lxml，‘pip install lxml’，否则报错
    soup = BeautifulSoup(r.text,'lxml')

    #找到该value所在的节点,用。text取值时加上strip()可以去掉多余的空格：
    city_aqi = soup.find('div',{'class': "value1"}).text.strip()
    return  city_aqi

def main():
    city_pinyin = input('Please give the city name: ')
    city_aqi = get_city_aqi(city_pinyin)

    print('空气质量为：{}'.format(city_aqi))

if __name__=='__main__':
    main()