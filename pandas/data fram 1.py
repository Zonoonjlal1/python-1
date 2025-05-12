import pandas as pd

student_data = {'std_id': [1001, 1002, 1003, 1004, 1005], 'name': ['ahmed', 'ali', 'ahmed', 'ali', 'ahmed'],
                'marks': [100, 200, 300, 400, 500], 'avrag': [80, 90, 70, 60, 50]}

std_name = ['ahmed','ali','zozo','sloa','eyad']
std_marks = [100,200,300,400,500]

zain = pd.DataFrame(student_data)
#print(zain)

sahar = pd.Series( data= std_marks , index= std_name)
#print(sahar)

#print(sahar['zozo'])

x= pd.Series(student_data)
print(x)

print(x['marks'])