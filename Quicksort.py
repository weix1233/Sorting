def quicksort(array, start, end):
     if start>end:
          return
     pivot = array[start]
     left=start+1
     right = end
     #partitioning
     while left<=right:
          if array[left]>=pivot and array[right]<=pivot:
               temp = array[left]
               array[left] = array[right]
               array[right] = temp
               left+=1
               right-=1
          if array[left]<pivot:
               left+=1
          if array[right]>pivot:
               right-=1
     temp = array[start]
     array[start]=array[right]
     array[right]=temp
     #recursively call quicksort
     quicksort(array,start,right-1)
     quicksort(array,left,end)

arr=[5,2,3,8,6,7,4,1,9,0]
quicksort(arr,0,9)
print(arr)
