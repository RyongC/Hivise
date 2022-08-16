'''
Author Seo YongTae
Ver 1.0 Date 2022-08-11
Ver 2.0 Date 2022-08-14
개인적으로 만든거라 맘대로 바꿔 쓰세요
'''

import os
from glob import glob
from time import strftime


def save_final():
    with open(f'{merged_file_dir}/Merged_{merged_file_name}.txt', 'w') as m_file:
        m_file.write(merged_txt)


def read_txt():
    global merged_txt
    for data in raw_fold_list:
        with open(data, 'r') as file:
            for line in file:
                if not line or line == '\n':
                    break
                merged_txt += line
    return


def make_folder(name):
    if name not in os.listdir():
        os.mkdir(name)
    return


raw_fold_list = glob('*.txt')  # *.txt 파일 리스트로 가져오기
merged_file_name = strftime('%Y_%m_%d_%H_%M_%S')  # 파일이름 안겹치게 시간으로
merged_file_dir = 'Merged'  # 반복실행시 서치안되게 예외처리
merged_txt = ''  # 빈 텍스트 생성

read_txt()
make_folder(merged_file_dir)
save_final()
