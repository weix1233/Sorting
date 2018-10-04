def insertion(data):
    for i in range(1,len(data)):
        j=i-1
        key = data[i]
        #shift stuff down then insert
        while j>=0 and key<data[j]:
            data[j+1]=data[j]
            j-=1
        data[j+1]=key
     
a=[5,2,7,6,3,1,4,8]
insertion(a)
print(a)
