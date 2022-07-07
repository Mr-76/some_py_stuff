
class Kangaroo:
    def __init__(self):
        self.pouch_contents = []


    def put_int_pouch(self,obj):
        self.pouch_contents.append(obj)
    def __str__(self):
        string = "" 
        for item in self.pouch_contents:
            string +=  str(item) +"\n"
            print(string)
        return string

