class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name, self.mode, encoding='UTF-8')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File('example1.txt', 'a') as file:
    file.write('Всем привет!\n')
