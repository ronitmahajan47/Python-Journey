#Merge sorting

myList = []
size = int(input("\nEnter the size of list : "))

for i in range(size):
    myList.append(int(input(f"Enter DATA {i + 1} = ")))

print("\nList before sorting : ",myList)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


myList = merge_sort(myList) 
print("List after sorting : ", myList)