def linear_search (arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Element found at position",i+1)
            return i
        print("Element not found")

        arr = [10,20,30,40]
        key = 20
        linear_search(arr,key)


