# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:24:19 2018

@author: 2014_Joon_IBS
"""
import math

def find_digit(target):
    count = 1
    i=1
    while(True):
        i_c = math.ceil(i/2)-1
        #print(i, i_c)
        cur_count = 9*10**(i_c)
        count+=cur_count
        print(i,cur_count, count)
        
        if count>=target:
            print('here!: {}'.format(i))
            return i, count-cur_count
        else:
            i+=1
        
def find_pal(n_digit, cum_count, target):
    diff_count = target-cum_count-1
    
    if n_digit<3:
        return str(diff_count+1)*n_digit    
    else:
        result = 10**(math.ceil(n_digit/2)-1) + diff_count
        if n_digit%2==0:
            return str(result)+str(result)[::-1]
        else:
            partial = str(result)[:-1]
            return partial+ str(result)[-1] + partial[::-1]
        
        
    
def main():
    n =20# int(input()) #자릿수
    n_digit, cum_count = find_digit(n)
    
    result = find_pal(n_digit, cum_count, n)
    print(result)
    
    
if __name__=='__main__':
    main()
    