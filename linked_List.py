class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    #Add methods for singly linked list 
    def addToFront(self, val) :
        #Create new node w/ val
        new_node = SLNode(val)
        #Set the next on the new node to the old head. Pushes the old head down
        new_node.next = self.head 
        #Set head to new node
        self.head = new_node  #new node is the memory address 
        return self
    def print_values(self) :
        runner = self.head   #starting point
        while (runner != None) :     #loop throgh nodes
            print(runner.value)
            runner = runner.next
        return self
    def add_To_Back(self, val) :
        new_node = SLNode(val)  #create node
        runner = self.head 
        while (runner.next != None) :     #loop throgh nodes
            runner = runner.next
        runner.next = new_node        #add new node to the end of the list 
        return self
    def remove_from_front(self) :
        runner = self.head 
        self.head = runner.next
        return self
    def remove_from_back(self) :
        runner = self.head 
        while (runner.next != None) :
            prev_runner = runner 
            runner = runner.next 
        prev_runner.next = None 
        return self
    def remove_val(self, val) :
        runner = self.head 
        if (runner.value == val) :   #if the first value is the desired remove 
            self.remove_from_front()
            return self
        while (runner.value != val) :
            prev_runner = runner 
            runner = runner.next
        # if (runner.value == val ) :    Don't need to account for last statement 
        #     self.remove_from_back()
        #     return self 
        prev_runner.next = runner.next  
        return self
    def insert_at(self, val, n) :
        new_node = SLNode(val)
        runner = self.head 
        index = 0
        if (n == 0) :
            self.addToFront(val)
            return self
        while(runner.next != None and n != index ) :
            prev_runner = runner 
            runner = runner.next 
            index += 1
        prev_runner.next = new_node
        new_node.next = runner
        # self.add_To_Back(val)
        return self




x = "hello"
my_list = SList()
# my_list.addToFront("Jim")
# my_list.addToFront("Dwight")
# my_list.addToFront("Andy")
# my_list.print_values()
my_list.addToFront("are").addToFront("Linked lists").add_To_Back("fun!").print_values()
print ("***********")
my_list.insert_at("fun!", 0).print_values()    # chaining, yeah!

