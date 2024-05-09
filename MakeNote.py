class MakeNote():
    def __init__(self, note_dict):
        self.note_title = note_dict['title'] # takes title from note_dict and sets it to the note_title attribute
        self.note_text = note_dict['text'] # takes text from note_dict and makes it the note_text attribute
        self.note_link = note_dict['link'] # takes link from note_dict and sets it to the note_link attribute
        self.note_tag = note_dict['tag'] # takes tag from note_dict and sets it to the note_tag attribute
        self.note_metadata = note_dict['meta'] # takes metadata from note_dict and sets it to the note_metadata attribute
        self.note_author = note_dict['author']
