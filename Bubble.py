def bubble(data):
    for i in range(len(data)):
        for j in range(1, len(data)):
            if data[j]<data[j-1]:
                temp = data[j]
                data[j]=data[j-1]
                data[j-1]=temp

data = [5,2,3,8,6,7,4,1,9,0]
bubble(data)
print(data)
