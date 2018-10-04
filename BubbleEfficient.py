def bubbleEfficient(data):
    noswaps=False
    while noswaps==False:
        noswaps=True
        for j in range(1,len(data)):
            if data[j]<data[j-1]:
                temp = data[j]
                data[j]=data[j-1]
                data[j-1]=temp
                noswaps=False
data = [5,2,3,8,6,7,4,1,9,0]
bubbleEfficient(data)
print(data)
