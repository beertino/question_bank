from pymongo import MongoClient

import os

client = MongoClient(
    'mongodb+srv://<USER_NAME>:<USER_PASSWORD>@<CLUSTER_LOCATION>')

subject_name = '<INSERT_SUBJECT_NAME>'

db = client[subject_name]

col = db['questions']

qn_list = os.listdir(f'../questions_to_upload/')
for qn in qn_list:
    if qn.count('_') == 3:
        year, source, paper_no, qn_no = qn[:-4].split('_')
    if qn.count('_') == 4:
        year, source, paper_type, paper_no, qn_no = qn[:-4].split('_')
    paper_no = paper_no[1:]
    qn_no = qn_no[1:]
    with open(f'../questions_to_upload/{qn}') as f:
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
