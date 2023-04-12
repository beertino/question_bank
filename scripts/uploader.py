from pymongo import MongoClient

import os

client = MongoClient(
    'mongodb+srv://<USER_NAME>:<USER_PASSWORD>@<CLUSTER_LOCATION>')

subject_name = 'h2_mathematics'

db = client[subject_name]

col = db['questions']

start_year = 2012
end_year = 2023

for yr in range(start_year, end_year):
    qn_list = os.listdir(f'../questions_to_upload/{yr}')
    for qn in qn_list:
        if qn.count('_') == 3:
            year, source, paper_no, qn_no = qn[:-4].split('_')
        if qn.count('_') == 4:
            year, source, paper_type, paper_no, qn_no = qn[:-4].split('_')
        paper_no = paper_no[1:]
        qn_no = qn_no[1:]
        with open(f'../questions_to_upload/{yr}/{qn}') as f:
            qn_content = f.read()
        qn_json = {
            'year': year,
            'source': source,
            'paper_no': int(paper_no),
            'qn_no': int(qn_no),
            'qn_content': qn_content
        }
        if qn.count('_') == 4:
            qn_json['paper_type'] = paper_type
        col.insert_one(qn_json)
