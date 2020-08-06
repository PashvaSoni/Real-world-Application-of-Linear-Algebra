'''
As we all know that images are matrices with M*N*3 dimension were M and N are 
its resolution dimensions and 3 represents the BGR color respectively 
i.e blue=0 , green=1, red=2
We will perform some fun experiments on images ________  !
'''
#Importing the pakages
import cv2      
import numpy as np
import matplotlib.pyplot as plt

# function to plot histogram in matplotlib
def histplotter(images,labels,rows,column,label):
    plt.figure(label)  # for plotting multiple instance of matplotlib
    for i in range(len(images)):
        plt.subplot(rows,column,i+1)
        plt.plot(images[i])
        plt.title(labels[i])
    plt.show()


#function to plot images on matplotllib .
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


#--------------------------------------------------------------

""" For plotting diffrent channels (BGR) """

# Reading the image
'''Here imread() takes 2 arguments :
    1) Path of the image
    2) Flag=0 if we want to grayscale image, 
       Flag=1 for color image,
       Flag=-1 for including alpha channel, with color image .
''' 
img=cv2.imread('parshva_1.jpg',1) 

# resize() is used to resize the image .
img=cv2.resize(img, (720,720))


# Separating Each BGR channels  
blue, green, red = img[:,:,0], img[:,:,1], img[:,:,2]   # M*N*3 dimension

# for labeling each image separately 
images=[img,blue,green,red]
titles=['original image','Blue Channel','Green Channel','Red Channel']

# for plotting each image separately (Diffrent Channels)
plotter(images,titles,2,2,1) # rows=2, column=2,label=1

# Now plotting the histogram of each channel .     # [0,255] range to plot
hist_B=cv2.calcHist(img,[0], None, [256], [0,255]) # [0] for the channel [BGR]
hist_G=cv2.calcHist(img,[1], None, [256], [0,255]) # None for mask(we don't need)
hist_R=cv2.calcHist(img,[2], None, [256], [0,255]) # [256]=histogram_size

# preparing the list and labels
img_hist=[hist_B,hist_G,hist_R]
hist_labels=['Blue Channel Histogram','Green Channel Histogram','Red Channel Histogram']

histplotter(img_hist, hist_labels, 3, 1, 3)

#---------------------------------------------------------------

""" For plotting diffrent filter """

# Reading the image
pic=cv2.imread('no plate 2.png',1)
pic=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY) # changing it to grayscale
pic=cv2.resize(pic, (720,480))

# Applying the thresolding
th1=cv2.adaptiveThreshold(pic,60,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 3)

# Applying canny edege dection
edj=cv2.Canny(pic,200, 100)

# Applying Morphological dilation
kernel = np.ones((5,5), np.uint8)
dil=cv2.dilate(pic, kernel,3)

# preparinf the list of images and labels
imgs=[pic,th1,edj,dil]
ts=['original','Thresolded INV','Canny Edge Detector','Morphological Dilation']

# plotting each images 
plotter(imgs, ts, 2, 2,2)

#---------------------------------------------------------------
