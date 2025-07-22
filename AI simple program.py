import pandas as pd
one = pd.DataFrame({
    'name':['amber','jack','brown','smith','young'],
    'subject_name':['sub1','sub2','sub4','sub6','sub5'],
    'marks_scored':[93,90,82,64,71]},
    index=[1,2,3,4,5])

two = pd.DataFrame({
    'name':['ben','cole','sam','tom','martial'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'marks_scored':[96,80,73,77,81]},
    index=[1,2,3,4,5])
print(pd.concat([one,two]))