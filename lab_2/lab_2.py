def quicksort(lst): # log(N)

  pivot = lst[len(lst) - 1]

  i = 0

  for j in range(len(lst) - 1):

    if lst[j] < pivot:
      lst[i], lst[j] = lst[j], lst[i]
      i += 1

  lst[i], lst[len(lst)-1] = lst[len(lst)-1], lst[i]

  return lst
    

def find_three_numbers(lst, P):
    lst = quicksort(lst)  
    n = len(lst)
    
    for i in range(n - 2):  #O(N)
        left = i + 1
        right = n - 1
        
        while left < right: #O(N)
            current_sum = lst[i] + lst[left] + lst[right]
            
            if current_sum == P:
                return True  
            elif current_sum < P:
                left += 1  
            else:
                right -= 1  
    
    return False  


lst = [1, 2, 3, 6, 5, 7]
P = 15
result = find_three_numbers(lst, P)
print(result)  