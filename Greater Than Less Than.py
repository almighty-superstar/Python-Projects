from itertools import groupby
nums=input("""Enter any set of number and it will be sorted to whether it is less than 10.
Seperate these numbers by a comma in between each one: """)
nums=nums.split(",")
new_nums=[float(i) for i in nums]
def smaller_than_10(x):
    return x<10
group_obj= groupby( new_nums, key=smaller_than_10)
for key,value in group_obj:
    print(key, list(value))
