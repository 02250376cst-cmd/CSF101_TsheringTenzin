print("hello world")
x = 2
y = 5
sum = x+y
print("The sum of x and y is: ",sum)
name = input("enter your name: ")
age = input("enter your age: ")
print("you are", name, "and you are", age, "years old")

class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll = LinkedList()
ll.display()  # Output: 1 -> 2 -> 3
