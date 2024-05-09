import datetime
from MakeNote import MakeNote
from tkinter import filedialog, messagebox
import os
import customtkinter
import json


class Snippet():
    def __init__(self, notes, notebook, note):
        self.notes = notes # pass through notes variable
        self.notebook = notebook # pass through note book variable
        # self.note_text = self.note_text.get('1.0', 'end').strip('\n') # extract user input from text section
        self.note = note
        
    def submit_edit(self, note):
        created = datetime.datetime.now() # get current dat and time
        local_now = created.astimezone() # shows the local time and the GMT offset
        local_tz = local_now.tzinfo # sets timezone 
        meta = f'edited: {created}, {local_tz}' # turns metadata into a string
        
        # get user input
        title = self.edit_title.get() # extract user input from title section
        text = self.edit_text.get('1.0', 'end').strip('\n') # extract user input from text section
        tag = self.edit_tags.get() # extract user input from tags section
        link = self.edit_link.get() # extract user input from link section
        meta = meta
        author = self.edit_author.get()

        note_dict = {'title':title, 'text':text, 'link':link, 'tag':tag, 'meta':meta, 'author':author} # create the dictionary by creating key value pairs        
        make_note = MakeNote(note_dict) # pass the dictionary through to the creation of the MakeNote instance called make_note
        self.notes.append(make_note) # append the instance of the class to the notes variable
        self.notebook.append(make_note) # append the instance of the class to the notebook variable
        
        file = filedialog.asksaveasfile(initialdir = os.getcwd(),
                                          defaultextension = ".json", 
                                          filetypes = [("JSON files", "*.json"),
                                         ("all files", ".*")]) # gets the working directory where files will be saved, *** may need to be changed depending on the computer that this program is being run on         

        first_note = self.notes[0]
        note_dict = {'title':first_note.note_title, 'text':first_note.note_text, 'link':first_note.note_link, 'tag':first_note.note_tag, 'meta':first_note.note_metadata} 
        
        json_out = json.dumps(note_dict)
        file.write(json_out)
        self.notes = [] # Setting self.notes to empty allows the index to always be 
                
        return note_dict # returns note_dict variable which is the dictionary

        
    def edit_note(self, note):
        edit_window = customtkinter.CTkToplevel()
        edit_window.geometry("800x700")
        edit_window.title("Edit Snippet")
        
        self.edit_text_label = customtkinter.CTkLabel(edit_window, text = "Note text:")
        self.edit_text_label.grid(padx = 10, pady = 10, row = 2, column = 0, sticky = "e")
        self.edit_text = customtkinter.CTkTextbox(edit_window, height = 10, width = 60)
        self.edit_text.grid(padx = 10, pady = 10, row = 2 , column = 1)
        self.edit_text.insert("1.0", note.note_text)

        
        # create note title entry field
        self.edit_title_label = customtkinter.CTkLabel(edit_window, text = 'Note Title:')
        self.edit_title_label.grid(padx = 10, pady = 10, row = 1, column = 0, sticky = 'e')
        self.edit_title = customtkinter.CTkEntry(edit_window, width = 80) # allows user to enter data
        self.edit_title.grid(padx = 10, pady = 10, row = 1, column = 1, sticky = 'w')
        self.edit_title.insert(0, note.note_title) # adds default text (useful during development)
        
        # create note tags entry field
        self.edit_tag_label = customtkinter.CTkLabel(edit_window, text = 'Note tag:')
        self.edit_tag_label.grid(padx = 10, pady = 10, row = 3, column = 0, sticky = 'e')
        self.edit_tags = customtkinter.CTkEntry(edit_window, width=80) # allows user to enter data
        self.edit_tags.grid(padx = 10, pady = 10, row = 4, column = 1, sticky = 'w')
        self.edit_tags.insert(0, note.note_tag) # adds default text (useful during development)
        
        # create note link entry field
        self.edit_link_label = customtkinter.CTkLabel(edit_window, text = 'Note link:')
        self.edit_link_label.grid(padx = 10, pady = 10, row = 4, column = 0, sticky = 'e')
        self.edit_link = customtkinter.CTkEntry(edit_window, width = 80) # allows user to enter data
        self.edit_link.grid(padx = 10, pady = 10, row = 3, column = 1, sticky = 'w')
        self.edit_link.insert(0, note.note_link) # adds default text (useful during development)
        
        self.edit_author_label = customtkinter.CTkLabel(edit_window, text = 'Author:')
        self.edit_author_label.grid(padx = 10, pady = 10, row = 5, column = 0, sticky = 'e')
        self.edit_author = customtkinter.CTkEntry(edit_window, width = 60) # allows user to enter data
        self.edit_author.grid(padx = 10, pady = 10, row = 5, column = 1)
        self.edit_author.insert('0', note.note_author) # adds default text (useful during development
        
        # Create new note form and get the variables into each entry window 
        # save back to original file 

        self.edit_submit_button = customtkinter.CTkButton(edit_window, text = "Submit Edit:", command= lambda n = note: self.submit_edit(n)) 
        self.edit_submit_button.grid(padx = 10, pady = 10, row = 6, column = 0, sticky = "e")
    