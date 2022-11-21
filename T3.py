import re

lst = ['(0, 0)', '(0, 2)', '(0, 10)']

hi = {}

def sorted_folder(lst):
    tmp = re.findall(pattern = '\d+', string = lst)
    tmp1 = [tmp[0].zfill(2) + tmp[1].zfill(2)]
    hi[lst] = tmp1 + tmp

def main_exe():
    for i in lst:
        sorted_folder(i)


if __name__ == '__main__':
    main_exe()

liakim = sorted(hi, key = lambda x: hi[x])

print(lst)
lst.sort()
print(lst, '<== 그냥 list sort')

print(hi)
print(liakim, '<-')



