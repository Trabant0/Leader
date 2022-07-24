from math import isnan
import pandas as pd

StudentData = pd.read_csv('StudentData.csv')

AbsoluteLeadersDictionary = {}

def check_absolute_leaders(_student: pd.DataFrame):
    if not isnan(_student['В образовании']):
        student = _student.copy()
        student = student.dropna(axis=1)
        student = student.transpose()
        if len(student)>2:
            return True
    return False


for student in StudentData['Ученики']:
    student_with_point = StudentData[StudentData['Ученики']==student]
    AbsoluteLeadersDictionary[student] = check_absolute_leaders(student_with_point)

AbsoluteLeaders = pd.Series(AbsoluteLeadersDictionary)
AbsoluteLeaders.to_csv('Абсолютный лидер.csv')

for leader_in in StudentData:
    if leader_in != 'Ученики':
        pd.concat([StudentData['Ученики'],  StudentData[leader_in]], axis=1).to_csv(leader_in+'.csv')



