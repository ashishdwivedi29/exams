def selection_sort(a):
    for i in range(len(a)-1):
        min_index=i
        for j in range(i+1,len(a)):
            if a[min_index]>a[j]:
                min_index=j
        a[min_index],a[i]=a[i],a[min_index]


arr=[12,3,56,7,2,120,90]

selection_sort(arr)
print(arr)