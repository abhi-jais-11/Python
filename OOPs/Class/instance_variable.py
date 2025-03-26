"""
Instance Varible or Object Level Variable:

    -If the value of the variable varied from object to object this type of variable is called instance variable.
    -The variable create using the self[argument] known as the instance variable.
    -The variable create using the object of the class known as the instance variable.
    -It can access only using self[inside] and instance[outside] [object of the class ]

Way to create Instance Variable:
    1.Using Constructor:
    2.Instance Method Using.
    3.Using object Of the class.

"""

# Instance variable example


class InstanceVariable:

    # using the constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("-------------------------------")
        print()
        print(f"Using Constructor:\nName:{self.name}\nAge:{self.age}")

    def set_instance_var_method(self, name, age):
        self.name = name
        self.age = age
        print("-------------------------------")
        print()
        print(f"Using Instance Method:\nName:{self.name}\nAge:{self.age}")


# creation of object

instanve_var = InstanceVariable("JackSone", 22)
instanve_var.set_instance_var_method("Jack", 24)
instanve_var.name = "Rahul"
instanve_var.age = 25
print("-------------------------------")
print()
print(f"Using Object:\nName:{instanve_var.name}\nAge:{instanve_var.age}")

