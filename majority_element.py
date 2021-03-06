"""
PEDAC
Problem: Given an array of size n, find the majority element. The majority element is the element that appears more than n / 2 times.
Assume the array is non-empty and major element is there.
Example:  Input:[3,2,3] Output: 3
          [2,2,1,1,1,2,2] Output : 2

Data: List
Algorthim:
1: Create a count to count how much times a number appears {}
2: Loop through array
3: add the index and the value as key-value pairs
4: return the 



"""

def majority_element(n):
  counter = {}
  for i in n:
    if i in counter:
      counter[i] += 1 
    else:
      counter[i] = 1
  for i in counter:
    if counter[i] > len(n) / 2:
      return i
  
ar = [3,2,3]
ar2 = [2,2,1,1,1,2,2]
print(majority_element(ar))
print(majority_element(ar2))