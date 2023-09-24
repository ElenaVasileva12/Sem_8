# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# 1) Для дочерних объектов указывайте родительскую директорию.
# 2) Для каждого объекта укажите файл это или директория.
# 3) Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.


import os 
import pickle
import json
import csv

#  находим размер директорий
def get_directory_size(path: str=os.getcwd()):
    dir_sizes={}
    for dir_path, _, file_name in os.walk(path):  #обходит все папки, подпапки, файлы
        size_p = sum(os.path.getsize(os.path.join(dir_path,file)) for file in file_name)
        dir_sizes[dir_path] = size_p #нашли размеры папок
    return dir_sizes



def get_file(path: str=os.getcwd()):
    file_list=[]
    size_f=0
    for obj in os.listdir(path):  #обходит все папки, подпапки, файлы
        objpath = os.path.join(path, obj) # полный путь
        sizes_ob=get_directory_size()
        if os.path.isfile(objpath):
            size_f=os.path.getsize(f'{objpath}')
            file_list.append(f'{objpath} -> {size_f} -> file')
        elif os.path.isdir(objpath):
            file_list.append(f'{objpath} - > {sizes_ob.get(objpath)} -> dir')
    
    return file_list

    # for i in file_list:
    #     print(i)

 #записываем Json
def python_to_json(file_list:list,json_file):
    with open(json_file,'w',encoding='UTF-8') as file:
        json.dump(file_list,file,indent=4,ensure_ascii=False)

 #записываем csv
def python_to_csv (file_list,csv_file):
    with open(csv_file,'w',encoding='UTF-8') as file1:
        write = csv.writer(file1,delimiter = '\r')
        write.writerow(file_list)

 #записываем Pickle
def python_to_pickle(file_list:list,pickle_file):
    with open(pickle_file,'wb') as file2:
        pickle.dump(file_list,file2)  
      


s=get_file('C:/Users/User/Desktop/Python/GB/Погружение в Python/PyCh/Sem_8')    
print(python_to_json(s,'Home_work_8.json'))
print(python_to_csv(s,'Home_work_8.csv'))
print(python_to_pickle(s,'Home_work_8.pickle'))



