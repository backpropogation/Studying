#this script does make list of number of integers you enter and finds its sum
def listCreator():
    L = [int(input('enter ['+str(i)+'] element:')) for i in range(int(input("ENter the number of elements:")))]
    return L

L = listCreator()

print('Amount of elements in L - ',len(L))
print('Sum of L = ',sum(L))
print(L)


