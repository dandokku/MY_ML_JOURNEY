def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        
        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
            
        else: 
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 2, 223, 12, 342, 42, 31, 41, 53, 123, 83, 32, 65, 34, 61] #binary search only works when the list is sorted

print(binary_search(my_list, 42))


# EXERCISES
# 1.1 Suppose you have a sorted list of 128 names, and you’re searching 
# through it using binary search. What’s the maximum number of 
# steps it would take?
# 1.2 Suppose you double the size of the list. What’s the maximum 
# number of steps now?
