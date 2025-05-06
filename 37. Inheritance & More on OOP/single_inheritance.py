# Inheritance method

class Employee:

    company = "ITC"
    name = "Rohan"      # Idhar maine ek employee karke ek class banaya hai jis mein ye do classes ke attributes define kiye hai

    def show(self):     # Ye function company ka name jo by default hai, employee ka name jo harry ke variable mein maine update kiya hai. Yeh dono chezein ye function print karega.

        print(f"He is working in {self.company} company and his name is {self.name}.")



class Salary(Employee):

    company = "ITC TechInfo"    # Idhar maine company ka name update kiya hai and jo bhi classes thi employee ki by default woh maine iss mein inherit kar di hai, iss Salary wali class mein. Isko inheritence method bolte hai.

    def his_salary(self):   #   Iss function mein updated company ka name print hoga, or by default name "Rohan" print hoga employee ki class se, and salary print hogi jo mein dunga.

        print(f"\nPrevious company name is {self.company} and his name is {self.name} and his salary is {self.salary}.")



harry = Employee()
harry.name = "Harry"    # update kiya hai name "Rohan" se maine "Harry" bana diya.

harry.show()    # show wale function ko call kiya hai harry variable ke saath and isse pahle jo bhi changes kiye honge maine woh bhi change karke print kar dega.


rohan = Salary()
rohan.salary = 150000   # ye new instance dala hai "salary" karke.

rohan.his_salary()  # ye his_salary wali function ko call karega and jo uss function mein print karne ka hoga, woh print kar dega.