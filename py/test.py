# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:46:58 2018

@author: 2014_Joon_IBS
"""


import matplotlib.pyplot as plt

print('test')

fig_size=(10,4)

ylim_max=10
fig, ax = plt.subplots(figsize=fig_size)#figsize=(10,4))
    
ax.set(title = 'ttttOFL',
      ylabel='freezing(%)',
      xlabel='(min)',
      ylim=[0,ylim_max])

ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


fig.tight_layout()
fig.savefig('test.png', transparent = True, dpi=200)
fig.show()
       