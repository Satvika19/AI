def selectionSort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if(array[j]<array[min]):
                min = j
        temp = array[i]
        array[i]=array[min]
        array[min] = temp
    return array

array = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
 
    array.append(element)
     
print(selectionSort(array))
