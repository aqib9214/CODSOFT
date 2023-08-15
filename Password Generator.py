#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the required modules
import random
import pyperclip
from tkinter import *
from tkinter.ttk import Combobox


# In[2]:


def generate_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    length = var1.get()
    password = ''.join(random.choice(characters) for i in range(length))
    return password


# In[3]:


#define the function to copy the password to clipboard
def copy_to_clipboard():
    password = entry.get()
    pyperclip.copy(password)


# In[4]:


def generate_and_display_password():
    password = generate_password()
    entry.delete(0, END)
    entry.insert(0, password)


# In[5]:


root = Tk()
root.title("Password Generator")


# In[6]:


# Labels and entry
Random_password = Label(root, text="Password")
Random_password.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)


# In[7]:


# Copy button
copy_button = Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=2, column=2)


# In[8]:


# Generate button
generate_button = Button(root, text="Generate", command=generate_and_display_password)
generate_button.grid(row=4, column=2)


# In[9]:


# Radio buttons for password strength
var = IntVar()
radio_low = Radiobutton(root, text="Low", variable=var, value=0)
radio_low.grid(row=6, column=3, sticky="W")
radio_medium = Radiobutton(root, text="Medium", variable=var, value=1)
radio_medium.grid(row=7, column=3, sticky="W")
radio_strong = Radiobutton(root, text="Strong", variable=var, value=2)
radio_strong.grid(row=8, column=3, sticky="W")
var.set(1)  # Set Medium as default strength


# In[10]:


# Combobox for password length
var1 = IntVar()
combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.grid(column=4, row=4)


# In[11]:


# Start the GUI
root.mainloop()

