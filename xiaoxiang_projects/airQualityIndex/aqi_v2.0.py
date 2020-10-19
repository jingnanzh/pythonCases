'''
    developer: Wendy
    date: Aug 26,2020
    version: 2.0
    function: read jason files
'''
import json

def process_json_file(file_path):
    '''
        decode the json file
    '''
    f = open(file_path, mode = 'r', encoding = 'utf-8' )
    city_list = json.load(f)
    return city_list

def main():
    file_path = input('please input the json file name: ')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda pp:pp['aqi'])
    top5_list = city_list[0:5]

    # write to the json file:
    f = open('top_aqi.json', mode= 'w', encoding='utf-8')
    json.dump(top5_list,f,ensure_ascii= False) #ensure is to ensure no 乱码
    f.close()

if __name__=='__main__':
    main()