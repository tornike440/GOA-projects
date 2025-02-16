def positive_sum(arr):
    sum_poss=[]
    for i in range (0,len(arr)):
        if arr[i]>0:
            sum_poss.append(arr[i])
    return sum(sum_poss)