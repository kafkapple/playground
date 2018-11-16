# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:30:03 2018

@author: 2014_Joon_IBS
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# minus font 깨지는 문제 관련
mpl.rcParams['axes.unicode_minus']=False

# sample data

import numpy as np
data = np.random.randint(-100,100,50).cumsum()

#
plt.plot(range(50),data,'r')
plt.title('시간별')
plt.ylabel('가격')
plt.xlabel('시간')

print ('버전: ', mpl.__version__)
print ('설치 위치: ', mpl.__file__)
print ('설정 위치: ', mpl.get_configdir())
print ('캐시 위치: ', mpl.get_cachedir())
font_path = mpl.matplotlib_fname()

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# ttf 폰트 전체개수
print(len(font_list))
font_list[:10]
print(font_list)

result = [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Na' in f.name]
print(mpl.get_cachedir())
print(result)

# 하나씩 설정

# fname 옵션을 사용하는 방법
#path = '/Library/Fonts/NanumBarunpenRegular.otf'
fontprop = fm.FontProperties(fname=path, size=18)

plt.plot(range(50), data, 'r')
plt.title('시간별 가격 추이', fontproperties=fontprop)
plt.ylabel('주식 가격', fontproperties=fontprop)
plt.xlabel('시간(분)', fontproperties=fontprop)
plt.show()

# 전체 설정

print('# 설정되어있는 폰트 사이즈')
print (plt.rcParams['font.size'] ) 
print('# 설정되어있는 폰트 글꼴')
print (plt.rcParams['font.family'] )

# serif, sans-serif, monospace
print('serif 세리프가 있는 폰트--------')
print (plt.rcParams['font.serif']) 
print('sans-serif 세리프가 없는 폰트 --------')
print (plt.rcParams['font.sans-serif']) 
print('monospace 고정폭 글꼴--------')
print (plt.rcParams['font.monospace'])

plt.rcParams["font.family"] = 'Nanum Brush Script OTF'
plt.rcParams["font.size"] = 20
plt.rcParams["figure.figsize"] = (14,4)
plt.plot(range(50), data, 'r')
plt.title('시간별 가격 추이')
plt.ylabel('주식 가격')
plt.xlabel('시간(분)')
plt.style.use('seaborn-pastel')
plt.show()
