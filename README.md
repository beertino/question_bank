# Question Bank

This is a documentation simple project that uses MongoDB Atlas to store questions as documents.

The attributes in the documents are assumed to be the following:
- `year`
- `source`
- `qn_no`
- `paper_type`
- `paper_no`
- `qn_content`

## Setting up a MongoDB Atlas
Head to <a href = https://www.mongodb.com/cloud/atlas/register> to sign up with your Google Account.

## Question Separator
Given a `.tex` file, run `question_separator.py` to extract each questions in the file and put in the `question_to_upload` folder categorized in 
different `year` folders.

Check the example file at `question_to_split\test.tex` for the format of the file.

## Uploading Questions with Python Script

The assumption is that:
- the questions are located in `questions_to_upload` directory of the project. 
- the questions have the format `<year>_<source>_<optional_paper_type>_P<paper_number>_Q<question_number>.tex` 

Example of the folder and file structure

>```
>root
>   |--questions_to_upload
>       |--<year>_<source>_<optional_paper_type>_P<paper_number>_Q<question_number>.tex
>   |--scripts
>```

Go to `scripts` folder and run `uploader.py`. 

The database will be called `subject_name` and the questions will be inserted into the `questions` collection.

## Retrieving Questions with MongoDB Data API

Go to `scripts` folder and run `downloader.py`. 

`qn_dict` is a list of Python dictionary objects which represents the questions queried.
