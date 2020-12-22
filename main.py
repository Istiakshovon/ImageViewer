from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewer")

my_img0 = ImageTk.PhotoImage(Image.open("index.jpeg"))
my_img1 = ImageTk.PhotoImage(Image.open("index1.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("index2.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("index3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("index4.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("index5.jpeg"))

image_list = [my_img0, my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img0)
my_label.grid(row=0, column=0, columnspan=3)

state = Label(root, text="Image 1 of "+str(len(image_list)), bd=1, relief=SUNKEN)
state.grid(row=2, column=0,columnspan=3, sticky=W+E)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    button_back.grid_forget()
    button_forward.grid_forget()

    my_label = Label(image=image_list[image_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))


    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)

    state = Label(root, text="Image "+str(image_number)+" of "+str(len(image_list)), bd=1, relief=SUNKEN)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    state.grid(row=2, column=0,columnspan=3, sticky=W+E)


def backward(image_number):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()

    my_label = Label(image=image_list[image_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    state = Label(root, text="Image "+str(image_number)+" of "+str(len(image_list)), bd=1, relief=SUNKEN)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    state.grid(row=2, column=0,columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command= backward, state=DISABLED)
buttonExit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
buttonExit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)

root.mainloop()
