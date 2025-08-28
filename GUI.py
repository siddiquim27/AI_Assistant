from tkinter import*
from PIL import Image , ImageTk
import speech_to_text
import action


root = Tk()
root.title("Noman's Assistant")
root.geometry("600x675")
# root.resizable(False, False)
root.config(bg="#6F8FAF")


#ask funtion
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END , 'User--->'+ user_val+ "\n")
    if bot_val != None:
        text.insert(END,"BOT<---"+ str(bot_val)+ "\n")

    if bot_val == "Okay sir":
        root.destroy()


def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END , 'User--->'+ send+ "\n")
    if bot != None:
        text.insert(END,"BOT<---"+ str(bot)+ "\n")
    if bot == "Okay sir":
        root.destroy()


def delete():
    text.delete('1.0' , "end")


#FRAME

frame = LabelFrame(root, padx = 100, pady = 10, borderwidth= 10 , relief="raised")
frame.config(bg= "#6F8FAF")
frame.grid(row= 0 , column= 1 , padx= 10, pady=10)

#text label

text_label= Label(frame, text="NOMAN'S ASSISTANT", font=("Comic Sans MS ", 14 , "bold") , fg="#356696")
text_label.grid(row= 0 , column= 0 , padx= 20 , pady= 10)


#image
image = ImageTk.PhotoImage(Image.open("image.png"))
image_label = Label(frame , image= image)
image_label.grid(row=1 , column= 0 , padx= 10, pady =20)

# adding a text widget

text = Text(root , font=('courior 10 bold') , bg="#356696")
text.grid(row =3 , column= 0, padx= 20, pady=  2)
text.place(x= 280 , y = 590 , width= 500 , height= 100)


#entry visit

entry = Entry(root , justify=CENTER)
entry.place(x = 350 , y=700 , width= 350, height= 25)

#button 1
Button1 = Button(root , text= "ASK" , bg="#356696" , pady= 16 , padx= 40, borderwidth=10 , relief= SOLID, command= ask)
Button1.place(x= 110 , y =750 )

#button 2
Button2 = Button(root , text= "Send" , bg="#356696" , pady= 16 , padx= 40, borderwidth=10 , relief= SOLID, command= send)
Button2.place(x= 780 , y =750 )

 #button 3
Button3 = Button(root , text= "delete" , bg="#356696" , pady= 16 , padx= 40, borderwidth=10 , relief= SOLID, command= delete)
Button3.place(x= 450 , y =750 )




root.mainloop()
