def linear_search_recursive(arr, target, index=0): 
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

def setup():
    arr = []
    n = int(input("How many elements are therte in the array?"))
    for i in range(n):
        element = int(input("enter the element"))
        arr.append(element)
    key = int(input("what to search?"))
    result = linear_search_recursive(arr,key)
    if result == -1:
        print("unfortunately the element is not found in the given array :(")
    else:
        print(f"element founded at {result+1} position")
    print("//karan singh ghugtyal,2202302530023")
if __name__ == "__main__":
    setup()