#DEF
L1 = [] #Emtpy list
L2 = [1, 2, 3, 4]
L3 = [1, 2, [3, 4]]

#INDEX / SLICE / LENGHT
L2[i][j]
L2[i:j]
len(L2)

L1 + L2 #Create new string object
L1 * L2 #Same but copy L2 to L1

for x in L2,   #Iteration
3 in L2        #Membership

L2.append(12)  #Add 12 to the end of L2
L2.sort()      #duh
L2.index(1),   #search for 
L2.reverse()   #duh
del L2[k]      #del number at k

range(4), xrange(0,4) #make list, tuple
