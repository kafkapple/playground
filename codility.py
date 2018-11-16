# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:49:34 2018

@author: 2014_Joon_IBS
"""

def solution(A):
    a = list(set(A))
    len_d = len(a)
    a.sort()
        
    if a[-1]<0: #최대값이 음수면 무조건 1
        return 1
    elif len_d==1:
        if a[0]>=2:
            return 1
        else:
            return a[0]+1
    else:
        a=[i for i in a if i>=0]
        len_d = len(a)
        if a[0]>1:
            return 1
        else:
            for i in range(len_d-1):
                if a[i+1]-a[i] > 1:
                    if a[i]>=int(1e6): #최대값이면 더 증가 불가.
                        return int(1e6)
                    else:
                        return a[i]+1
            if a[-1]>=int(1e6):
                return int(1e6)
            else:
                return a[-1]+1
                
    # 음수 있으면 거긴 계산 패스하기. 효율성 위해.
    
        

def main():
    
    d1 = [1,3,5,5,1]
    d2= [100000000]
    d3 = [ -1,-3,5]
    d4 = [int(-1e5), int(7e10), 23, -3]
    d5=[-1,1,2,3]
    d6=[55255533]
    d7=[0,2,3,23,100,17,50,32]
    d8=[102,135,200,166]
    # 주의! sort 후 시작 점이 2 이상이면, 1이 답인데 그 뒤의 값 탐색 시작하게 되는 실수 오랫동안 저지름.
    
    data_list = [d1,d2,d3,d4,d5,d6,d7,d8]
    
    for i in data_list:
        result = solution(i)
        print(result)
        
if __name__=='__main__':
    main()