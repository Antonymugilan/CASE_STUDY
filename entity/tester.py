from entity.employee import Employee


class Tester(Employee):
    def __init__(self, emp_id ,name , salary,designation, skilled_in_selenium ,skilled_in_uft, skilled_in_jemeter , test_allowance):
        super().__init__(emp_id,name, salary ,designation)  # Initialize parent class attributes
        self.__skilled_in_selenium =skilled_in_selenium
        self.__skilled_in_uft = skilled_in_uft
        self.__skilled_in_jemeter =skilled_in_jemeter
        self.__test_allowance = test_allowance

    def __str__(self):
        parent_str = super().__str__()
        return parent_str+ "\n Skilled in Selenium : "+str(self.__skilled_in_selenium)+"\n Skilled in UFT : "+str(self.__skilled_in_uft)+"\n Skilled in Jemeter : "+ str(self.__skilled_in_jemeter)+"\n Test Allowance : "+str(self.__test_allowance)
