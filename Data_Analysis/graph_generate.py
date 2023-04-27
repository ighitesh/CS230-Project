import os
import csv

bimodal_data = []
gshare_data = []
perceptron_data = []

l1i = 'L1I AVERAGE MISS LATENCY'
l1d = 'L1D AVERAGE MISS LATENCY'
l2c = 'L2C AVERAGE MISS LATENCY'
llc = 'LLC AVERAGE MISS LATENCY'

for new_files, old_files in zip(os.scandir('results_new'), os.scandir('results_old')):
    filename = str(new_files)[11:-2]
    split_name = filename.split("-")
    trace_type = split_name[0]
    bp_type = split_name[2]
    policy = split_name[3:7]
    l1i_tmp = []
    l1d_tmp = []
    l2c_tmp = []
    llc_tmp = []
    with open('results_old/' + filename) as curr_file:
        for line in curr_file:
            if l1d in line:
                l1d_tmp.append(line[26:-7])
            if l1i in line:
                l1i_tmp.append(line[26:-7])
            if l2c in line:
                l2c_tmp.append(line[26:-7])
            if llc in line:
                llc_tmp.append(line[26:-7])
    with open('results_new/' + filename) as curr_file:
        for line in curr_file:
            if l1d in line:
                l1d_tmp.append(line[26:-7])
            if l1i in line:
                l1i_tmp.append(line[26:-7])
            if l2c in line:
                l2c_tmp.append(line[26:-7])
            if llc in line:
                llc_tmp.append(line[26:-7])
    if bp_type == "bimodal":
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1d', 'old', l1d_tmp[0]])
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1d', 'new', l1d_tmp[1]])
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1i', 'old', l1i_tmp[0]])
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1i', 'new', l1i_tmp[1]])
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'l2c', 'old', l2c_tmp[0]])
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'l2c', 'new', l2c_tmp[1]])
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'llc', 'old', llc_tmp[0]])
        bimodal_data.append(['bimodal', trace_type, policy[0], policy[1], policy[2], policy[3], 'llc', 'new', llc_tmp[1]])
    if bp_type == "gshare":
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1d', 'old', l1d_tmp[0]])
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1d', 'new', l1d_tmp[1]])
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1i', 'old', l1i_tmp[0]])
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1i', 'new', l1i_tmp[1]])
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'l2c', 'old', l2c_tmp[0]])
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'l2c', 'new', l2c_tmp[1]])
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'llc', 'old', llc_tmp[0]])
        gshare_data.append(['gshare', trace_type, policy[0], policy[1], policy[2], policy[3], 'llc', 'new', llc_tmp[1]])
    if bp_type == "perceptron":
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1d', 'old', l1d_tmp[0]])
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1d', 'new', l1d_tmp[1]])
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1i', 'old', l1i_tmp[0]])
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'l1i', 'new', l1i_tmp[1]])
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'l2c', 'old', l2c_tmp[0]])
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'l2c', 'new', l2c_tmp[1]])
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'llc', 'old', llc_tmp[0]])
        perceptron_data.append(['perceptron', trace_type, policy[0], policy[1], policy[2], policy[3], 'llc', 'new', llc_tmp[1]])

with open('data.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(bimodal_data)
    writer.writerows(gshare_data)
    writer.writerows(perceptron_data)


