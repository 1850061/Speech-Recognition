import win32api


class asrFunction:
    def __init__(self):
        pass

    def playMusic(self, filename):
        filename = filename + ".mp3"
        win32api.ShellExecute(0, 'open', filename, '', '', 1)


    def openNotepad(self):
        win32api.ShellExecute(0, 'open', 'C:\\Program Files\\Typora\\Typora.exe', '', '', 0)


    def drawPicture(self):
        win32api.ShellExecute(0, 'open', 'C:\\WINDOWS\\system32\\mspaint.exe', '', '', 1)
