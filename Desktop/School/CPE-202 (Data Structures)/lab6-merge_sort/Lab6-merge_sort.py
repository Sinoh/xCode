# Name: Jeffery Ho
# Section: 201 - 11

import random


# list of ints -> int
# takes in a list, sorts it, and returns the # of comparisions needed to sort the list
def insert_sort(alist):
   counter = 0
   for idx in range(1, len(alist)):
       cur = alist[idx]
       pos = idx
       counter += 1
       while (pos > 0 and alist[pos - 1] > cur):
           alist[pos] = alist[pos - 1]
           pos -= 1
           counter += 2
       counter += 1
       alist[pos] = cur
   counter += 1
   return counter  # selection sort


# list of ints -> int
# implements selection sort on a list of ints and returns the number of comparisons
def select_sort(alist):
   count = 0
   for i in range(len(alist) - 1, 0, -1):
       max_pos = 0
       count += 1
       for j in range(1, i + 1):
           count += 1
           if alist[j] > alist[max_pos]:
               count+=1
               max_pos = j
       count += 1
       temp = alist[i]
       alist[i] = alist[max_pos]
       alist[max_pos] = temp
   count+=1
   return count

# Merge Sort
# list of int -> int
# Given a list of number, sorts the list and returns the number of comparisons
def merge_Sort(alist, count = 0, left = 0, right = 0):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_Sort(lefthalf, count, left, right)
        merge_Sort(righthalf, count, left, right)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            count += 2
            if lefthalf[i] < righthalf[j]:
                count += 1
                alist[k]=lefthalf[i]
                i=i+1
            else:
                count += 1
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        count += 1
        while i < len(lefthalf):
            count += 1
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        count += 1
        while j < len(righthalf):
            count += 1
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        count += 1
    return count

alist = []

for i in range(1000):
    n=random.randint(0,100)
    alist.append(n)

print('merge:',merge_Sort(alist))
print('selection:', select_sort(alist))
print('insertion:', insert_sort(alist))
