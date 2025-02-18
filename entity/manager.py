from entity.employee import Employee


class Manager(Employee):
    def __init__(self, emp_id ,name , salary,designation,project_allowance ,no_of_projects):
        super().__init__(emp_id,name, salary ,designation)  # Initialize parent class attributes
        self.__project_allowance = project_allowance
        self.__no_of_projects = no_of_projects

    def __str__(self):
        parent_str = super().__str__()
        return parent_str+ "\n Project Allowance : "+str(self.__project_allowance)+"\n Number Of Projects : "+str(self.__no_of_projects)
