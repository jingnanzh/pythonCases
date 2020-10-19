'''
    developer: Wendy
    date: Aug 29,2020
    version: 5.0
    function: differentiate csv or json, use os module command: splitext()
    note: use 'with' to close the file automatically after use
'''

import requests

def get_html_text(url):
    '''
        get url text
    '''
    r = requests.get(url,timeout=30) #wait for 30 seconds
    print(r.status_code)
    return r.text

def main():
    city_pinyin = input('Please give the city name: ')
    url = 'http://www.pm25s.com/en/'+city_pinyin+'.html'
    url_text =  get_html_text(url)
    # print(url_text)
    #ctrl+u 拿到源代码，找到aqi 的值，然后copy前面的div， 注意空格：
    aqi_div= '''<div class="city_aqi">
<div class="value1">'''

    #找到文本中该段文本的起始位置：
    index = url_text.find(aqi_div)
    #找到aqi开始的位置
    begin_index = index + len(aqi_div)
    # 找到aqi结束的位置
    end_index = begin_index + 2
    #找到aqi的值：
    aqi_value =  url_text[begin_index:end_index]

    print('空气质量为：{}'.format(aqi_value))



if __name__=='__main__':
    main()