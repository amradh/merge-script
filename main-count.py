import os
import re


file_1_name = 'file1'
file_2_name = 'file2'
file_3_name = 'file3'
result_file_name = 'result.txt'


def processing(f1=file_1_name, f2=file_2_name, f3=file_3_name, fr=result_file_name):
    file_1 = open(f1, 'r', encoding='utf-8')
    file_2 = open(f2, 'r', encoding='utf-8')
    file_3 = open(f3, 'r', encoding='utf-8')
    file1_lines_count = 0
    with open(fr, 'w', encoding='utf-8') as result_file:
        for line in file_1:
            file1_lines_count += 1
            source_string = line.strip()
            try:
                first_string = file_2.readline().strip()
                second_string = file_3.readline().strip()
                assert first_string, f'Empty line in {file_2_name} file'
                assert second_string, f'Empty line in {file_3_name} file'
            except Exception as e:
                print('Failed to get data ffirstrom file:', e)
                file_1.close()
                file_2.close()
                file_3.close()
                return 'File processing error'
            pattern_split = '\x01'
            source_list = re.split(pattern_split, source_string)
            if len(source_list) != 6:
                print('The string does not correspond to the number of fragments.')
                print('Line number =', file1_lines_count)
                print('String :', source_string)
                print(f'The data for the line : \n{first_string} \n {second_string}')
            try:
                source_list[-2] = first_string
                source_list[-1] = second_string
            except Exception as e:
                print('Line processing error :', e, '\nString =', source_string)
                return 'Line processing error'
            result_string = pattern_split.join(source_list) + '\n'
            result_file.write(result_string)
    file_1.close()
    file_2.close()
    file_3.close()
    print('The result is saved in the file :', fr)
    return 'Done'


if __name__ == '__main__':
    self_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(self_path)
    result_status = processing()
    print('Task status :', result_status)
