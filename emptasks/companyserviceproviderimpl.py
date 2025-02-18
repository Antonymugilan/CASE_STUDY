from typing import List

from emptasks.icompanyserviceprovider import ICompanyServiceProvider
from errorsss.EmployeeNotFoundException import EmployeeNotFoundException


class CompanyServiceProviderImpl(ICompanyServiceProvider):
    def __init__(self):
        self.__employee_list = []


    def AddEmployee(self, employee_obj):
        self.__employee_list.append(employee_obj)
        return self.__employee_list


    def returnSortedList(self , employee_obj) -> List:
         return sorted(employee_obj, key=lambda emp: int(emp._Employee__salary.replace("$", "").strip()))

    def searchEmployee(self,emp_list ,emp_id):
        for emp in emp_list:
            if emp._Employee__emp_id == emp_id:
                return f"{emp}\nEmployee Found: True"
        else:
            raise EmployeeNotFoundException()



    def returnSeleniumTesters(self,tester_list) :
        sel_tester =[]
        for tes in tester_list:
            if tes._Tester__skilled_in_selenium is True:
                sel_tester.append(tes.__getattribute__("_Employee__name"))
        return sel_tester


    def returnUFTTesters(self,tester_list):
        uft_tester = []
        for tes in tester_list:
            if tes._Tester__skilled_in_uft is True:
                uft_tester.append(tes.__getattribute__("_Employee__name"))
        return uft_tester

    def returnManagersWithHighAllowance(self, man_list):
        high_all_list = []
        high = 0

        for e in man_list:
            if e._Manager__project_allowance > high:
                high = e._Manager__project_allowance

        for e in man_list:
            if e._Manager__project_allowance == high:
                high_all_list.append(e.__getattribute__("_Employee__name"))

        return high_all_list

    def returnUnAllocatedDevelopers(self,dev_list):
        allocated_developer = []
        for dev in dev_list:
            if dev._Developer__allotted is True:
                allocated_developer.append(dev.__getattribute__("_Employee__name"))
        return allocated_developer



    def managerWithMaxProjects(self,man_list):
        man_with_max_project = []
        max = 0

        for e in man_list:
            if e._Manager__no_of_projects > max:
                max = e._Manager__no_of_projects

        for e in man_list:
            if e._Manager__no_of_projects == max:
                man_with_max_project.append(e.__getattribute__("_Employee__name"))

        return  man_with_max_project


    def returnHighlyPaidEmployees(self,employee_obj) -> List:
        return sorted(employee_obj, key=lambda emp: int(emp._Employee__salary.replace("$", "").strip()),reverse=True)
