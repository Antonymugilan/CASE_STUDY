class Employee:
    """ Base class containing member variables """
    def __init__(self,emp_id,name,salary,designation):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary= salary
        self.__designation = designation

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __str__(self):
        return " Employee Details : \n " + "\n Employee id : " + str(self.__emp_id)+"\n Employee name : " + self.__name +"\n Salary : "+str(self.__salary)+ "\n Designation : "+self.__designation + "\n"

    def __repr__(self):
        return " \n " + "\n Employee id : " + str(self.__emp_id)+"\n Employee name : " + self.__name +"\n Salary : "+str(self.__salary)+ "\n Designation : "+self.__designation + "\n"





