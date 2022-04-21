
def average(salary):
    salary.remove(min(salary))
    salary.remove(max(salary))
    totalAv = 0
    for item in salary:
        totalAv += item
    return totalAv / len(salary)


average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000])