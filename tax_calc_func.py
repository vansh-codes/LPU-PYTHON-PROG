salary=float(input("Salary: "))
percent=int(input("Tax percentage: "))

def CalculateTax(salary,percent=20):
    print(salary*(percent/100))

CalculateTax(salary)
CalculateTax(salary,percent)
