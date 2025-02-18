from abc import ABC, abstractmethod
from typing import List


class ICompanyServiceProvider(ABC):
    @abstractmethod
    def AddEmployee(self, employee_obj) -> List:
        pass

    @abstractmethod
    def returnSortedList(self ,employee_obj ) -> List:
        pass

    @abstractmethod
    def searchEmployee(self, emp_list,emp_id):
        pass

    @abstractmethod
    def returnSeleniumTesters(self,tester_list) :
        pass

    @abstractmethod
    def returnUFTTesters(self,tester_list):
        pass

    @abstractmethod
    def returnManagersWithHighAllowance(self,man_list):
        pass

    @abstractmethod
    def returnUnAllocatedDevelopers(self,dev_list):
        pass

    @abstractmethod
    def managerWithMaxProjects(self , man_list):
        pass

    @abstractmethod
    def returnHighlyPaidEmployees(self ,employee_obj) -> List:
        pass
