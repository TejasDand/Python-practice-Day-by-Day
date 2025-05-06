class Employee:
    a = 56

    @classmethod    # ye method jab hum use karenge toh ye class attribute ko dikhayega. Agar hum instance (object) se bhi isko change karenge toh koi change nhi hoga.

    def show(cls):
        print(f"The value of class attribute is {cls.a}")   # 1 print karega naa ki 45, kyunki class attribute mein value 1 hai or humne class method use kiya hai.


e = Employee()
e.a = 45
e.show()