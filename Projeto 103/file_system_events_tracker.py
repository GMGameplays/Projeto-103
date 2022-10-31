from msilib.schema import File
import sys
import time
import random
import os
import shutil
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Gabriel Martins/projetos/"

class FileEventHandler():
    def files_created(ref,event):
        print(f"{event.src_path} foi criado!")

    def files_modified(ref,event):
        print(f"{event.src_path} foi modificado!")

    def files_moved(ref,event):
        print(f"{event.src_path} foi movido para {event.dest_path}!")

    def files_deleted(ref,event):
        print(f"{event.src_path} foi deletado!")

event_handler = FileEventHandler()
observer = Observer()

observer.schedule(event_handler,from_dir,recursive = True)

observer.start()

try:
    while True:
        time.sleep(1)
        print("monitorando...")
except KeyboardInterrupt:
    print("encerrado o monitoramento!")
    observer.stop()