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
task1_list = []

task2_L_list = []
task2_R_list = []

task3_L_P_list = []
task3_L_M_list = []
task3_L_L_list = []
task3_R_P_list = []
task3_R_M_list = []
task3_R_L_list = []

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
                task1_list.append("{}/{}/{} {}".format(case, sample_num, sample, 1)) # 1: vfp
                
                detail_list = sample.split('_')
                if detail_list[1] == 'L':
                    task2_L_list.append("{}/{}/{} {}".format(case, sample_num, sample, 1))
                    
                    if detail_list[2] == 'P':
                        task3_L_P_list.append("{}/{}/{} {}".format(case, sample_num, sample, 1))
                    elif detail_list[2] == 'M':
                        task3_L_M_list.append("{}/{}/{} {}".format(case, sample_num, sample, 2))
                    elif detail_list[2] == 'L':
                        task3_L_L_list.append("{}/{}/{} {}".format(case, sample_num, sample, 3))
                    
                    
                if detail_list[1] == 'R':
                    task2_R_list.append("{}/{}/{} {}".format(case, sample_num, sample, 2))
                    
                    if detail_list[2] == 'P':
                        task3_R_P_list.append("{}/{}/{} {}".format(case, sample_num, sample, 4))
                    elif detail_list[2] == 'M':
                        task3_R_M_list.append("{}/{}/{} {}".format(case, sample_num, sample, 5))
                    elif detail_list[2] == 'L':
                        task3_R_L_list.append("{}/{}/{} {}".format(case, sample_num, sample, 6))
                
normal_list = np.array(normal_list)
vfp_task1_list = np.array(task1_list)

vfp_task2_L_list = np.array(task2_L_list)
vfp_task2_R_list = np.array(task2_R_list)

vfp_task3_L_P_list = np.array(task3_L_P_list)
vfp_task3_L_M_list = np.array(task3_L_M_list)
vfp_task3_L_L_list = np.array(task3_L_L_list)
vfp_task3_R_P_list = np.array(task3_R_P_list)
vfp_task3_R_M_list = np.array(task3_R_M_list)
vfp_task3_R_L_list = np.array(task3_R_L_list)

# random set split
normal_split = int(0.2 * len(normal_list))
vfp_task1_split = int(0.2 * len(vfp_task1_list))

vfp_task2_L_split = int(0.2 * len(vfp_task2_L_list))
vfp_task2_R_split = int(0.2 * len(vfp_task2_R_list))

vfp_task3_L_P_split = int(0.2 * len(vfp_task3_L_P_list))
vfp_task3_L_M_split = int(0.2 * len(vfp_task3_L_M_list))
vfp_task3_L_L_split = int(0.2 * len(vfp_task3_L_L_list))
vfp_task3_R_P_split = int(0.2 * len(vfp_task3_R_P_list))
vfp_task3_R_M_split = int(0.2 * len(vfp_task3_R_M_list))
vfp_task3_R_L_split = int(0.2 * len(vfp_task3_R_L_list))

random_indices_normal = np.random.choice(len(normal_list), normal_split, replace=False)
random_indices_vfp_task1 = np.random.choice(len(vfp_task1_list), vfp_task1_split, replace=False)

random_indices_vfp_task2_L = np.random.choice(len(vfp_task2_L_list), vfp_task2_L_split, replace=False)
random_indices_vfp_task2_R = np.random.choice(len(vfp_task2_R_list), vfp_task2_R_split, replace=False)

random_indices_vfp_task3_L_P = np.random.choice(len(vfp_task3_L_P_list), vfp_task3_L_P_split, replace=False)
random_indices_vfp_task3_L_M = np.random.choice(len(vfp_task3_L_M_list), vfp_task3_L_M_split, replace=False)
random_indices_vfp_task3_L_L = np.random.choice(len(vfp_task3_L_L_list), vfp_task3_L_L_split, replace=False)
random_indices_vfp_task3_R_P = np.random.choice(len(vfp_task3_R_P_list), vfp_task3_R_P_split, replace=False)
random_indices_vfp_task3_R_M = np.random.choice(len(vfp_task3_R_M_list), vfp_task3_R_M_split, replace=False)
random_indices_vfp_task3_R_L = np.random.choice(len(vfp_task3_R_L_list), vfp_task3_R_L_split, replace=False)

val_normal = normal_list[random_indices_normal]
val_vfp_task1 = vfp_task1_list[random_indices_vfp_task1]
val_task1_set = np.hstack([val_normal, val_vfp_task1])

val_vfp_task2_L = vfp_task2_L_list[random_indices_vfp_task2_L]
val_vfp_task2_R = vfp_task2_R_list[random_indices_vfp_task2_R]
val_task2_set = np.hstack([val_normal, val_vfp_task2_L, val_vfp_task2_R])

