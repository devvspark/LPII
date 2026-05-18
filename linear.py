# Linear Search Program

arr = [10, 25, 30, 45, 50]

target = int(input("Enter number to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
