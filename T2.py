from glob import glob
import re

txt_lst = glob('PRESSURE_*.txt')

def txt_sort(txts):
    tmp = re.findall('\d+', txts)
    idx = int(''.join([x.zfill(2) for x in tmp]))
    return idx

idx = map(txt_sort, txt_lst)
txt_dict = dict(zip(txt_lst, idx))
sorted_txt = sorted(txt_dict, key = lambda x : txt_dict[x])

print(sorted_txt)