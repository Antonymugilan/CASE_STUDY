""" Container class - Company """

class Company:
    def __init__(self ,company_name , location , emp_list):
        self.__company_name = company_name
        self.__location = location
        self.__emp_list = emp_list

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __str__(self):
        return " Company Details : \n" +" Company Name : " + self.__company_name +"\n Location : " + self.__location + "\n Employee List : "+str(self.__emp_list)

    def __repr__(self):
        return " Company Details : \n" +" Company Name : " + self.__company_name +"\n Location : " + self.__location + "\n Employee List : "+str(self.__emp_list)
