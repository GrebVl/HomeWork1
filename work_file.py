from Notes import *
import json

def file_writ(notes_list):
    with open('note_js.json', 'w') as f:
        i = 0
        to_json = []
        while i < notes_list.get_size():
            to_json.append({'titl': notes_list.get_note(i).get_titl(), 'msg': notes_list.get_note(i).get_msg(),
                            'date': notes_list.get_note(i).get_dat()})
            i += 1
        f.write(json.dumps(to_json))

def file_read():
    with open('note_js.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)
    return templates