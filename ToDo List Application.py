#!/usr/bin/env python
# coding: utf-8

# Importing the required modules

# In[20]:


#import the required modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql


# In[21]:


#define an empty list
tasks = []


# Adding a Task to the list

# In[22]:


#define the function to add tasks to the list
def add_task():
    #getting the string from the entry field
    task_string = task_field.get()
    
    
    #check whether the string is empty or not
    if len(task_string) == 0:
        #display a message box with 'Empty Field' message
        messagebox.showinfo('Error','Field is Empty.')
        
        
    else:
        #add the string to the tasks list
        tasks.append(task_string)
        #use the execute() method to execute a SQL statement
        the_cursor.execute('insert into tasks values(?)',(task_string,))
        #calling the function to update the list
        list_update()
        #deleting the entry in the entry field
        task_field.delete(0,'end')


# Updating the list

# In[23]:


#define the function to update the list
def list_update():
    #call the function to clear the list
    clear_list()
    #iterating through the strings in the list
    
    for task in tasks:
        #using the insert() method to insert the tasks in the list box
        task_listbox.insert('end',task)


# Deleting a task from the list

# In[24]:


#define the function to delete a task from the list
def delete_task():
    #using the try-except method
    try:
        #getting the selected entry from the list box
        the_value = task_listbox.get(task_listbox.curselection())
        
        #checking if the stored value is present in the tasks list
        if the_value in tasks:
            #remove the tasks from the list
            task.remove(the_value)
            
            #call the function to update the list
            list_update()
            
            #use the execute() method to execute a SQL statement
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
            
    except:
        #displaying the message box with 'No Item Selected' message for an exception  
        messagebox.showinfo('Error','No Task Selected.Cannot Delete.')


# Deleting all the entries from the list

# In[25]:


#function to delete all tasks from the list
def delete_all_tasks():
    #display a message box to ask user for confirmation
    message_box = messagebox.askyesno('Delete All','Are you sure')
    
    #if the value turns to be True
    if message_box == True:
        
        #use the while loop to iterate through the tasks list until it is empty
        while (len(tasks)!=0):
            #use the pop() method to pop out the elements from the list
            tasks.pop()
            
            #use the execute() method to execute a SQL statement
            the_cursor.execute('delete from tasks')
            
            #call the function to update the list
            list_update()


# Clearing the list

# In[26]:


#define the function to clear the list
def clear_list():
    #using the delete method to delete all entries from the list box
    task_listbox.delete(0,'end')


# Closing the application

# In[27]:


#define the function to close the application
def close():
    #print the elements from the tasks list
    print(tasks)
    #use the destroy() method to close the application
    guiWindow.destroy()


# Retrieve data from the database

# In[28]:


#define the function to retrive data from the database
def retrieve_database():
    
    #use while loop to iterate through the elements in the tasks lists
    while(len(tasks)!=0):
        
        #use the pop() method to pop out the elements from the list
        tasks.pop()
        
        #iterate through the rows in the database base
        for row in the_cursor.execute('select title from tasks'):
            
            #use the append() method to insert the titles from the table to the list
            tasks.append(row[0])


# Creating the main window for the application

# In[29]:


# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = tk.Tk()
    
    # setting the title of the window  
    guiWindow.title("ToDo List")  
    
    # setting the geometry of the window  
    guiWindow.geometry("500x500+750+250")
    
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    
    # setting the background color to #FAEBD7  
    guiWindow.configure(bg = "#FAEBD7")  


# Adding the database to the application

# In[30]:


#use the connect() method to connect to the database
the_connection=sql.connect('listOfTasks.db')

#create an object of the cursor class
the_cursor = the_connection.cursor()

#use the execute() method to execute a SQL statement
the_cursor.execute('create table if not exists tasks (title text)')


# Adding the necessary widgets to the application and applying event triggers

# Frames

# In[31]:


#define the frames using the tk.Frame() widget
header_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
functions_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
listbox_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
  
#using the pack() method to place the frames in the application  
header_frame.pack(fill = "both")  
functions_frame.pack(side = "left", expand = True, fill = "both")  
listbox_frame.pack(side = "right", expand = True, fill = "both")  


# Labels

# In[32]:


#define the using the ttk.Label() widget
header_label = ttk.Label(
    header_frame,
    text = "ToDo List",
    font = ("Brush Script MT", "30"),
    background = "#FAEBD7",  
    foreground = "#8B4513"  
)

#use the pack() method to place the label in the application
header_label.pack(padx=20,pady=20)

#define another label using the ttk.Label() widget
task_label = ttk.Label(  
    functions_frame,  
    text = "Enter the Task:",  
    font = ("Consolas", "11", "bold"),  
    background = "#FAEBD7",  
    foreground = "#000000"  
)

#using the place() method to place the label in the application  
task_label.place(x = 30, y = 40)  


# Entry Field

# In[33]:


#defining an entry field using the ttk.Entry() widget  
task_field = ttk.Entry(  
    functions_frame,  
    font = ("Consolas", "12"),  
    width = 18,  
    background = "#FFF8DC",  
    foreground = "#A52A2A"  
)

#using the place() method to place the entry field in the application  
task_field.place(x = 30, y = 80)  


# Buttons

# In[34]:


#adding buttons to the application using the ttk.Button() widget  
add_button = ttk.Button(  
    functions_frame,  
    text = "Add Task",  
    width = 24,  
    command = add_task  
)


del_button = ttk.Button(  
    functions_frame,  
    text = "Delete Task",  
    width = 24,  
    command = delete_task  
)  


del_all_button = ttk.Button(  
    functions_frame,  
    text = "Delete All Tasks",  
    width = 24,  
    command = delete_all_tasks  
)  


exit_button = ttk.Button(  
    functions_frame,  
    text = "Exit",  
    width = 24,  
    command = close  
)  


#using the place() method to set the position of the buttons in the application  
add_button.place(x = 30, y = 120)  
del_button.place(x = 30, y = 160)  
del_all_button.place(x = 30, y = 200)  
exit_button.place(x = 30, y = 240)  


# List box

# In[35]:


#defining a list box using the tk.Listbox() widget  
task_listbox = tk.Listbox(  
    listbox_frame,  
    width = 26,  
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)


#using the place() method to place the list box in the application  
task_listbox.place(x = 10, y = 20)  


# Calling the functions

# In[36]:


#calling some fuctions
retrieve_database()
list_update()

#using the mainloop() method to run the application
guiWindow.mainloop()

#establishing the connection with database
the_connection.commit()
the_cursor.close()


# In[ ]:




