class Employee:

    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")
    
def Create_obj():
    print("Creating object...")
    obj=Employee()
    print("Function end...")

print("Create_obj() called")
obj = Create_obj()
print("Program end")