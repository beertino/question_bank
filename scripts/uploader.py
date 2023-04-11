from pymongo import MongoClient

import os

client = MongoClient(
    'mongodb+srv://<USER_NAME>:<USER_PASSWORD>@<CLUSTER_LOCATION>')

db = client['alvl']

col = db['questions']

start_year = 2012
end_year = 2023

for yr in range(start_year, end_year):
    qn_list = os.listdir(f'../questions_to_upload/{yr}')
    for qn in qn_list:
        year, paper_type, paper_no, qn_no = qn[:-4].split('_')
        paper_no = paper_no[1:]
        qn_no = qn_no[1:]
        print(year, paper_type, paper_no, qn_no)
        with open(f'../questions_to_upload/{yr}/{qn}') as f:
            qn_content = f.read()
        qn = {
            'year': year,
            'paper_type': paper_type,
            'paper_no': int(paper_no),
            'qn_no': int(qn_no),
            'qn_content': qn_content
        }
        col.insert_one(qn)
