'''
    developer: Wendy
    date: Aug 26,2020
    version: 3.0
    function: read csv files
'''
import json
import csv

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

    lines = []
    # get the names of columns
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    # write to the csv file:
    f = open('aqiW.csv', 'w', encoding='utf-8',newline='') #newline will make sure lines have no empty line in between
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

if __name__=='__main__':
    main()