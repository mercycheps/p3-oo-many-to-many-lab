class Author:
    all = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)
        


class Book:
    all = []
    
def __init__(self, title):
    if not isinstance(title):
        raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)
         
class Contract:
   
        