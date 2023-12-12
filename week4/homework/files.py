import os
import shutil
import time

def list_files():
    return [f for f in os.listdir('.') if os.path.isfile(f)]

def is_recent(file):
    current_time = time.time()
    file_ctime = os.path.getctime(file)
    file_mtime = os.path.getmtime(file)
    return (current_time - file_ctime) < 24*60*60 or (current_time - file_mtime) < 24*60*60

def update_file(file):
    with open(file, 'a') as f:
        f.write("\nUpdated at: " + time.ctime())

def create_folder():
    if not os.path.exists("last_24hours"):
        os.makedirs("last_24hours")

def move_file(file):
    shutil.move(file, "last_24hours/" + file)

def main():
    create_folder()
    for file in list_files():
        if is_recent(file):
            update_file(file)
            move_file(file)


main()
