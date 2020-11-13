
def binary_search(l,inf, sup, x):
    corte = (sup + inf)  // 2
    print(inf, sup, corte)
    m = l[corte]
    print(l[inf:sup+1])
    
    if sup >= inf:
        if x == m:
            return corte
        if( x < m ):
            return binary_search(l, inf, corte-1,  x)
        else:
            return binary_search(l, corte+1, sup,  x)
    else:
        return -1
    
def binary_search_it(l, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

l = [1,5,7,45,89,110, 345, 456, 897, 1233]
x = binary_search(l, 0, len(l)-1,  1)
print("--", x)