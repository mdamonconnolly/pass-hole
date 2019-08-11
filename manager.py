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
            
        try:
            self.entries.update({title:[email, username, password]})    
            with open(self.file, 'w') as file:
                json.dump(self.entries, file)
        except Exception as e:
            print('Error adding entry {0} with Exception: {1}'.format(title, e))
            
    def edit_entry(self, title, email, username, password):

        try:
            self.entries[title] = {title: [email, username, password]}
            with open(self.file, 'w') as file:
                json.dump(self.entries, file)
        except Exception as e:
            print('Error editing entry {0} with Exception: {1}'.format(title, e))

    def delete_entry(self, title):

        try:
            self.entries.pop(title)
            with open(self.file, 'w') as file:
                json.dump(self.entries, file)
        except Exception as e:
            print('Delete failed with Exception: {0}'.format(e))


    def get_entry(self, title):
        return self.entry[title]

    def get_all_entries(self):
        print('returning {0}'.format(self.entries))

        return self.entries




    '''TODO {
            -hash passwords. Encrypt Json file.
        }'''
