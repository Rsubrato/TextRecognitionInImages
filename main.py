from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pytesseract
import imgtext as im
import imgextract as ie


pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'

ro = Tk()
ro.configure(bg="#4B0082")
ro.title('Text Recognition In Images')
ro.geometry("700x750")
ro.maxsize(700,750)
sb = Scrollbar(ro)
sb.pack( side = RIGHT, fill = Y )
# mylist = Listbox(ro, yscrollcommand = sb.set )
# newline= Label(ro)
uploaded_img=Label(ro)

def changeOnHover(button, colorOnHover, colorOnLeave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def show_extract_button(path):

    extractBtn= Button(ro,text="Extract text", command=lambda:im.extract(path), bg="green", fg="black", height=2, width=20, font=('Times', 15,))
    extractBtn.pack(pady=20)
    changeOnHover(extractBtn, "#CCFFFF", "green")

    extractBtn1 = Button(ro, text="Extract image", command=lambda: ie.extract1(path), bg="green", fg="black", height=2,
                        width=20, font=('Times', 15,))
    extractBtn1.pack(pady=20)
    changeOnHover(extractBtn1, "#CCFFFF","green")

    # extractBtn2 = Button(ro, text="New", command=lambda: up(path) , bg="green", fg="black", height=2,
    #                      width=20, font=('Times', 15,))
    # extractBtn2.pack(pady=20)


def upload():
    try:
        path = filedialog.askopenfilename()
        # print(path)
        image = Image.open(path)
        image = image.resize((500, 450), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image = img
        uploaded_img.pack()
        show_extract_button(path)
    except:
        pass



# upload_btn = Button(text="Home", command=home, bg="green", fg="black", height=2, width=20, font=('Times', 15))
# upload_btn.pack(pady=10)


upload_btn = Button(text="Upload an image", command=upload, bg="green", fg="black", height=2, width=20, font=('Times', 15))
upload_btn.pack(pady=10)
changeOnHover(upload_btn,"#CCFFFF","green")


ro.mainloop()




