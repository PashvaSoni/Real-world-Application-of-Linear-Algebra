"""
    Welcome TO My Encoder (Parshva's)

    Problem statement : Implementing Hill Chipher
    
    Hill Chipher is technique for encryption of the message .
    In this technique, the back bone for encoding and decoding of a 
    message string is done by a matrix whose inverse is either already 
    known or finded dynamically .
    
    In this program i have taken a matrix whose inverse was known to me 
    for making the program as simple as possible . But you can use some 
    inbuilt function such as :
                    
        numpy.linalg.inv(A)  where A is matrix whose inverse is needed
        numpy.linalg.det(A)  where A is matrix whose determinant is needed

    to determine the matrix inverse dynamically .

    You can try the following strings to know better about this program :
            1) helloworld
            2) HELLOWORLD
            3) @@@@

    Must watch the Movie " Imitation Game " for motivation .
    
"""
# Importing packages
import numpy as np
import string

# For indexing : a-to-z  ==>  1-to-26
d = dict.fromkeys(string.ascii_lowercase, 0)
count=0
for i in d:
    d[i]=count
    count+=1


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


# Coverting the Dictionary to list for getting keys from values and vica-versa
k=list(d.keys())  # k is a list which Conatins each alphabets 
v=list(d.values()) # v is a list which contains index of each alphabets

w=np.matrix([[1,2,3],
             [0,1,4],
             [5,6,0]
            ],float)   # matrix for encoding 

inv=np.matrix([ [-24,18,5],
                [20,-15,-4],
                [-5,4,1]],float)  # matrix for decoding


# 
def encrypter(A,msg):
    final_string=''
    # B matrix is the coversion msg into matrix form of 3*1 dimension
    B=np.matrix([ [d[msg[0]]],
                  [d[msg[1]]],
                  [d[msg[2]]] ],float)
    
    # Simple matrix multiplication
    C=A*B
    
    C=np.mod(C,[69]) # mod 69 needed because the answer should be between 0 to 69 which are present in dictionary
    
    # fetching the keys by use of values
    final_string+=(k[v.index(int(C[0]))]+k[v.index(int(C[1]))]+k[v.index(int(C[2]))])
    return final_string
# for making the choice .
ch=0
while(ch!=3):
    print("\nWelcome to Pms encoder.....!")
    ch=int(input('1) Encrypt message\n2) Decrypt message\n3) exit\nEnter your choice :'))
    if(ch==1):
        string=''
        final_string='' # string in which the encrypted string will be added
        final_string_decrypt='' # string in which the decrypted string will be added
        msg=input("Enter the message to encrypt (size<69):")
        
        # if the string is not in multiple of 3 letters 
        l=len(msg)
        
         # it is true if the message is 2 character less than multiple of 3 
        if(l%3==1):
            msg+="  " # so added 2 space
        
        #  it is true if the message is 1 character less than multiple of 3     
        if(l%3==2):
            msg+=" "  # so added 1 space
        
        # for encrypting the string at every 3 letter
        i=0
        while(i<len(msg)):
            string=msg[i:i+3]  # sending 3 charcter token of the string
            str1=encrypter(w, string.lower())
            final_string+=str1  # Adding to final string
            i+=3
        print(final_string)
        
        
    if(ch==2):
        string=''
        string1=input("Enter the message to decrypt :")
        i=0
        
        # for decrypting the string at every 3 letter 
        while(i<len(string1)):
            string=string1[i:i+3]
            str1=encrypter(inv, string.lower())
            final_string_decrypt+=str1
            i+=3
        print(final_string_decrypt)
        final_string_decrypt=''
