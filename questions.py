import pandas as pd
import sys,os

sys.path.append(os.path.abspath(os.path.join('people_ask')))
from Google_Questions import get_related_questions, get_simple_answer


dataframe_name = 'df'



df = pd.read_csv(f'./data/{dataframe_name}.csv')
# Creating list of keywords from the dataframe
Row_list =[]
for index, rows in df.iterrows():
	my_list = rows.keyword
	Row_list.append(my_list) 

nums = 1   
for I in Row_list:
    num = 1 
    myquestions = get_related_questions(I, 3)
    questions = []
    for i in myquestions:
     questions.append(i.split('Search for')[0])
    for x in questions:
        y = get_simple_answer(x)
        df.at[(nums-1), f'question_{num}'] = x
        df.at[(nums-1), f'answer_{num}'] = y
        num = num + 1 
    nums = nums + 1
    print(nums)

df.to_csv(f'./data/df.csv', index= False)
   