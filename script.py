#this script does make list of number of integers you enter and finds its sum
def listCreator(numberOfElements):
    L = [int(input('enter ['+str(i)+'] element:')) for i in range(numberOfElements)]
    return L
numberOfElements = int(input("Enter amount of elements:"))
L = listCreator(numberOfElements)
print('Amount of elements in L - ',len(L))
print('Sum of L = ',sum(L))
print(L)

