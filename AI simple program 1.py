import pandas as pd
student_grades={
    'student':["sona","lisa","thomas","jilli","gary"],
    'grades':[75,82,95,88,79]
}
student =pd.DataFrame(student_grades)
print(student)
