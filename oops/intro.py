
class Greeting:
    name = ""
    def __init__(self, name):
        print("constructor is envoked")
        self.name = name  
    def say_hello_world(self):
        print("Hello,World")
    
    def say_hello(self, name):
        print(f"Hello,{name}")

    def say_hello_name(self):
        print(f"hello, {self.name}")

    def __str__(self):
        return "This is a Greet Class"

obj = Greeting("Mark")
obj.say_hello_name()

# print(obj.name)
# obj.say_hello_world()
# # obj.say_hello("Jhon")
