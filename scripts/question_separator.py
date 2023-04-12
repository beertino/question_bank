import os


def separate(filename):

    with open(filename) as f:
        reader = f.read()

    reader_size = len(reader)

    break_phrase = '\\rule[0.5ex]{1\columnwidth}{1pt}'

    found_index = reader.find(break_phrase)

    qns = []

    while 0 <= found_index < reader_size:
        next_index = reader.find(break_phrase, found_index + len(break_phrase))
        qns.append(reader[found_index + len(break_phrase):next_index])
        found_index = next_index
        if found_index == -1:
            break

    qns = [qn.strip()[len('\\begin{enumerate}'):-
                      len('\\begin{enumerate}')+1].strip()+'\n' for qn in qns[:-1]]

    for q in qns:
        question_info = q[q.find('{[}')+len('{[}'):q.find('{]}')]
        if question_info.count('/') == 3:
            year, source, paper_no, question_no = question_info.split('/')
            with open(f'../questions_to_upload/{year}_{source}_{paper_no}_{question_no}.tex', 'w+') as f:
                f.write(q)
        elif question_info.count('/') == 4:
            year, source, exam_type, paper_no, question_no = question_info.split(
                '/')
            with open(f'../questions_to_upload/{year}_{source}_{exam_type}_{paper_no}_{question_no}.tex', 'w+') as f:
                f.write(q)
        else:
            print(f'Incorrect format for {question_info}')


# Rename the filename appropriately
filename = '../question_to_split/test.tex'

separate(filename)
