
![Zenodo doi badge](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.1234567-red.svg)
[![Documentation Status](https://readthedocs.org/projects/ai-and-open-science/badge/?version=latest)](https://ai-and-open-science.readthedocs.io/en/latest/?badge=latest)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
# AI-and-open-science
Repository created for uploading the assigment of Artificial Intelligence And Open Science In Research Software Engineering subject

The assigment consists in analysing papers with grobid and python:
- Draw a keyword cloud based on the abstract information.
- Create a visualization showing the number of figures per article.
- Create a list of links found in each paper.

# [License](LICENSE)
GNU GENERAL PUBLIC LICENSE

# Using the software with docker
If you want to use docker to use the software, you should do the following steps
Before start, make sure that you have docker installed
- First of all clone the repository in your local
```bash
  git clone https://github.com/dreynes/AI-and-open-science.git
```
- We move to inside the repository
```bash
  cd AI--amd-open-science/
```
- Now we can create the containers executing:
```bash
docker compose up -d
```
- Then for execute the program use:
```bash
docker logs client
```
The results will be inside a folder called "out_docker"

- If a connection problem apperar try cchanging the first line of the config.json and change grobid for our ip
```bash
"grobid_server": "http://grobid:8070",
```

# Using the software without docker
Alternatively here are instructions on how to run the software without docker in case you prefer this option
First install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and [docker](https://www.docker.com/)
- Next clone the repository in your local
```bash
  git clone https://github.com/dreynes/AI-and-open-science.git
```
- Open a terminal execute this command to deploy grobid

```bash
  docker pull lfoppiano/grobid:0.7.2
  docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```


- Now, create an anaconda environment activate it and install the dependences

```bash
  conda create -n newenv
  conda activate newenv 
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt 
``` 
- Next, install the grobid client

```bash
  git clone https://github.com/kermitt2/grobid_client_python
  cd grobid_client_python
  python3 setup.py install
  cd ..
```
- To finish execute the python file
```bash
  python3 script.py
```




