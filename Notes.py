from Note import *


class Notes:

    notes = list()

    def notes_add(self, note, msg):
        self.notes.append(Note(note, msg))

    def get_note(self, index):
        return self.notes[index]

    def set_note(self, note, index):
        self.notes[index] = note

    def get_size(self):
        return len(self.notes)


    def notes_rm(self, index):
        self.notes.remove(self.notes[index])






