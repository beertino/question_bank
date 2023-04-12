import requests
import json

url = "<INSERT_API_ENDPOINT>"

subject_name = '<INSERT_SUBJECT_NAME>'

payload = json.dumps({
    "collection": "questions",
    "database": f"{subject_name}",
    "dataSource": "Cluster0",

    # change the filter parameters below as fit
    # filter parameters : 'paper_no', 'source', 'paper_type', 'qn_no', 'year'
    "filter": {

    },

    # qn_content is the string of the questions
    # remove unnecessary parameters if the information is not needed
    "projection": {
        "paper_no": 1,
        "source": 1,
        "paper_type": 1,
        "qn_no": 1,
        "year": 1,
        "qn_content": 1
    }
})

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',

    # provide the API key
    'api-key': '<INSERT_API_KEY>',
}

response = requests.request("POST", url, headers=headers, data=payload)

# qn_dict is a list of dict objects that represents a question
qn_dict = json.loads(response.text)['documents']
