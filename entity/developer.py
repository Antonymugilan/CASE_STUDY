from entity.employee import Employee


class Developer(Employee):
    def __init__(self, emp_id ,name , salary,designation, ot_allowance, night_shift_allowance, allotted):
        super().__init__(emp_id,name, salary ,designation)  # Initialize parent class attributes
        self.__ot_allowance = ot_allowance
        self.__night_shift_allowance = night_shift_allowance
        self.__allotted = allotted

    def __str__(self):
        parent_str = super().__str__()
        return parent_str+ "\n OT Allowance : "+str(self.__ot_allowance)+"\n Night Shift Allowance : "+str(self.__night_shift_allowance)+"\n Allotted : "+ str(self.__allotted)
