import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from sklearn.metrics import accuracy_score, f1_score,precision_score, recall_score 
from sklearn.neighbors import KernelDensity
import pandas as pd
import numpy as np

def data_visualization_non(df):
    #normal datapoints
    df_normal = df.loc[(df['data_label'] == 0)]
    df_normal = df_normal.set_index('time')
    df_normal = df_normal.reset_index()
    # Outlier datapoints
    df_outlier = df.loc[(df['data_label'] == 1)]
    df_outlier = df_outlier.set_index('time')
    df_outlier = df_outlier.reset_index()
    #plotting
    plt.rcParams['figure.figsize'] = (11, 7)
    fig, ax = plt.subplots(1,1)
    fig.patch.set_facecolor('white')
    Normal = ax.scatter(df_normal['time'],df_normal['height'], c ="black", marker="o", s = 10**1.25)
    Outlier = ax.scatter(df_outlier['time'],df_outlier['height'], c ="red",marker ="o", s = 10**1.25)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 1.5)
    ax.set_title('River Muringato Data (Non-uniform Regime)', fontsize=18, weight='bold')
    ax.set_xlabel('Time', fontsize=18, weight = 'bold')
    ax.set_ylabel('Water level (m)', fontsize=18, weight = 'bold')
    ax.set_xlim(['2022-04-26 00:00:01'],['2022-05-17 23:59:59'])
    ax.set_ylim(0,2)
    ax.set_xticklabels(df['time'], fontsize=16, weight='bold')
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x',which='major', labelsize=16)
    ## Define the date format
    date_form = DateFormatter("%d-%m")
    ax.xaxis.set_major_formatter(date_form)
    ax.legend(["Normal", "Outlier"], loc ="upper left", fancybox=True,facecolor='#01FFFF',prop={'size': 15,  'style': 'normal'})
    ax.set(facecolor = "white")
    plt.show()
    
def data_visualization_u(df):
    #normal datapoints
    df_normal = df.loc[(df['data_label'] == 0)]
    df_normal = df_normal.set_index('time')
    df_normal = df_normal.reset_index()
    # Outlier datapoints
    df_outlier = df.loc[(df['data_label'] == 1)]
    df_outlier = df_outlier.set_index('time')
    df_outlier = df_outlier.reset_index()
    #plotting
    plt.rcParams['figure.figsize'] = (11, 7)
    fig, ax = plt.subplots(1,1)
    fig.patch.set_facecolor('white')
    Normal = ax.scatter(df_normal['time'],df_normal['height'], c ="black", marker="o", s = 10**1.25)
    Outlier = ax.scatter(df_outlier['time'],df_outlier['height'], c ="red",marker ="o", s = 10**1.25)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 1.5)
    ax.set_title('River Muringato Data (uniform Regime)', fontsize=18, weight='bold')
    ax.set_xlabel('Time', fontsize=18, weight = 'bold')
    ax.set_ylabel('Water level (m)', fontsize=18, weight = 'bold')
    ax.set_xlim(['2022-03-06 00:00:01'],['2022-03-26 23:59:59'])
    ax.set_ylim(0,2)
    ax.set_xticklabels(df['time'], fontsize=16, weight='bold')
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x',which='major', labelsize=16)
    ## Define the date format
    date_form = DateFormatter("%d-%m")
    ax.xaxis.set_major_formatter(date_form)
    ax.legend(["Normal", "Outlier"], loc ="upper left", fancybox=True,facecolor='#01FFFF',prop={'size': 15,  'style': 'normal'})
    ax.set(facecolor = "white")
    plt.show()

def data_visualization_result_u(df):
    #normal datapoints
    df_normal = df.loc[(df['kde_label'] == 0)]
    df_normal = df_normal.set_index('time')
    df_normal = df_normal.reset_index()
    # Outlier datapoints
    df_outlier = df.loc[(df['kde_label'] == 1)]
    df_outlier = df_outlier.set_index('time')
    df_outlier = df_outlier.reset_index()
    #plotting
    plt.rcParams['figure.figsize'] = (11, 7)
    fig, ax = plt.subplots(1,1)
    fig.patch.set_facecolor('white')
    Normal = ax.scatter(df_normal['time'],df_normal['height'], c ="black", marker="o", s = 10**1.25)
    Outlier = ax.scatter(df_outlier['time'],df_outlier['height'], c ="red",marker ="o", s = 10**1.25)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 1.5)
    ax.set_title('Kde output for the Uniform data', fontsize=18, weight='bold')
    ax.set_xlabel('Time', fontsize=18, weight = 'bold')
    ax.set_ylabel('Water level (m)', fontsize=18, weight = 'bold')
    ax.set_xlim(['2022-03-06 00:00:01'],['2022-03-26 23:59:59'])
    ax.set_ylim(0,2)
    ax.set_xticklabels(df['time'], fontsize=16, weight='bold')
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x',which='major', labelsize=16)
    ## Define the date format
    date_form = DateFormatter("%d-%m")
    ax.xaxis.set_major_formatter(date_form)
    ax.legend(["Normal", "Outlier"], loc ="upper left", fancybox=True,facecolor='#01FFFF',prop={'size': 15,  'style': 'normal'})
    ax.set(facecolor = "white")
    plt.show()
    
    
def histogen(w):
    data_samples = np.array(w)
    plt.rcParams['figure.figsize'] = (11, 7)
    plt.hist(data_samples, 20, edgecolor = 'Red');
    plt.title('Distribution of data samples',fontsize=15,weight = 'bold')
    plt.xlabel(r'$bins$', fontsize=15)
    plt.ylabel('Counts', fontsize=15)
    plt.tick_params(axis='both',labelsize=16,)
    plt.tick_params(axis = 'x', labelsize = 16,)
    #plt.yscale("log")
    plt.grid(True)
    plt.show()
    
