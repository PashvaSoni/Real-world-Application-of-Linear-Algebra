"""

    Problem Statement : Steganography
    
    In simple term Steganography is a process of hiding the message in
    to an image .
    
    We will implement steganography with the help of binary image which 
    will take any type of string as input from known keyboard symbol, character 
    and numbers and palce it in 70*70 matrix and generate the binary image .
    
    Notice : ANY CHARACTER, SYMBOL, DIGITS FROM KEYBOARD ARE ALLOWED ( SPACE IS INCLUDED )
    
    I took 70*70 matrix because the total number of all character, symbol, and digit result 
    in to total 68 characters and 68 can be represented in binary by 7-bits , so we can 
    place 10-characters in one row.

"""

# Importing the packages 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import string
import collections  # specifically used for comparing the list elements .


# function which would return binary representaion of values in fixed sized format . 
def binary(value,size): 
    return(bin(value)[2:].zfill(size))


# For indexing : a-to-z  ==>  0001-to-11010 (binary indexing)
d = dict.fromkeys(string.ascii_lowercase, 0)


# Adding numbers to dictionary
d[' ']=26;  d['0']=27;  d['1']=28;  d['2']=29 # 26th index for space 
d['3']=30;  d['4']=31;  d['5']=32;  d['6']=33
d['7']=34;  d['8']=35;  d['9']=36 


# Adding symbols to dictionary
d['~']=37; d['!']=38; d['@']=39; d['#']=40;
d['$']=41; d['*']=42; d['(']=43; d[')']=44; d['_']=45;
d['-']=46; d['+']=47; d['=']=48; d['{']=49; d['[']=50;
d['}']=51; d[']']=52; d['|']=53; d['\\']=54; d[':']=55;
d[';']=56; d['\'']=57; d['"']=58; d['?']=59; d['/']=60;
d['.']=61; d['>']=62; d['<']=63; d[',']=64; d['`']=65;
d['%']=66; d['^']=67; d['&']=68;


# this for loop will assign each element to its binary numbers and place them into dictionary
count=1
for i in d:
    d[i]=str(binary(count,7)) 
    count+=1

d[' ']=binary(0,7)
d['a']=binary(1,7)
d['b']=binary(2,7)
print(d)


# for plotting the image on matplotlib
def plotter(images,titles,rows,column,label):
    plt.figure(label)  # for plotting multiple instance of matplotlib
    for i in range(len(images)):
        #images[i].setfheight(50)
        #images[i].setfwidth(50)
        plt.subplot(rows,column,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([])          # for removing the x ticks
        plt.yticks([])          # for removing the y ticks
    plt.show()


# for indexing purpose
d_list=list(d)
d_val=list(d.values())

# Generating the binary image of 70*70 (Approx 700 character can be stored) 
img=np.zeros((70,70,3),np.uint8)
ch=0 #choice varaible
while(ch!=3):
    ch=int(input('1) Encrypt message\n2) Decrypt message\n3) exit\nEnter your choice :'))

    if ch==1:
        
        # Taking the message from the user .
        msg=input("Enter the message :")
        
        # some varaibles used further .
        i,j=0,0
        color={ '1':[255,255,255] , '0':[0,0,0] }
        color_list=list(color)
        temp=0
        
        """ This function will covert each character of message into
        7-bit representation binary and place them into image matrix 
        where 0 indicates black colour and 1 indicate white color """
        while i<70:
            j=0
            while j<70:
                
                if(temp==len(msg)):   # this conditon will break the loop when the msg string is 
                    break             # completed .

                barr=d[msg[temp]]   # takes each character from msg and find the binary number in dictionary
  
                """ this for loop will take each bit from the barr and assign corresponding bit (0 or 1)
                to the corresponding pixel. if the bit is zero than color assign to that corresponding pixel
                is [0,0,0] and if the bit is 1 than that pixel is assigned [255,255,255]"""
                for k in barr:     
                    img[i,j]=color[ str(k) ]
                    j+=1
  
                temp+=1
            i+=1
        
        # for plotting the image using matplotlib
        images=[img]
        titles=['Message is encrypted here !']
        plotter(images,titles,1,1,1)
        
        save=input("Do you want to save the image ? [y/n]:").lower()
        if(save=='y'):
            filename=input("Enter the file name with correct 'EXTENSION' and 'ADDRESS' :")
            cv2.imwrite(filename, img) # function to save image (INBUILT)
            print("saved.....!")
    if ch==2:
         final='' # the final string that will contain the message

         str1=''  # this string is for appending the binary bits upto 7 bits .
         
         i=0; j=0; k=0
         """ opposite of the encrypted function """
         while i<70:
            j=0
            while j<70:
                for k in range(7):
                   
                    # this condition is to compare the list elements
                    if (collections.Counter(img[i,j]))==(collections.Counter([0,0,0])):
                        str1+='0'
                    else:
                        str1+='1'
                    j+=1

                # this line will find the correspondig character from the dictionary
                final+=(d_list[d_val.index(str1)])
                str1=''
            i+=1
         print("Decrypted message :",final)