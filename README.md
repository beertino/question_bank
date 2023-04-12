# Question Bank

This is a documentation simple project that uses MongoDB running on Google Cloud Platform (GCP) to store questions as documents.

The attributes in the documents are assumed to be the following:
- `year`
- `qn_no`
- `paper_type`
- `paper_no`
- `qn_content`

## Setting up a MongoDB on GCP


## Question Separator

## Uploading Questions with Python Script

The assumption is that:
- the questions are located in `questions_to_upload` directory of the project. 
- each question are located each folder with the format `<year>_<paper_type>_P<paper_number>_Q<question_number>.tex` 

Example of the folder and file structure

>```
>root
>   |--questions_to_upload
>       |--<year_one>
>       |  |---<year>_<paper_type>_P<paper_number>_Q<question_number>.tex
>       |--<year_two>
>   |--scripts
>```

Go to `scripts` folder and run `uploader.py`. 

## Retrieving Questions with MongoDB Data API

Go to `scripts` folder and run `downloader.py`. 
