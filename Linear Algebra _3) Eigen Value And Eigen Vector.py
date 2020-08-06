"""

The problem statment :
    
    Suppose the school is attacked by zombies and their is no way to go out of
    the school so the population humans and Zombie remains constatnt .
    Now let say that every 1 hour 20% of humans are converted into zombies due 
    to infection .
    Their is also a cure for the infection but it not guaranteed so every hour
    10% of zombies are cured and converted to humans .
    
    If you are given that their are 150-humans and 150-zombies what is going to
    happen at the long run ?
"""

# importing packages :
import numpy as np
import matplotlib.pyplot as plt
import time
# declaring the varibles 
humans=150      # current humans population
zombies=150     # current zombies population
 
f_humans=0      # future humans population
f_zombies=0     # future humans population

"""
  As we know 20% humans are converted to zombies every hour, that means 80% of 
  humans will remain as humans and also 10% of zombies are converted in to
  humans thus total humans becomes :
              
                          humans = 0.8(humans) + 0.1(zombies)
                         
  Similarly for zombie we have 20% of humans which are converted into zombie
  and 10% of zombie are converted into humans which meaans 90% remains zombie
  so total population of zombie becomes :
  
                         zombies = 0.2(humans) + 0.9(zombies)
  
    So we can write the above 2 equation in this form matrix form as :
        
                    | 0.8   0.1 |  *   | humans  |  =  | Future_humans |
                    | 0.2   0.9 |      | zombies |  =  | Future_zombies|

"""

A=np.matrix( [ [0.8 , 0.1],
               [0.2 , 0.9]  ], float )

B=np.matrix([ [humans],
              [zombies]  ], float )

C=np.matrix([ [f_humans],
              [f_zombies]  ], float)


n=int(input("Enter the number of hours to analyse :"))

x=[] # for plotting humans on grafh on x-axis 
y=[] # for plotting zombies on grafh on y-axis
labels=[]

# for performing matrix operations
for i in range(n):      
    labels.append(i)    # for plotting purpose
    x.append(B[0])      # appending the values of humans in x list for plotting
    y.append(B[1])      # appending the values of zombie in y list for plotting
    print("Humans =",B[0]," Zombies =",B[1])
    C = A * B
    B=C

# for finding the range of values possible for plotting on grafh
x_max= max(x)
y_max= max(y)

plt.plot(0,0,'ok') #<-- plot a black point at the origin
plt.axis('equal')  #<-- set the axes to the same scale
plt.xlim(0,x_max) #<-- set the x axis limits
plt.ylim(0,y_max) #<-- set the y axis limits
plt.grid(b=True, which='major') #<-- plot grid lines
plt.xlabel("humans") # for labeling x-axis
plt.ylabel("zombie") # for labeling y-axis


for i in range(len(y)):
 
    x_val=[0,x[i]]   
    y_val=[0,y[i]]   # for plotting multiple lines on same grafh
    plt.plot(x_val,y_val)
    plt.legend(labels) # for naming each line uniquely

plt.show()    
    
"""

    In output you would see that the vector are going towards [100,200] 
    which is the "MULTIPLE" of one of eigen vector for the matrix A which
    are [0.5 , 1] and [-1 , 1] and the eigen values are 1 and 7/10 .
    
    This shows that the equilibrium of the above case is, after some hours
    humans will remains 100 and zombies will remain 200 

    Thus Eigen vector and Eigen value as their unique application in such
    thing where equilibrium of the model is to be found for example:
        --> How dieases will spread .
            and similar kind of analysis can be done .
    
    
"""

