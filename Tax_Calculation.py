'''
Write a program that can be used to calculate the federal tax. The tax is
calculated as follows: For single people, the standard exemption is $4,000; for
married people, the standard exemption is $7,000. A person can also put up
to 6% of his or her gross income in a pension plan. The tax rates are as follows:

If the taxable income is:
-Between $0 and $15,000, the tax rate is 15%.
- Between $15,001 and $40,000, the tax is $2,250 plus 25% of the taxable income over $15,000.
-Over $40,000, the tax is $8,460 plus 35% of the taxable income over $40,000.
Prompt the user to enter the following information:
 -Marital status
- If the marital status is "married," ask for the number of children under the age of 14
- Gross salary (If the marital status is "married" and both spouses have income, enter the combined salary.)
- Percentage of gross income contributed to a pension fund
    Your program must consist of at least the following functions:
a. Function getData: This function asks the user to enter the relevant data.
b. Function taxAmount: This function computes and returns the tax owed.


To calculate the taxable income, subtract the sum of the standard exemption,
the amount contributed to a pension plan, and the personal exemption,
which is $1,500 per person. (Note that if a married couple has two children
under the age of 14, then the personal exemption is $1,500 * 4 = $6,000.)
'''

def getData():
    
        global empSalary
        empName = input("Enter Employee Name : ")
        empSalary = int(input("Enter  Salary of " + empName + ": "))
        maritalStatus = input("married ? 'Y' for yes and 'N' for no : ").upper()
        
          
        if (maritalStatus == 'Y'):
            spouseSalary = int(input("Enter  Salary of " + empName +"'s Spouse " +" : "))
            children = int(input ("Enter the number of children under Age 14 :" ))
            grossSalary = empSalary + spouseSalary
            print("Combined salary of couple = ", grossSalary)
            taxableIncome = grossSalary - 7000
            # print("taxable income 1 : " , taxableIncome)
            taxableIncome = taxableIncome - (0.06*taxableIncome) - (1500*(children+1))
            # print("taxable income 2 : " , taxableIncome)
        elif(maritalStatus == 'N' ):
             taxableIncome = empSalary - 4000
            #  print("taxable income 1 : " , taxableIncome)
             taxableIncome = taxableIncome - (0.06*taxableIncome) - 1500
            #  print("taxable income 1 : " , taxableIncome)
        else:
             print("invalid")
    
                
        return taxableIncome
        
        
def taxAmount(taxableIncome):
    
        global totalTax
        if 0<taxableIncome<=15000:
             totalTax = ((taxableIncome*15)/100)
            #  return totalTax
        elif 15001<=taxableIncome<=40001: 
             totalTax = 2250 + (((taxableIncome-15000)*25)/100) 
            #  return totalTax
        elif 40001<taxableIncome:
             totalTax = 8460 + (((taxableIncome - 40000)*35)/100)
            #  return totalTax
             
        print("Total Taxable Income = " + str(taxableIncome))
        print("Total Tax = " + str(totalTax))
        return totalTax

     
def main():
    Employee = getData()
    EmployeeTotalTax = taxAmount(Employee)
    GrossIncome = empSalary - totalTax
    print ("Gross Income is = ",GrossIncome)
main()
# totalTax = taxAmount(taxableIncome = input(taxableIncome))
# grossIncome = empSalary - totalTax

# print("Total Taxable Income = " + str(taxableIncome))
# print("Total Tax = " + str(totalTax))

# print("Employee's Gross Income is : " + str(grossIncome))


# print(empName , empSalary)



# nameList = []


# numofemp = int(input("Enter the numbers of Employees : "))

# for i in range (numofemp):
#     Name = str(input("Enter Employee name :"))
#     Salary = int(input("Enter "))
#     nameList.append(Name)
    
# print(nameList)


    
