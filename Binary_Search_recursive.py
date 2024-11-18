array = []
def binary_Search(key,low,high):
    if low > high:
        return -1
    mid = (low + high) // 2  # Use integer division
    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return binary_Search(key, low, mid - 1)
    else:
        return binary_Search(key, mid + 1, high)
    
def initial_Setup():
    n = int(input("How many elements are therte in the array?"))
    print("Remember to enter the array in sorted manner !")
    for i in range(n):
        element = int(input("enter the element"))
        array.append(element)
    key = int(input("what to search?"))
    low = 0
    result = binary_Search(key,low , len(array)-1)
    if result == -1:
        print("unfortunately the element is not found in the given array :(")
    else:
        print(f"element founded at {result+1} position")
    
    
if __name__ == "__main__":
    initial_Setup()


