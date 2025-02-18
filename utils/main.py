from emptasks.companyserviceproviderimpl import CompanyServiceProviderImpl
from entity.company import Company
from entity.developer import Developer
from entity.employee import Employee
from entity.manager import Manager
from entity.tester import Tester
from entity.developer import Developer
from errorsss.EmployeeNotFoundException import EmployeeNotFoundException

""" Testing Employee Class """

emp_obj = Employee(101,"Steve","$50000" , " Manager ")
print(emp_obj)

print("===========================================")

""" Testing Developer  """

dev_obj = Developer(101 ,"Steve" ,"$50000"," Manager ",191.22,1000.76,True)
print(dev_obj)

print("===========================================")

""" Tester module """

test_obj = Tester(101,"Steve","$50000"," Manager ",True,True,True,5000.9463)
print(test_obj)

print("===========================================")

""" Testing Manager """
man_obj = Manager(101,"Steve","$50000"," Manager ",23999.98,40)
print(man_obj)

print("===========================================")

""" Container Class Company """
emp_obj1 = Employee(101,"Steve","$50000" , " Manager ")
emp_obj2 = Employee(102,"Bucky","$55000" , " Developer ")
emp_obj3 = Employee(103,"Tony","$45000" , " Tester ")
emp_obj4 = Employee(104,"Barton","$78900" , " Manager ")
emp_obj5 = Employee(105,"Annie","$67000" , " Developer ")

emp_list =[emp_obj1,emp_obj2,emp_obj3,emp_obj4,emp_obj5]

company_obj = Company("S Industries" ,"Times Square , NYC ." ,emp_list)
print(company_obj)

print("===========================================")

""" Implementing Add Employee"""
service_obj  = CompanyServiceProviderImpl()
print(service_obj.AddEmployee(emp_obj1))
print(service_obj.AddEmployee(emp_obj2))

print("===========================================")

"""Implementing sorted list """

print(service_obj.returnSortedList(emp_list))

print("===========================================")

"""Implementing search Employee """
try :
    print(service_obj.searchEmployee(emp_list,103))
except EmployeeNotFoundException as e :
    print(e)

try :
    print(service_obj.searchEmployee(emp_list,106))
except EmployeeNotFoundException as e :
    print(e)

print("===========================================")

""" Returning Selenium testers """

test_obj1 = Tester(101,"Steve","$50000"," Tester ",True,True,True,5000.9463)
test_obj2 = Tester(102,"Harry","$50000"," Tester ",True,False,True,5000.9463)
test_obj3 = Tester(103,"Bob","$50000"," Tester ",False,True,True,5000.9463)
test_obj4 = Tester(104,"Tony","$50000"," Tester ",True,True,True,5000.9463)
test_obj5 = Tester(105,"Richard","$50000"," Tester ",False,True,True,5000.9463)


tester_list = [test_obj1,test_obj2,test_obj3,test_obj4,test_obj5]

print(service_obj.returnSeleniumTesters(tester_list))

print("===========================================")

""" Returning Uft Tester"""

print(service_obj.returnUFTTesters(tester_list))

print("===========================================")


""" Returning Manager with high allowance """

man_obj1 = Manager(101,"John","$50000","Manager" ,12000,10)
man_obj2 = Manager(102,"Phil","$50000","Manager" ,8000,17)
man_obj3 = Manager(103,"Alan","$50000","Manager" ,11000,34)
man_obj4 = Manager(104,"Stew","$50000","Manager" ,9000,26)

man_list = [man_obj1,man_obj2,man_obj3,man_obj4]
print(service_obj.returnManagersWithHighAllowance(man_list))

print("===========================================")

""" Returning the name of Developers who are allocated to projects """

dev_obj1 = Developer(101,"John","$50000","Developer",1231.12,1233,False)
dev_obj2 = Developer(101,"Phil","$50000","Developer",1231.12,1233,True)
dev_obj3 = Developer(101,"Alan","$50000","Developer",1231.12,1233,True)
dev_obj4 = Developer(101,"Stew","$50000","Developer",1231.12,1233,True)

dev_list = [dev_obj1,dev_obj2,dev_obj3,dev_obj4]

print(service_obj.returnUnAllocatedDevelopers(dev_list))

print("===========================================")


""" Returning manager who has maximum no of projects handled """

print(service_obj.managerWithMaxProjects(man_list))

print("===========================================")

""" Return Highly Paid Employees"""

print(service_obj.returnHighlyPaidEmployees(emp_list))




