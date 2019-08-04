import json
import pathlib

class Manager():


    def __init__(self):

        self.file = '.\\values.json'
        self.entries = {}
        
        if pathlib.Path(self.file).exists():
            with open('.\\values', 'r') as file:
                self.entries = json.load(file)

        



    def add_entry(self, title, email, username, password):
            
        self.entries.update({title:[email, username, password]})
            
        with open(self.file, 'w') as file:
            json.dump(self.entries, file)

    def edit_entry(self, title, email, username, password):
        
        self.entries[title] = {title: [email, username, password]}

    def delete_entry(self, title):
            
        self.entries.pop(title)
        with open(self.file, 'w') as file:
            json.dump(self.entries, file)

    def get_entry(self, title):
        print(self.entries[title])

    def get_all_entries(self):
        print(self.entries)




    '''TODO {
            -hash passwords. Encrypt Json file.
            -This is crude as hell for a reason. But it must be cleaned up in the next iter.
            -get_all_entries() must format the data and return it instead of printing
            -learn about creating a tidier json file format on disk?
            -create an argument for "get_all_entries()" that returns entries sorted by alphabetical title
            -difflib functionality to help targetting when editing.
        }'''
