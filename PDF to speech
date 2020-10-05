# -*- coding: utf-8 -*-

# you will need 2 python libraries 
#1. pyttx3
#2. PyPDF2

import pyttsx3
import PyPDF2

book=open('your pdf file location','rb')

pdfreader=PyPDF2.PdfFileReader(book)

pages=pdfreader.numPages
#print(pages)
#select the page number that you want python program to narrate
page=pdfreader.getPage(30)

text=page.extractText()

speaker=pyttsx3.init()

speaker.say(text)

speaker.runAndWait()
