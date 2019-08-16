# Pick-Parser
![Pick Resume Parser](/images/resume_parsers.png)

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/dsc-iiitdmk/Pick-Parser/blob/master/LICENSE)

## Introduction
Resumes are a great example of unstructured data. Each resume has its unique style of formatting, has its own data blocks, and has many forms of data formatting. This makes reading resumes hard, programmatically. Recruiters spend ample amount of time going through the resumes and selecting the ones that are a good fit for their jobs. 
 We want to make a Resume parser based on NLP, which can accept any resume in any style and can parse it to extract Names, Phone numbers, Email IDs, Education, Skills and some more information from resumes.
 
 ## Prerequisites
- Knowledge of Python
- Knowledge of NLP
## Installation
- pdm miner
```
$ pip install pdfminer        # python 2
$ pip install pdfminer.six    # python 3
```
-doc2text
```
$ pip install doc2text
```
-spaCy
```
$ pip install spacy
```
Now, we want to download pre-trained models from spacy. For this we need to execute:
```
$ python -m spacy download en_core_web_sm
```
-pandas
```
$ pip install pandas
```
For Extracting information of tuple we will be needing nltk
```
$ pip install nltk
$ python -m nltk nltk.download('words')
```

 


