#For this proper microphone and access is required and also after pressing the button 2s wait time is required for processing(start speaking after 2s)
#Please install requirements from requirement.txt file

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
import speech_recognition as sr


#this fuction listens audio
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening Now")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Not Understood")
        messagebox.showinfo("Speech Recognition Error", "Speech not recognized. Please try again.")
        return None
    except sr.RequestError as e:
        print("Error: {0}".format(e))
        return None

#login button fuction
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Abhinav" and password == "12345":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# speech to text converter
def speech_to_text(entry_widget):
    recognized_text = recognize_speech()
    if recognized_text:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, recognized_text)

# main window
root = tk.Tk()
root.title("Livewire Login Page")
root.geometry("400x500")
root.configure(bg="#ffffff")

#image setting
image = Image.open("Livewire.png")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg="#ffffff")
image_label.image = photo
image_label.pack()
img = Image.open("microphone.png")
pic = ImageTk.PhotoImage(img)



# Username label 
username_label = tk.Label(root, text="Username:", bg="#ffffff", font=("Helvetica", 12))
username_label.pack()
username_entry = tk.Entry(root, font=("Helvetica", 12))
username_entry.pack()

# Speech to text button for username
speech_button_username = tk.Button(root, text="", image=pic, command=lambda: speech_to_text(username_entry))
speech_button_username.pack()

# Password label
password_label = tk.Label(root, text="Password:", bg="#ffffff", font=("Helvetica", 12))
password_label.pack()
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
password_entry.pack()

# Speech to text button for password
speech_button_password = tk.Button(root, text="", image=pic, command=lambda: speech_to_text(password_entry))
speech_button_password.pack()

# Login button
login_button = tk.Button(root, text="Login", command=login, font=("Helvetica", 14), bg="#4CAF50", fg="white")
login_button.pack(pady=10)

#loop
root.mainloop()
