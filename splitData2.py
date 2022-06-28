# conding:utf-8
import sys,os
import math
import random
import shutil
root_path = sys.path[0]
values_path = root_path+"/data"
values_list = os.listdir(values_path)
 
# 生成训练集、测试集、验证集，放文件的位置
target_path = '/home/project/data/images'
target_label_path = '/home/project/data/labels'
target_path_list = [target_path,target_label_path]
train_and_val = random.sample(values_list,int(math.floor(len(values_list)*0.9)))
train_list = random.sample(train_and_val,int(math.floor(len(train_and_val)*8/9)))
val_list = list(set(train_and_val).difference(set(train_list)))
test_list = list(set(values_list).difference(set(train_and_val)))
def create_set(input_list_name, folder_name):
    # 创建相应的文件夹
    for target_g_path in target_path_list:
        folder_name_path = target_g_path + "/" + folder_name
        if not os.path.exists(folder_name_path):
            os.mkdir(folder_name_path)
    # 将数据和标签数复制到指定的位置
    for file in eval(input_list_name):
        # 1.数据写入
        # 数据源所在文件夹
        source_path = root_path + "/data"
        full_target_file_name = os.path.join(source_path, file)  # 把文件的完整路径得到
        # 写入到指定的文件
        target_folder_path = os.path.join(target_path,folder_name)
        shutil.copy(full_target_file_name, target_folder_path)
 
        # 数据标签写入
        source_path = root_path + "/data_label"
        file = file.strip().split('.')[0] + '.txt'
        full_target_file_name = os.path.join(source_path, file)  # 把文件的完整路径得到
        target_folder_path = os.path.join(target_label_path, folder_name)
        shutil.copy(full_target_file_name, target_folder_path)
 
 
 
key_name = ['train', 'val', 'test']
for folder_name in key_name:
    list_name = folder_name + "_list"
    ##txt_name = folder_name + ".txt"
    create_set(list_name, folder_name)