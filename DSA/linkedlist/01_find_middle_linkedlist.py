#creating node
class Node:
    def __init__(self,x):
        self.data =x
        self.next=None
    
#creating linkedlist
class Linkedlist:
    def __init__(self):
        self.head = None


    #inseart at the begining

    def Insert_at_begining(self,data):
        
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next =self.head
            self.head = new_node

        

    
    def Traversing_linked_list(self):
        current = self.head
        while current:
            print(current.data,end="--> ")
            current = current.next
        print('None')

    #insert at the end of the list
    def insert_at_end(self,data):
        new_node = Node(data)
        current = self.head

        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        #insert at any position
    def insert_at_any_position(self,index,data):
        current = self.head
        for i in range(0,index-1):
            current = current.next
        new_node = Node(data)
        new_node.next=current.next
        current.next=new_node
        
    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return True
            current= current.next

        return False
    
    def delete(self,key):
        temp = self.head

        while temp:
            if temp.data == key:
                print(temp.data)
                break
        
        print(temp.data)

    def find_max(self):
        v = []
        #Traverse through the entire linked list and push all the values into the list
        temp = self.head
        while temp :
            # print(temp.data)
            v.append(temp.data)
            temp = temp.next
        
        max_num = max(v)
        print(max_num)
    def find_middle(self):
        v =[]
        current = self.head
        while current:
            # print(current.data)
            v.append(current.data)
            current = current.next

            
        mid_index = len(v)//2

        print(v[mid_index])

    def reverse_linkedlist(self):
        current = self.head

    
        while current.next is not None:
            current = current.next

        self.head = current.next
        current.next = current
        print(self.head.data)
            



if __name__ == "__main__":
    l1 = Linkedlist()
    l1.Insert_at_begining(34)
    l1.insert_at_end(12)
    l1.insert_at_end(45)
    l1.Insert_at_begining(10)
    l1.insert_at_end(100)
    l1.insert_at_any_position(2,23)
    l1.insert_at_any_position(4,35)
    l1.Traversing_linked_list()
    # print(l1.search(35))
    # l1.delete(35)
    l1.find_middle()
    l1.reverse_linkedlist()