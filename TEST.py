'''
2022.11.14
Author: Yongtae.Seo
'''
import os
import re
from tkinter import *
from tkinter import filedialog
from glob import glob
import numpy as np

root = Tk()
root.title('Hivise')
root.resizable(False, False)


def btn_exe():
    tmp = folder_path()
    main_path.set(tmp)  # <- path
    folder_list = folder_dir(tmp)  # <- ['(0, 0)' ... ]
    # final = map(txt_lst, folder_list)
    for i in folder_list:
        txt_lst(i)
    print(arr_dict)
    return

def merged(sorteds):  # path / 정렬된 텍스트 이터레이터 활용 -> {매개변수 폴더이름 : 머지 배열(ndim : 1)}
    with open(f'{txt_path.get()}/{sorteds}', 'r') as txt:
        tmp1 = txt.read().replace('\t\n', '\t').split('\t')
        tmp2 = filter(lambda x: x != '', tmp1)
        arr = np.array(list(tmp2))
    return arr


def txt_lst(folders):
    path = f'{main_path.get()}/{folders}'
    folder_idx.set(folders)
    txt_path.set(path)
    lst = glob('PRESSURE_*.txt', root_dir = txt_path.get())  # <- 비정렬 텍스트 리스트
    for i in lst:
        idx_txt(i)
    sorted_txt = sorted(txt_dict, key = lambda x: txt_dict[x])  # <- 정렬된 텍스트 이름
    for txt in sorted_txt:
        sorted_txt_lst.append(merged(txt))
    arr_dict[folders] = np.array(sorted_txt_lst).reshape(-1)
    sorted_txt_lst.clear()
    txt_dict.clear()
    return


def idx_txt(arg):  # <- txt 리스트를 받아서 txt_dict 딕셔너리에 이름과
    tmp = indexing(arg)
    txt_dict[arg] = int(''.join([x.zfill(2) for x in tmp]))
    return


def indexing(arg):
    tmp = re.findall(pattern = '\d+', string = arg)
    return tmp


def folder_dir(tmp):
    folders = glob('(*)', root_dir = f'{tmp}')
    point = list(map(indexing, folders))
    # print(point, '<-p')
    # print(folders, '<-f')
    folder_indexing.append(point)
    return folders


def folder_path():
    tmp = filedialog.askdirectory()
    print(tmp, '<-')
    return tmp


def entrylength(var):
    if len(var.get()) > 2:
        var.set(var.get()[1])


'''
Variable
'''
sorted_txt_lst = []
arr_dict = {}
txt_dict = {}
folder_idx = StringVar()
main_path = StringVar()
txt_path = StringVar()
folder_indexing = []
txt_list = []
path_list = []
row_var = StringVar()
col_var = StringVar()
length = 3


'''
UI

'''
frm1 = LabelFrame(root, text = ' 압자 정보 (숫자만 입력하세요) ', bd = 1)
frm1.pack(fill = X, padx = 10, pady = 10)

btn1 = Button(frm1, text = '폴더 선택', padx = 5, pady = 5, command = btn_exe)
btn1.grid(column = 6, padx = 5, pady = 5)

row_label = Label(frm1, text = '행 갯수').grid(row = 0, column = 0)
entry_row = Entry(frm1, width = 2, textvariable = row_var)
entry_row.grid(row = 0, column = 1, padx = 2, pady = 2)
row_var.trace('w', lambda *x: entrylength(row_var))

slash = Label(frm1, text = ' / ').grid(row = 0, column = 2)

col_label = Label(frm1, text = '열 갯수').grid(row = 0, column = 3)
entry_col = Entry(frm1, width = 2, textvariable = col_var)
entry_col.grid(row = 0, column = 4, padx = 2, pady = 2)
col_var.trace('w', lambda *y: entrylength(col_var))

if __name__ == '__main__':
    root.mainloop()