def window(df, h_band,q):
    surprise_threshold = 0
    data_win = list(df.height)
    data_labels = list(df.data_label)
    window_size_list = np.arange(5,q,5,dtype=int)
    clusters_dic = {}
    for i in window_size_list:
        win_list = []
        for indx in range(0,len(data_win)-i,i):
            data_int = data_win[indx:indx+i]
            win_list.append(data_int)
        win_list = np.array(win_list)
        surprise_list = []
        clusters =[]
        for element in win_list:
            kde = KernelDensity(kernel="gaussian", bandwidth = h_band).fit(element.reshape(-1, 1))
            surprise = -kde.score_samples(element.reshape(-1, 1))
            surprise_list.append(surprise.tolist())
        sup_tup = tuple(surprise_list)
        surprise_concat = np.concatenate(sup_tup).tolist()
        #print(len(surprise_concat))
        for ii in surprise_concat:
            if ii < surprise_threshold:
                cluster = 0
            else:
                cluster = 1
            clusters.append(cluster)
        clusters_dic[str(i)] = clusters
    precision_scores = []
    accuracy_scores = []
    recall_scores = []
    f1_scores = []
    for key in clusters_dic:
        kde_labels = clusters_dic[key]
        data_precision_score = precision_score(data_labels[:len(kde_labels)],kde_labels)
        data_accuracy_score = accuracy_score(data_labels[:len(kde_labels)],kde_labels)
        data_f1_score = f1_score(data_labels[:len(kde_labels)],kde_labels)
        data_recall_score = recall_score(data_labels[:len(kde_labels)],kde_labels)

        precision_scores.append(data_precision_score)
        accuracy_scores.append(data_accuracy_score)
        recall_scores.append(data_recall_score)
        f1_scores.append(data_f1_score)
    k = np.argmax(recall_scores)
    g = window_size_list[k]
    fig, ax = plt.subplots(1,1)
    fig.patch.set_facecolor('white')

    Precision = ax.plot(window_size_list,precision_scores, color='y', linewidth=2)
    Accuracy = ax.plot(window_size_list,accuracy_scores, color='m', linewidth=2)
    Recall = ax.plot(window_size_list,recall_scores, color='c', linewidth=2)
    F1_scores = ax.plot(window_size_list,f1_scores, color='r', linewidth=2)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.8)
    ax.set_title('Window Size vs Metric', fontsize=18)
    ax.set_xlabel('Window Size', fontsize=18, weight = 'bold')
    ax.set_ylabel('Performance Metric', fontsize=18, weight = 'bold')
    ax.set_ylim(-.1, 1.1)
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x',which='major', labelsize=16)

    ## Define the date format
    date_form = DateFormatter("%d-%m")
    ax.legend(["Precision", "Accuracy", "Recall", "F1_score"], loc ="lower right", fancybox=True,facecolor='#FFFFFF',prop={'size': 15,   'style': 'normal'})
    ax.set(facecolor = "white")
    plt.rcParams['figure.figsize'] = (15, 9)
    plt.show()
    print('check out window size :',g)
        
def bandwidth_test(b):
    x = [21.370, 19.435, 20.363, 20.632, 20.404, 19.893, 21.511, 19.905, 22.018, 19.93, 31.304, 32.286, 28.611, 29.721, 29.866, 30.635, 29.715, 27.343, 27.559, 31.32, 39.693, 38.218, 39.828, 41.214, 41.895, 39.569, 39.742, 38.236, 40.460, 39.36, 50.455, 50.704, 51.035, 49.391, 50.504, 48.282, 49.215, 49.149, 47.585, 50.0]
    value_test = np.array(x)
    kde_model = KernelDensity(kernel="gaussian", bandwidth = b).fit(value_test.reshape(-1, 1))
    data_sample_plot = np.linspace(np.min(value_test),np.max(value_test),100)
    log_density = kde_model.score_samples(data_sample_plot.reshape(-1, 1))

    plt.hist(value_test, 20, edgecolor = 'black', density=True);
    plt.title(' Effect of bandwidth on KDE estimator', fontsize=18)
    plt.xlabel(' Data Samples', fontsize=18)
    plt.ylabel(r'$\hat{f}_{WL}(x)$', fontsize=18)
    plt.plot(data_sample_plot, np.exp(log_density), color = 'r', linewidth=4)
    plt.show()
    
    
def dailymean_plot(df):
    #plotting
    plt.rcParams['figure.figsize'] = (9, 6)
    fig, ax = plt.subplots(1,1)
    fig.patch.set_facecolor('white')
    ax.plot(df['time'],df['Data'], c ="black", linewidth=4)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 1.5)
    ax.set_title('River Muringato water level Data (2021) ', fontsize=18, weight='bold')
    ax.set_xlabel('Time', fontsize=18, weight = 'bold')
    ax.set_ylabel('Water level (m)', fontsize=18, weight = 'bold')
    ax.set_xlim(['2021-02-19 00:00:00'],['2021-12-02 23:59:59'])
    ax.set_ylim(0,2)
    ax.set_xticklabels(df['time'], fontsize=16, weight='bold')
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x',which='major', labelsize=16)
    ## Define the date format
    date_form = DateFormatter("%d-%m")
    ax.xaxis.set_major_formatter(date_form)
    ax.set(facecolor = "white")
    plt.show()
    
    

        