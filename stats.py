import math

# Given a list L, return the average (mean) of the numbers in L
# If L is empty, return None.
def mean(L):
    sum = 0
    if not L: 
       return None
    for i in range(len(L)):
       sum += L[i]
    return sum/len(L)

# Given a list L, return the standard deviation of the numbers in L
def std(L):
    if len(L) == 0 or len(L) == 1:
       return None
    sumSquare = 0
    for i in range(len(L)):
        sumSquare += pow(L[i] - mean(L), 2)
    return math.sqrt(sumSquare/(len(L) - 1))

# Given a list L, remove any numbers which are more than sd standard
# deviations awayfrom the mean of the list and return the updated list.
# For this function, assume that sd is an int and is greater than 0
def remove_outliers(L, sd):
    sd = std(L)
    newList = []
    for i in range(len(L)):
        if L[i] <= sd:
           newList.insert(len(newList), L[i]) 
    return newList

# Given two lists L1 and L2, return the t-test statistic for the two lists
def t_test(L1, L2):
    meanSub = mean(L1)-mean(L2)
    p1 = pow(std(L1), 2)/len(L1)
    p2 = pow(std(L2), 2)/len(L2)
    addSqrt = math.sqrt(p1 + p2)
    
    return meanSub / addSqrt

