from tkinter import *
import cv2
import pytesseract



def extract(path):
    textwindow=Tk()
    textwindow.configure(bg="#4B0082")
    # textwindow = Toplevel(ro)
    textwindow.title("Text in image")
    textwindow.geometry("300x450")

    eimg = cv2.imread(path)
    # seimg = cv2.resize(eimg,(200,300))
    # Image_ht, Image_wd, Image_thickness = Sample_img.shape
    seimg = cv2.cvtColor(eimg,cv2.COLOR_BGR2RGB)
    texts = pytesseract.image_to_data(seimg)
    # print(texts)
    mytext=""
    prevy=0
    for cnt,text in enumerate(texts.splitlines()):
        if cnt==0:
            continue
        text = text.split()
        if len(text)==12:
            x,y,w,h = int(text[6]),int(text[7]),int(text[8]),int(text[9])
            if(len(mytext)==0):
                prevy=y
            if(prevy-y>=10 or y-prevy>=10):
                print(mytext)
                Label(textwindow, text=mytext, font=('Times', 15, 'bold'),bg="#ADA96E").pack()
                mytext=""
            mytext = mytext + text[11]+" "
            prevy=y
    Label(textwindow, text=mytext, font=('Times', 15, 'bold'),bg="#ADA96E").pack()