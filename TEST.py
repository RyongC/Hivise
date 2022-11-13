'''
2022.11.10
Author: Yongtae.Seo
'''
import os
from tkinter import *
from tkinter import filedialog
from glob import glob

root = Tk()
root.title('Hivise')
root.resizable(False, False)


def btn_exe():
    tmp = folder_path()
    path = folder_dir(tmp)
    final = map(txt_lst, path)
    print(list(final))
    return

## 아래 꺼 한번더 생각해보자
def txt_lst(tmp):
    # lst = glob(f'{tmp}\PRESSURE_*.txt')
    # tmp = []
    # for txt in lst:
    #     tmp.append(txt.lstrip(f'{tmp}\PRESSURE_').rstrip('.txt').split('_'))
    # print(tmp)
    # return
    tmp1 = os.listdir(tmp)
    print(tmp1)
    return



def folder_dir(tmp):
    path = glob(f'{tmp}\(*)')
    print(path)
    return path


def folder_path():
    tmp = filedialog.askdirectory()
    print(tmp)
    return tmp


def entrylength(var):
    if len(var.get()) > 2:
        var.set(var.get()[1])


'''
Variable
'''

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
