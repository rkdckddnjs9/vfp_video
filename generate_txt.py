import os
import numpy as np

np.random.seed(20240214)

data_path = "./data/spa_data/"
case_list = os.listdir(data_path)
case_list.sort()

# data_list = []
# task define
# vfp_list_task1 class : normal:0, vfp:1
# vfp_list_task2 class : normal:0, vfp_left:1, vfp_right:2
# vfp_list_task3 class : normal:0, vfp_left_P:1, vfp_left_M:2, vfp_left_L:3, vfp_right_P:4, vfp_right_M:5, vfp_right_L:6
normal_list = []
vfp_list = []
for case in case_list:
    if case not in ['Normal', 'VFP',]:
        continue
    sample_list = os.listdir(data_path + case)
    if case == "Normal":
        for sample_num in sample_list: # 1~50, 51~100, ...
            sample_num_list = os.listdir(data_path + case + "/" + sample_num)
            for sample in sample_num_list: # sample data Normal_300_014_C3
                normal_list.append("{}/{}/{} {}".format(case, sample_num, sample, 0)) # 0: Normal
    elif case == "VFP":
        for sample_num in sample_list: # 1~50, 51~100, ...
            sample_num_list = os.listdir(data_path + case + "/" + sample_num)
            for sample in sample_num_list: # sample data VFP_300_014_C3
                vfp_list.append("{}/{}/{} {}".format(case, sample_num, sample, 1)) # 1: vfp
normal_list = np.array(normal_list)
vfp_list = np.array(vfp_list)
# random set split
normal_split = int(0.2 * len(normal_list))
vfp_split = int(0.2 * len(vfp_list))
random_indices_normal = np.random.choice(len(normal_list), normal_split, replace=False)
random_indices_vfp = np.random.choice(len(vfp_list), vfp_split, replace=False)

# import pdb; pdb.set_trace()
val_normal = normal_list[random_indices_normal]
val_vfp = vfp_list[random_indices_vfp]
val_set = np.hstack([val_normal, val_vfp])

train_normal = np.delete(normal_list, random_indices_normal)
train_vfp = np.delete(vfp_list, random_indices_vfp)
train_set = np.hstack([train_normal, train_vfp])

os.makedirs(data_path, exist_ok=True)

with open(data_path + "train.txt", "w") as file:
    for obj in train_set:
        file.writelines(obj+"\n")

with open(data_path + "val.txt", "w") as file:
    for obj in val_set:
        file.writelines(obj+"\n")

with open(data_path + "normal_split_index.txt", "w") as file:
    for obj in random_indices_normal.tolist():
        file.writelines(str(obj)+"\n")

with open(data_path + "vfp_split_index.txt", "w") as file:
    for obj in random_indices_vfp.tolist():
        file.writelines(str(obj)+"\n")