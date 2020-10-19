'''
    developer: Wendy
    date: Aug 26,2020
    version: 3.0
    function: differentiate csv or json, use os module command: splitext()
    note: use 'with' to close the file automatically after use
'''
import json
import csv
import os

def process_json_file(file_path):
    '''
        decode the json file
    '''
    with open(file_path, mode = 'r', encoding = 'utf-8' ) as f:
        city_list = json.load(f)
        print(city_list)

def process_csv_file(file_path):
    '''
        decode the csv file
    '''
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    file_path = input('please input the file name: ')
    file_name, file_ext = os.path.splitext(file_path)

    if file_ext == '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print('This format is not supported')

if __name__=='__main__':
    main()