import os
import re


file_1_name = 'file1'  # source file
file_2_name = 'file2'  # data file
file_3_name = 'file3'  # data file
result_file_name = 'result.txt'


def processing(f1=file_1_name, f2=file_2_name, f3=file_3_name, fr=result_file_name, line_num=0):
    file_1 = open(f1, 'r', encoding='utf-8')
    file_2 = open(f2, 'r', encoding='utf-8')
    file_3 = open(f3, 'r', encoding='utf-8')
    file_result = open(fr, 'r', encoding='utf-8')
    source_line = None
    first_data = None
    second_data = None
    result_line = None
    for _ in range(line_num):
        source_line = None
        first_data = None
        second_data = None
        result_line = None
        try:
            source_line = file_1.readline()
            first_data = file_2.readline()
            second_data = file_3.readline()
            result_line = file_result.readline()
        except Exception as err:
            print('Error : ', err)
            break
    result = {
        'source string :': source_line,
        'first data :': first_data,
        'second data :': second_data,
        'result string :': result_line
    }
    file_1.close()
    file_2.close()
    file_3.close()
    file_result.close()
    return result


if __name__ == '__main__':
    self_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(self_path)
    line_number = int(input('Input number of string : '))
    result = processing(line_num=line_number)
    for key, value in result.items():
        print(key)
        print(value)
