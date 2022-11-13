'''
Author : Yongtae.Seo
Date : 2022.11.13
'''


import numpy as np
from glob import glob
import re

def arr_txt(args):
    with open(args, 'r') as txt:
        # print(txt)
        tmp1 = txt.read().replace('\t\n', '\t')
        tmp2 = tmp1.split('\t')
        tmp3 = filter(lambda x: x != '', tmp2)
        arr = np.array(list(tmp3)).reshape(-1, 40).astype('int32')
    return arr

def txt_sort(txts):
    tmp = re.findall('\d+', txts)
    idx = int(''.join([x.zfill(2) for x in tmp]))
    return idx


txt_glob = glob('PRESSURE_*.txt')
idx = map(txt_sort, txt_glob)
txt_dict = dict(zip(txt_glob, idx))
sorted_txt = sorted(txt_dict, key = lambda x : txt_dict[x])

final = map(arr_txt, sorted_txt)
fin_arr = np.array(list(final)).reshape(-1, 40)

np.savetxt('./hello.csv', fin_arr, delimiter = '\t', fmt = '%d')





