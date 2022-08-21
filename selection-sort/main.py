
#selection sort

arr = [3, 2, 1]

for i in range(len(arr)):
     minor = i

     for j in range(i + 1, len(arr)):
         if arr[j] < arr[minor]:
             minor = j
         if arr[i] != arr[minor]:
            aux = arr[i]
            arr[i] = arr[minor]
            arr[minor] = aux

print(arr)




