import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
from matplotlib.ticker import MaxNLocator

# import multiprocessing
import concurrent.futures

os.sched_setaffinity(0, range(8))


def my_plot_func(liset_struct):
    tgt3_data = liset_struct[0]
    num = liset_struct[1]
    label_id = liset_struct[2]
    fig_path = liset_struct[3]
    tgt3_selected_by_id = tgt3_data[tgt3_data[label_id] == num & tgt3_data[label_id]]
    seq = tgt3_selected_by_id["sequence"]
    # print(tgt3_data.columns)

    if seq.size > 10:
        # flag_start = 0
        # cnt = seq[0]
        # i_start  = seq[0]
        # i_current = seq[0]
        # for i in range(seq.size):
        plt.figure(figsize=(16, 12))
        plt.subplot(2, 2, 1)
        plt.scatter(seq, tgt3_selected_by_id[label_rx])
        plt.scatter(seq, tgt3_selected_by_id[label_rx_flt])
        plt.ylim(-10, 10)
        plt.ylabel("rx")
        plt.legend(["rx", "rx_flt"])
        plt.title("RX Comparison")
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.subplot(2, 2, 3)
        plt.scatter(seq, tgt3_selected_by_id[label_vx])
        plt.scatter(seq, tgt3_selected_by_id[label_vx_flt])
        plt.ylim(-5, 5)
        plt.ylabel("vx")
        plt.legend(["vx", "vx_flt"])
        plt.title("VX Comparison")
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.subplot(2, 2, 2)
        plt.scatter(seq, tgt3_selected_by_id[label_ry])
        plt.scatter(seq, tgt3_selected_by_id[label_ry_flt])
        plt.legend(["ry", "ry_flt"])
        plt.ylim(-80, 10)
        plt.ylabel("ry")
        plt.title("RY Comparison")
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.subplot(2, 2, 4)
        plt.scatter(seq, tgt3_selected_by_id[label_vy])
        plt.scatter(seq, tgt3_selected_by_id[label_vy_flt])
        plt.legend(["vy", "vy_flt"])
        plt.ylim(-0, 20)
        plt.ylabel("vy")
        plt.title("VY Comparison")
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.figtext(
            0.5, 0.95, "tgt3_id:" + str(num), ha="center", va="top", fontsize=16
        )
        plt.savefig(fig_path + "/glb_id_tgt3_" + str(num).format(3) + ".png")
        plt.close()


def my_plot_func_single(liset_struct):
    tgt3_data = liset_struct[0]
    num = liset_struct[1]
    label_id = liset_struct[2]
    fig_path = liset_struct[3]
    tgt3_selected_by_id = tgt3_data[tgt3_data[label_id] == num & tgt3_data[label_id]]
    seq = tgt3_selected_by_id["sequence"]
    seq_array = pd.Series.to_numpy(seq)
    ry_array = pd.Series.to_numpy(tgt3_selected_by_id[label_ry])
    rx_array = pd.Series.to_numpy(tgt3_selected_by_id[label_rx])

    # print(tgt3_data.columns)
    if (
        seq.size > 20
        # and np.max((seq_array[1 : seq.size - 1]) - (seq_array[0 : seq.size - 2])) < 20
        and np.min(ry_array) < -6
        and np.max(np.abs(rx_array)) < 10
    ):
        # flag_start = 0
        # cnt = seq[0]
        # i_start  = seq[0]
        # i_current = seq[0]
        # for i in range(seq.size):
        plt.figure(figsize=(16, 12))
        plt.subplot(2, 2, 1)
        plt.plot(seq, tgt3_selected_by_id[label_rx])
        plt.ylim(-5, 5)
        plt.ylabel("rx")
        plt.title("RX Comparison")
        plt.grid("major")
        plt.yticks(np.arange(-5, 5, step=0.5))
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.subplot(2, 2, 2)
        plt.plot(seq, tgt3_selected_by_id[label_vx])
        plt.ylim(-2, 2)
        plt.ylabel("vx")
        plt.title("VX Comparison")
        plt.grid("minor")
        plt.yticks(np.arange(-2, 2, step=0.2))

        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.subplot(2, 2, 3)
        plt.plot(seq, tgt3_selected_by_id[label_ry])
        plt.ylim(-80, 10)
        plt.ylabel("ry")
        plt.title("RY Comparison")
        plt.grid("major")
        plt.yticks(np.arange(-80, 10, step=10))
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.subplot(2, 2, 4)
        plt.plot(seq, tgt3_selected_by_id[label_vy])
        plt.ylim(-0, 20)
        plt.ylabel("vy")
        plt.title("VY Comparison")
        plt.grid("minor")
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        plt.figtext(
            0.5, 0.95, "tgt3_id:" + str(num), ha="center", va="top", fontsize=16
        )
        plt.savefig(fig_path + "/glb_id_tgt3_" + str(num).format(3) + ".png")
        plt.close()


label_vx = "vx"
label_vy = "vy"
label_vx_flt = "vx_flt"
label_vy_flt = "vy_flt"

label_rx = "rx"
label_ry = "ry"
label_rx_flt = "rx_flt"
label_ry_flt = "ry_flt"

upper_folder_path = "/home/li/Programs/CornerRadar/dirac/csv_out_pf/"

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

file_type_list = ["/rear_right/track_file.csv", "/rear_left/track_file.csv", "/fusion_file.csv"]
radar_type_list = ["/rear_right", "/rear_left", "/fusion"]
label_id_list = ["glb_trk_id", "glb_trk_id", "fusion_id"]



fig_upper_path = "./fig/" + bag_name
if not os.path.exists(fig_upper_path):
    os.mkdir(fig_upper_path)
else:
    shutil.rmtree(fig_upper_path)
    os.mkdir(fig_upper_path)

for n in np.arange(len(file_type_list) - 1):
    file_name = file_type_list[n] 
    file_path = middle_folder_path + file_name

    fig_path = "./fig/" + bag_name + radar_type_list[n]

    if not os.path.exists(fig_path):
        os.mkdir(fig_path)
    else:
        shutil.rmtree(fig_path)
        os.mkdir(fig_path)

    tgt3_data = pd.read_csv(file_path)
    label_id = label_id_list[n]
    gld_id_select = 256

    unique_id_list = tgt3_data[label_id].unique()
    unique_count = tgt3_data[label_id].nunique()
    print(range(unique_id_list.size))

    input_list = []
    num_list = []
    for num in unique_id_list:
        input_list.append([tgt3_data, num, label_id, fig_path])
        my_plot_func_single([tgt3_data, num, label_id, fig_path])

    # with multiprocessing.Pool() as pool:
    #     pool.map(my_plot_func, input_list)

    # with concurrent.futures.ThreadPoolExecutor(max_workers= 8) as executor:
    #     try:
    #         results = executor.map(my_plot_func, input_list)
    #     except:
    #         print("parallel loop failed")
