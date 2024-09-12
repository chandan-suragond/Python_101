class Parent():
    def __init__(self, id = None, name = None):
        if id is None and name is None:
            self.id = 7
            self.name = 'Chandan'
            print('Default constructor called')
        else:
            self.id = id
            self.name = name
            print('Parameterised constructor called')

    def printArgs(self) :
        # print(f"{self.name} {self.id}")
        return f"ID: {self.id} \nNAME: {self.name}\n------------------"
    
if __name__ == '__main__':
    obj1 = Parent()
    print(obj1.printArgs())

    obj2 = Parent(30, 'Nivu')
    print(obj2.printArgs())