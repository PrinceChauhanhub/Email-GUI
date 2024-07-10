import smtplib
from tkinter import *
from tkinter import messagebox

def send_message():
    try:
        sender_info = sender_address.get()
        password_info = password.get()
        address_info = address.get()
        email_body_info = email_body.get("1.0", END)

        # Email validation can be added here
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_info, password_info)
        print("Login successful")
        server.sendmail(sender_info, address_info, email_body_info)
        print("Message sent")

        messagebox.showinfo("Success", "Message sent successfully")
        
        sender_address_entry.delete(0, END)
        password_entry.delete(0, END)
        address_entry.delete(0, END)
        email_body.delete("1.0", END)
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send message: {str(e)}")

gui = Tk()
gui.geometry("500x500")
gui.title("Email Sender App")
gui.configure(background="#f0f8ff")  # AliceBlue background color

heading = Label(text="Email Sender App", bg="#4682b4", fg="white", font="Helvetica 16 bold", width="500", height="3")  # SteelBlue background color
heading.pack()

Label(text="Sender's Email:", bg="#f0f8ff", fg="#4682b4", font="Helvetica 12").place(x=15, y=70)
sender_address = StringVar()
sender_address_entry = Entry(textvariable=sender_address, width="30")
sender_address_entry.place(x=15, y=100)

Label(text="Sender's Password:", bg="#f0f8ff", fg="#4682b4", font="Helvetica 12").place(x=15, y=140)
password = StringVar()
password_entry = Entry(textvariable=password, width="30", show='*')
password_entry.place(x=15, y=170)

Label(text="Recipient Email:", bg="#f0f8ff", fg="#4682b4", font="Helvetica 12").place(x=15, y=210)
address = StringVar()
address_entry = Entry(textvariable=address, width="30")
address_entry.place(x=15, y=240)

Label(text="Message:", bg="#f0f8ff", fg="#4682b4", font="Helvetica 12").place(x=15, y=280)
email_body = Text(width="30", height="5")
email_body.place(x=15, y=320)

button = Button(gui, text="Send Message", command=send_message, width="30", height="2", bg="#4682b4", fg="white")
button.place(x=15, y=400)

mainloop()
