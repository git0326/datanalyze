import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
from matplotlib.ticker import MaxNLocator
from tqdm import tqdm
# import multiprocessing
import concurrent.futures

os.sched_setaffinity(0, range(8))
id_select_list = [3304, 3404]
gld_id_select = 3304


def my_plot_func(liset_struct):
    data = liset_struct[0]
    num = liset_struct[1]
    label = liset_struct[2]
    fig_path = liset_struct[3]
    data_select = data[data[label] == num]
    x_list = data_select[label_x]
    data_select = data_select[x_list < 150]

    seq = data_select["sequence"]
    range_list = data_select[label_range]
    doppler_list = data_select[label_doppler]
    if seq.size > 10:
        plt.figure(figsize=(24, 12))
        plt.subplot(2, 3, 1)
        plt.scatter(range_list, data_select[label_range])
        plt.ylim(-10, 250)
        plt.ylabel(label_range)
        plt.legend(label_range)
        plt.title(label_range)
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.subplot(2, 3, 2)
        plt.scatter(range_list,  (data_select[label_azm]).multiply(57.3))
        plt.ylim(-90, 90)
        plt.ylabel(label_azm)
        plt.legend(label_azm)
        plt.title(label_azm)
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.subplot(2, 3, 3)
        plt.scatter(range_list, (data_select[label_ele]).multiply(57.3))
        plt.legend([label_ele])
        plt.ylim(-30, 30)
        plt.ylabel(label_ele)
        plt.title(label_ele)
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.subplot(2, 3, 4)
        plt.scatter(range_list, data_select[label_x])
        plt.legend(label_x)
        plt.ylim(-0, 120)
        plt.ylabel(label_x)
        plt.title(label_x)
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.subplot(2, 3, 5)
        plt.scatter(range_list, data_select[label_y])
        plt.legend(label_y)
        plt.ylim(-20, 20)
        plt.xlim(0, 150)

        plt.ylabel(label_y)
        plt.xlabel(label_range)

        plt.title(label_y)
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.subplot(2, 3, 6)
        plt.scatter(range_list, data_select[label_z])
        plt.legend(label_z)
        plt.ylim(-8, 8)
        plt.ylabel(label_z)
        plt.xlabel(label_range)
        plt.title("z vs range")
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        # plt.figtext( 0.5, 0.95, "tgt3_id:" + str(num), ha="center", va="top", fontsize=16 )
        plt.savefig(fig_path + "/seq_" + str(num).format(3) + ".png")
        plt.close()


        plt.figure(figsize=(16, 16))

        plt.scatter(doppler_list, range_list)
        # plt.legend(label_z)
        plt.ylim(0, 180)
        plt.xlim(-40, 40)

        plt.ylabel(label_range)
        plt.xlabel(label_doppler)
        plt.title("range vs doppler")
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.savefig(fig_path + "/seq_" + str(num).format(3) + "_rdmap" + ".png")
        plt.close()
label_range = "range"
label_azm = "original_azimuth"
label_ele = "original_elevation"

label_power = "power"
label_doppler = "fixed_dopplers"


label_x = "x"
label_y = "y"
label_z = "z"


label_z = "z"
upper_folder_path = "/home/li/Programs/2944/dirac_front/csv_out_simple/"

sub_directories = [
    os.path.join(upper_folder_path, d)
    for d in os.listdir(upper_folder_path)
    if os.path.isdir(os.path.join(upper_folder_path, d))
]


if sub_directories:
    middle_folder_path = max(sub_directories, key=os.path.getctime)
    dir_name_part = middle_folder_path.split("/")
    bag_name_whole = dir_name_part[len(dir_name_part) - 1]
    bag_name_part = bag_name_whole.split(".")
    bag_name = bag_name_part[0]

# bag_name = "radar_camera_2023-09-15-13-59-35_0.bag_2023-09-15-16-43-36"

file_type_list = ["/point_file.csv"]
label_list = ["sequence"]



fig_upper_path = "./fig/" + bag_name
if not os.path.exists(fig_upper_path):
    os.mkdir(fig_upper_path)
else:
    shutil.rmtree(fig_upper_path)
    os.mkdir(fig_upper_path)

for n in np.arange(len(file_type_list)):
    file_name = file_type_list[n] 
    file_path = middle_folder_path + file_name

    fig_path = "./fig/" + bag_name 

    if not os.path.exists(fig_path):
        os.mkdir(fig_path)
    else:
        shutil.rmtree(fig_path)
        os.mkdir(fig_path)

    point_data = pd.read_csv(file_path)
    label_partition = label_list[n]

    unique_label_list = point_data[label_partition].unique()
    unique_count = point_data[label_partition].nunique()
    print(range(unique_label_list.size))

    input_list = []
    num_list = []
    for num in tqdm(unique_label_list):
        input_list.append([point_data, num, label_partition, fig_path])
        my_plot_func([point_data, num, label_partition, fig_path])

    # with multiprocessing.Pool() as pool:
    #     pool.map(my_plot_func, input_list)

    # with concurrent.futures.ThreadPoolExecutor(max_workers= 8) as executor:
    #     try:
    #         results = executor.map(my_plot_func, input_list)
    #     except:
    #         print("parallel loop failed")
