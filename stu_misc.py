
from math import sqrt

"""
    Stack Overflow - statistics about questions
"""

def average(lst):
    return (sum(lst) / len(lst))

def median(lst):
    lst.sort()
    return(lst[len(lst)//2])

def variance(lst):
    moy = average(lst)
    d = [(item - moy) ** 2 for item in lst]
    return (1/ (len(lst)-1)) * sum(d)

def std_deviation(lst):
    return sqrt(variance(lst))


"""
    Test
"""
#lst = [16,21,32,4,56,64,7,80,96,42,1024]
#print(average(lst))
#print(median(lst))
#print(variance(lst))
#print(std_deviation(lst))
