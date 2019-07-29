import time 
import numpy as np
import math

def merge(a,b):    
    #print "Len a {}".format(len(a))
    #print "Len b {}".format(len(b))
    if len(a) == 0 and len(b) == 0:
        return []
    if len(a) == 0:   
        return [b[0]] + merge([], b[1:])
    if len(b) == 0:
        return [a[0]] + merge(a[1:],[])
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:],)
def merge_sort(n=[1,5,4,8,10,2,6,9,12,11,3,7,100,102, 19,23]):
    if len(n) == 1:
        return n
    if len(n) == 2:
        #print "Base case"
        if n[0] > n[1]:
            return [n[1],n[0]]
        else:
            return n  
    else:
        split = len(n)/2
        a = merge_sort(n[:split])
        b = merge_sort(n[split:])
        #print len(a)
        #print len(b)
        res = merge(a,b)
        return res
    

# 1ms 100

a = np.random.randint(1,99999999,900).tolist()    
t1 = time.time()
res = merge_sort(a)
t2 = time.time()
print "Elapsed_time {0} seconds".format(t2-t1)