val_vfp_task3_L_P = vfp_task3_L_P_list[random_indices_vfp_task3_L_P]
val_vfp_task3_L_M = vfp_task3_L_M_list[random_indices_vfp_task3_L_M]
val_vfp_task3_L_L = vfp_task3_L_L_list[random_indices_vfp_task3_L_L]
val_vfp_task3_R_P = vfp_task3_R_P_list[random_indices_vfp_task3_R_P]
val_vfp_task3_R_M = vfp_task3_R_M_list[random_indices_vfp_task3_R_M]
val_vfp_task3_R_L = vfp_task3_R_L_list[random_indices_vfp_task3_R_L]
val_task3_set = np.hstack([val_normal, val_vfp_task3_L_P, val_vfp_task3_L_M, val_vfp_task3_L_L, val_vfp_task3_R_P, val_vfp_task3_R_M, val_vfp_task3_R_L])




train_normal = np.delete(normal_list, random_indices_normal)
train_vfp_task1 = np.delete(vfp_task1_list, random_indices_vfp_task1)
train_task1_set = np.hstack([train_normal, train_vfp_task1])

train_vfp_task2_L = np.delete(vfp_task2_L_list, random_indices_vfp_task2_L)
train_vfp_task2_R = np.delete(vfp_task2_R_list, random_indices_vfp_task2_R)
train_task2_set = np.hstack([train_normal, train_vfp_task2_L, train_vfp_task2_R])

train_vfp_task3_L_P = np.delete(vfp_task3_L_P_list, random_indices_vfp_task3_L_P)
train_vfp_task3_L_M = np.delete(vfp_task3_L_M_list, random_indices_vfp_task3_L_M)
train_vfp_task3_L_L = np.delete(vfp_task3_L_L_list, random_indices_vfp_task3_L_L)
train_vfp_task3_R_P = np.delete(vfp_task3_R_P_list, random_indices_vfp_task3_R_P)
train_vfp_task3_R_M = np.delete(vfp_task3_R_M_list, random_indices_vfp_task3_R_M)
train_vfp_task3_R_L = np.delete(vfp_task3_R_L_list, random_indices_vfp_task3_R_L)
train_task3_set = np.hstack([train_normal, train_vfp_task3_L_P, train_vfp_task3_L_M, train_vfp_task3_L_L, train_vfp_task3_R_P, train_vfp_task3_R_M, train_vfp_task3_R_L])

os.makedirs(data_path, exist_ok=True)

print("normal_train : {}\n".format(len(train_normal)))
print("normal_val : {}\n".format(len(val_normal)))
print("task1_vfp_train : {}\n".format(len(train_vfp_task1)))
print("task1_vfp_val : {}\n".format(len(val_vfp_task1)))
print("task1 train/val all : {}/{}".format(len(train_task1_set), len(val_task1_set)))


print("task2_vfp_train_L : {}\n".format(len(train_vfp_task2_L)))
print("task2_vfp_train_R : {}\n".format(len(train_vfp_task2_R)))
print("task2_vfp_val_L : {}\n".format(len(val_vfp_task2_L)))
print("task2_vfp_val_R : {}\n".format(len(val_vfp_task2_R)))
print("task2 train/val all : {}/{}".format(len(train_task2_set), len(val_task2_set)))

print("task3_vfp_train_L_P : {}\n".format(len(train_vfp_task3_L_P)))
print("task3_vfp_train_L_M : {}\n".format(len(train_vfp_task3_L_M)))
print("task3_vfp_train_L_L : {}\n".format(len(train_vfp_task3_L_L)))
print("task3_vfp_train_R_P : {}\n".format(len(train_vfp_task3_R_P)))
print("task3_vfp_train_R_M : {}\n".format(len(train_vfp_task3_R_M)))
print("task3_vfp_train_R_L : {}\n".format(len(train_vfp_task3_R_L)))
print("task3_vfp_val_L_P : {}\n".format(len(val_vfp_task3_L_P)))
print("task3_vfp_val_L_M : {}\n".format(len(val_vfp_task3_L_M)))
print("task3_vfp_val_L_L : {}\n".format(len(val_vfp_task3_L_L)))
print("task3_vfp_val_R_P : {}\n".format(len(val_vfp_task3_R_P)))
print("task3_vfp_val_R_M : {}\n".format(len(val_vfp_task3_R_M)))
print("task3_vfp_val_R_L : {}\n".format(len(val_vfp_task3_R_L)))

print("task3 train/val all : {}/{}".format(len(train_task3_set), len(val_task3_set)))





with open(data_path + "train_task1.txt", "w") as file:
    for obj in train_task1_set:
        file.writelines(obj+"\n")

with open(data_path + "val_task1.txt", "w") as file:
    for obj in val_task1_set:
        file.writelines(obj+"\n")

with open(data_path + "train_task2.txt", "w") as file:
    for obj in train_task2_set:
        file.writelines(obj+"\n")

with open(data_path + "val_task2.txt", "w") as file:
    for obj in val_task2_set:
        file.writelines(obj+"\n")

with open(data_path + "train_task3.txt", "w") as file:
    for obj in train_task3_set:
        file.writelines(obj+"\n")

with open(data_path + "val_task3.txt", "w") as file:
    for obj in val_task3_set:
        file.writelines(obj+"\n")

# with open(data_path + "normal_split_index.txt", "w") as file:
#     for obj in random_indices_normal.tolist():
#         file.writelines(str(obj)+"\n")

# with open(data_path + "vfp_split_index.txt", "w") as file:
#     for obj in random_indices_vfp.tolist():
#         file.writelines(str(obj)+"\n")