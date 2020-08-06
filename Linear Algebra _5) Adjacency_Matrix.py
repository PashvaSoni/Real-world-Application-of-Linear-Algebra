"""
    Problem Statment : Understanding of Adjacency Matrix 
    
    In graph theory and computer science, an adjacency matrix is a square
    matrix used to represent a finite graph. 
    The elements of the matrix indicate whether pairs of vertices are 
    adjacent(connected) or not in the graph.
    
    FOR EXAMPLE : We are told that their are 6 friends in the tution and 
                 and we want to analyse the connectio among this friends.
                 This can be done by genrating the adjacency matrix formed
                 by the connection between this friends .
    
    NOTE : FOR BETTER UNDERSTANDING OF THIS PROGRAM FIRST RUN THE PROGRAM
           AND SEE THE CODE OF THIS PROGRAM .
"""
# importing packages
import numpy as np
import matplotlib.pyplot as plt

# Naming each person for proper understanding
names={'0':'parshva','1':'mitesh','2':'umesh','3':'sidhraj','4':'meet','5':'rajvi'}
n_key=list(names.keys())
n_val=list(names.values())

""" Their are totsl 6 friends in the example so their should be 6 rows
     and 6 column of the adjacency matrix
"""
adj=np.matrix([[0,0,0,1,1,1],
               [0,0,0,1,1,0],
               [0,0,0,0,0,1],
               [1,1,0,0,0,0],
               [1,1,0,0,0,0],
               [1,0,1,0,0,0]],np.uint8)

print("Here is an exapmle of 6 friends :\n",names)
print("The connection between them is shown by the adjacency matrix :")
print(adj)
ch=0
while ch!=5:
    print('\n1) Find who is connected to whom ?\n2) Find Mutual friends \n3) Change the adjacency matrix\n4) Plot the adjacency matrix\n5) exit')
    ch=int(input("Enter your choice :"))

    # 1st choice will tell who is connected to whom ... !
    if ch==1:
        print("\n\n'===>' indicates that person1 is friend of person2 and vica-versa :")
        for i in range(len(adj)):
            print("\nFriend list of :",names[str(i)])
            for j in range(len(adj)):
                if(adj[i,j]>0):
                    print(names[str(i)],'===>',names[str(j)])
            print("________________________________")
    
    # 2nd choice will tell who is mutually connectedd to whom ...!
    """
        In adjacency matrix we can find the mutual relationship just by squaring the adjacency matrix
    """
    if ch==2:
        print("Friends list :",names)
       
        # squaring the matrix to find the mutually related friends
        mat=adj*adj
        print(mat)
     
        for i in range(len(mat)):
            print("_____________________________________________________________________")
            print("Mutual friend list of ",names[str(i)])
            for j in range(len(mat)):
                if(i==j):   # this condition says that the person is mutually related to itself so just pass it
                    pass
                if(int(mat[i,j])>0 and i!=j): # this will take in who many ways they are connected mutually
                    print(names[str(i)],' becomes the mutual friend of ',names[str(j)],'in ',mat[i,j],' ways .')
    
    # 3rd choice is to change the adjacency matrix if required ...!
    if ch==3:
        n=int(input("Enter the total no of friends or nodes :")) # for knowing the size of adjacency matrix 
        names.clear()
        print("\n===> Enter the name of each friend 'one-by-one' :")

        # for taking the names of new friendlist
        for i in range(n):
            str1=input("\nEnter the name of friend or node :")
            names[str(i)]=str1.lower()

        print("\n",names)
        n_key=list(names.keys())
        n_val=list(names.values())

        # creating new matrix of size of new friendlist
        adj=np.zeros((n,n))

        # for taking the inputs of new adjacency matrix
        for i in range(n):
            print("\n______________________________________________")
            print("Enter the name of people who are friend of ",names[str(i)])
            for j in range(n):
                t=input("Enter the 'friend_name' -> OR <- 'end' for finishing :").lower()
                if(t=='end'):
                    print("_________________________________________________\n")
                    break
                j=n_val.index(t)
                adj[i][j]=adj[j][i]=1
        print(adj)
    
    # for plotting the adjaceny matrix on matplotlib for analysis .
    if ch==4:
        plt.matshow(adj)
        plt.colorbar()
        plt.title('matrix')
        plt.show()