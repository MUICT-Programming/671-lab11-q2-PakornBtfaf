# YOUR CODE HERE
n = int(input())
lst1=[]
lst2=[]
up_lst=[]
def summation(n):
    for i in range(n):
        list1=int(input())
        lst1.append(list1)
    for i in range(n):
        list2=int(input())
        lst2.append(list2)
        up_lst.append(lst1[i]+lst2[i])
    return up_lst
def find_min_or_max(up_lst):
    min_value=min(up_lst)
    max_value=max(up_lst)
    return min_value,max_value
print(summation(n))
print(find_min_or_max(up_lst))
