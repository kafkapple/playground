# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:49:46 2018

@author: 2014_Joon_IBS
"""

import pandas as pd
import numpy as np
import glob
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats
import matplotlib.pyplot as plt

#os.chdir('e:')
#path='/0Temp_data/20180911_OFL_after_tube_n3_batch1/'
#os.chdir(path)

#name = 'freeze_20180911_OFL_after_tube_n3_batch1'
bar_width = .5

params = {
   'axes.labelsize': 8,
   'font.size': 18,
   'legend.fontsize': 10,
   'legend.frameon':False,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'text.usetex': False,
   'figure.figsize': [4, 6] # instead of 4.5, 4.5
   }

plt.rcParams.update(params)


def color_setting(n_color=2):
    sns.set_style('whitegrid')
    sns.set_color_codes()
    
    ###### customize color palette
    flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
    beach_towel = ['#fe4a49', '#2ab7ca', '#fed766', '#e6e6ea', '#f4f4f8']
    pastel_rainbow = ['#a8e6cf','#dcedc1','#ffd3b6','#ffaaa5', '#ff8b94']
                      
    list_palette = [flatui,
                 beach_towel,
                 pastel_rainbow]                      
    
    if n_color <=3:  # color 종류 별로 안써도 되는 경우
        for i, i_p in enumerate(list_palette):
            list_palette[i] = i_p[::2]  #홀수 값만 취함. 
    
    #### 
    sns.set_palette('hls',n_color) # Reds
    sns.set_palette(list_palette[2], n_color)
    current_palette = sns.color_palette()
    #sns.palplot(current_palette)
    ###
    sns.set_context('poster', font_scale=0.8)
    return current_palette

def legend_patch(current_palette, labels):
    patches = []
    for i, _ in enumerate(labels):
        patch_i = mpatches.Patch(color=current_palette[i], label=labels[i])
        patches.append(patch_i)
    return patches

def plot_time_series(data):
    columns = []
    ofl_bin = 9
    columns = np.arange(ofl_bin)+1
    
    #test = pd.DataFrame(data = data, columns=columns)
    
    fig2, ax2 = plt.subplots()#figsize=(10,4))
    sns.set_style('ticks',rc = {"lines.linewidth":0.1,"xtick.major.size": 0.1, "ytick.major.size": 1})
    g = sns.catplot(
                #palette={"male": "g", "female": "m"},
                markers=["^"], linestyles=["-"],linewidth=0.1,
                kind="point", data=data, ci=68, ax=ax2, aspect=0.5, scale=0.5)
    
    ax2.set(title = 'OFL',
          ylabel='freezing(%)',
          xlabel='(min)',
          ylim=[0,20])
    
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    for l in g.ax.lines:
        print(l.get_linewidth())
        plt.setp(l,linewidth=5)
        
def plot_bar_scatter(data, p, current_palette, labels):
      
    patches = legend_patch(current_palette, labels)   # to add legend
   
    fig, ax = plt.subplots( figsize=(5,5))
    
    sns.barplot(data=data, ci=68, errwidth = 2, capsize=.05, ax= ax)
    sns.stripplot(data=data, jitter=True, size= 7,  
                  edgecolor = 'gray', linewidth=1, ax=ax)#,color="0.4")
    ax.grid(False)
    
    ax.set(title = 'Social rank vs OFL',
          ylabel='avg OFL (%)',
          #xlabel='trial',
          ylim=[0,30])
    
    ax.legend(handles = patches, loc='best', edgecolor =None, fontsize=13, bbox_to_anchor=(0.7,0.7)) # upper right
    #ax.axis('equal')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    change_width(ax, bar_width) # bar_width
    add_star(ax, p, df)
    
    fig.tight_layout()
    fig.savefig('test.png', transparent = True, dpi=300)


def stars(p):
   if p < 0.0001:
       return "****"
   elif (p < 0.001):
       return "***"
   elif (p < 0.01):
       return "**"
   elif (p < 0.05):
       return "*"
   else:
       return "-"

def t_test(x,y):
    # normality test. p>0.05 means fail
    _, p_x = stats.shapiro(x)
    _, p_y = stats.shapiro(y)
    # equal variance test. p <=0.05 means fail
    _, p_var = stats.levene(x,y) 
    
    if (p_x or p_y > 0.05) or p_var <=0.05 :  # normality fail
        print('Non-parametric test is needed. MannWhitney U test.\n')
        statistic, p_final = stats.mannwhitneyu(x,y, alternative='two-sided')
    else:
        print('T-test\n')
        statistic, p_final = stats.ttest_ind(x,y)
        
    print('Result. Statistic: {}\n p-value: {}'.format(statistic, p_final))
    return statistic, p_final
    
def data_vec(data):  # convert Pandas dataframe into vectors
    n_category = len(data.keys())
    d_list = [0 for i in range(n_category)]
    legend=[]
    for i, i_key in enumerate(data.keys()):
        d_list[i] = np.array(data[i_key])
        d_list[i] = d_list[i][np.isnan(d_list[i])==False]  # remove NaN
        print('n = {}'.format(len(d_list[i])))
        legend.append(i_key + ' \n(n={})'.format(len(d_list[i])))
    return d_list, legend

def data_ofl_read(path):
    csv_file = glob.glob(path+'*.csv')[0]
    print(csv_file)
    df = pd.read_csv(csv_file)

    # OFL time bin 만큼 추출
    time_bin = 9
    df = df.iloc[:, 0:time_bin+1]
    
    # pandas 로 csv read 시, 기본 key 탐색 (첫번째 row)
    key_subject = df.keys()[0]
    
    obs = df[df[key_subject].str.contains("dem|Onset|Duration")==False]  # dem, onset, duration 중 하나라도 포함되어 있으면 제외 -> obs 데이터만 추출 가능
    dem = df[df[key_subject].str.contains("dem")==True]  # dem data
    return obs, dem    

def add_star(ax, p_value, df):
    
    y_max = np.max(np.array(df.max()))
    y_min = np.min(np.array(df.min()))
    s = stars(p_value)
    print(s)
    ax.annotate("", xy=(0, y_max), xycoords='data',
               xytext=(1, y_max), textcoords='data',
               arrowprops=dict(arrowstyle="-", ec='black',#'#aaaaaa',
                               connectionstyle="bar,fraction=0.2"))
    
    # fig size 5 -> 
    p = 'p = {:.2f}'.format(p_value)
    ax.text(0.5, y_max + abs(y_max - y_min)*0.3, s,
           horizontalalignment='center',
           verticalalignment='center')
    
    ax.text(0.5, y_max + abs(y_max - y_min)*0.05, p,
           horizontalalignment='center',
           verticalalignment='center')

def change_width(ax, new_value):
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)


if __name__ == '__main__':
    name = '/python/data/dom_sub.xlsx'
    df = pd.read_excel(name)
    #obs, dem = data_ofl_read()
    
    current_palette = color_setting(2) # 2 종류 plot 준비
    
    ## Statistics. T-test 
    d_list, legend = data_vec(df)
    x = d_list[0]
    y = d_list[1]
    
    _, p = t_test(x,y)
    
    plot_bar_scatter(df, p, current_palette, legend) # bar scatter plot
    
    path_ofl = '/python/data/ofl/'
    obs, dem = data_ofl_read(path_ofl)
    plot_time_series(obs)
    #obs.rename(lambda x: x[1:], axis='columns')
    obs.set_axis(['a', 'b', 'c', 'd', 'e'], axis='columns', inplace=False)
    
    
    
    
    

    
