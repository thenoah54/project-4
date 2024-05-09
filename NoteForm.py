import datetime
from MakeNote import MakeNote
from tkinter import filedialog, messagebox
import os
import customtkinter
import json

class NoteForm(customtkinter.CTkToplevel):
    
    def __init__(self, master, notebook, notes): # initialize the new object
        super().__init__(master) # initialize it as a toplevel window

        self.geometry("2300+500") # set geometry
        self.title('Note Form') # set title
        # self.config(bg = 'light gray') # set color
        self.notes = notes # pass through notes variable
        self.notebook = notebook # pass through note book variable 
        
        # create note title entry field
        self.title_label = customtkinter.CTkLabel(self, text = 'Note Title:')
        self.title_label.grid(padx = 10, pady = 10, row = 1, column = 0, sticky = 'e')
        self.note_title = customtkinter.CTkEntry(self, width = 200, placeholder_text='New note title') # allows user to enter data
        self.note_title.grid(padx = 10, pady = 10, row = 1, column = 1, sticky = 'w')
        # self.note_title.insert(0, 'New note title') # adds default text (useful during development)
        
        # create note text entry field
        self.text_label = customtkinter.CTkLabel(self, text = 'Note Text:')
        self.text_label.grid(padx = 10, pady = 10, row = 2, column = 0, sticky = 'e')
        self.note_text = customtkinter.CTkTextbox(self, height = 100, width = 300) # allows user to enter data
        self.note_text.grid(padx = 10, pady = 10, row = 2, column = 1)
        self.note_text.insert("0.0", "Enter note") # adds default text (useful during development)
        
        # create note tags entry field
        self.tag_label = customtkinter.CTkLabel(self, text = 'Note tag:')
        self.tag_label.grid(padx = 10, pady = 10, row = 3, column = 0, sticky = 'e')
        self.note_tags = customtkinter.CTkEntry(self, width = 200, placeholder_text='Enter #tags, separated by commas') # allows user to enter data
        self.note_tags.grid(padx = 10, pady = 10, row = 3, column = 1, sticky = 'w')
        # self.note_tags.insert(0, 'Enter #tags, separated by commas') # adds default text (useful during development)
        
        # create note link entry field
        self.link_label = customtkinter.CTkLabel(self, text = 'Note link:')
        self.link_label.grid(padx = 10, pady = 10, row = 4, column = 0, sticky = 'e')
        self.note_link = customtkinter.CTkEntry(self, width = 200, placeholder_text='Insert link') # allows user to enter data
        self.note_link.grid(padx = 10, pady = 10, row = 4, column = 1, sticky = 'w')
        # self.note_link.insert(0, 'If there is a link with this note enter it here. Else, enter "None"') # adds default text (useful during development)
        
        self.author_label = customtkinter.CTkLabel(self, text = 'Author:')
        self.author_label.grid(padx = 10, pady = 10, row = 5, column = 0, sticky = 'e')
        self.note_author = customtkinter.CTkEntry(self, width = 200, placeholder_text='Insert author name') # allows user to enter data
        self.note_author.grid(padx = 10, pady = 10, row = 5, column = 1, sticky = 'w')
        # self.note_author.insert(0, "Insert Name") # adds default text (useful during development
        
        # create submit button
        submit_button = customtkinter.CTkButton(self, text = 'submit', command = self.submit) # submit buttons runs when this button is clicked
        submit_button.grid(padx = 10, pady = 10, row = 6, column = 1, sticky = 'w')
        
        
    # the submit button gets the metadata for the note and calls the MakeNote class to transform the the entered data into a new note object
    def submit(self):
        '''
        This method is run when the submit button is clicked.
        This first calculates the metadata from when the note is created.
        Then, this method gets all the data the user entered and adds it to a dictionary.
        The dictionary is passed to the MakeNote class to form the instance make_note which creates each note to be presented later to the user.
        This instance is then added to the notes variable.
    
        '''
        # calc metadata
        created = datetime.datetime.now() # get current dat and time
        local_now = created.astimezone() # shows the local time and the GMT offset
        local_tz = local_now.tzinfo # sets timezone 
        meta = f'created {created}, {local_tz}' # turns metadata into a string
        
        # get user input
        title = self.note_title.get() # extract user input from title section
        text = self.note_text.get('1.0', 'end').strip('\n') # extract user input from text section
        tag = self.note_tags.get() # extract user input from tags section
        link = self.note_link.get() # extract user input from link section
        meta = meta
        author = self.note_author.get()

        
        note_dict = {'title':title, 'text':text, 'link':link, 'tag':tag, 'meta':meta, 'author':author} # create the dictionary by creating key value pairs        
        make_note = MakeNote(note_dict) # pass the dictionary through to the creation of the MakeNote instance called make_note
        self.notes.append(make_note) # append the instance of the class to the notes variable
        self.notebook.append(make_note) # append the instance of the class to the notebook variable
        self.destroy() # destroy the window
        return note_dict # returns note_dict variable which is the dictionary
    