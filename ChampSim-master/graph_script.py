import os

branch_predictors = ['bimodal', 'gshare', 'perceptron']
prefetcher = {'l1i' : ['next_line', 'no'], 'l1d' : ['next_line', 'no'], 'l2c' : ['next_line', 'no'], 'llc' : ['next_line', 'no']}

for bp in branch_predictors:
    for l1i_pref in prefetcher['l1i']:
        for l1d_pref in prefetcher['l1d']:
            for l2c_pref in prefetcher['l2c']:
                for llc_pref in prefetcher['llc']:
                    os.system("./build_champsim.sh " + bp + " " + l1i_pref + " " + l1d_pref + " " + l2c_pref + " " + llc_pref + " lru 1")
                    for traces in os.scandir('dpc3_traces'):
                        os.system("./run_champsim.sh " + bp + "-" + l1i_pref + "-" + l1d_pref + "-" + l2c_pref + "-" + llc_pref + "-lru-1core 1 10 " + str(traces)[11:-2])