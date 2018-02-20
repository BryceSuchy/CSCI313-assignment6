import pygame

class File(self):
    def __init__(self):
        pass

    def Open(self, file):
        self._file_object = open("blockobjects.txt", "r")
        self._file_sounds = open("sounds.txt", "r")
        self._file_object.read()
        self._file_sounds.read()
        










