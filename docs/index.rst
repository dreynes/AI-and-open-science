|DOI| |Documentation Status| |Python| |GitHub| # AI-and-open-science
Repository created for uploading the assigment of Artificial
Intelligence And Open Science In Research Software Engineering subject

The assigment consists in analysing papers with grobid and python: -
Draw a keyword cloud based on the abstract information. - Create a
visualization showing the number of figures per article. - Create a list
of links found in each paper.

`License <LICENSE>`__
=====================

GNU GENERAL PUBLIC LICENSE

Using the software with docker
==============================

If you want to use docker to use the software, you should do the
following steps Before start, make sure that you have docker and docker
compose installed - First of all clone the repository in your local

.. code:: bash

     git clone https://github.com/dreynes/AI-and-open-science.git

-  We move to inside the repository

.. code:: bash

     cd AI--amd-open-science/

-  Now we can create the containers executing:

.. code:: bash

   docker compose up -d

-  Then for execute the program use:

.. code:: bash

   docker logs client

The results will be inside a folder called “out_docker”

-  If a connection problem apperar try cchanging the first line of the
   config.json and change grobid for your ip

.. code:: bash

   "grobid_server": "http://grobid:8070",

Using the software without docker
=================================

Alternatively here are instructions on how to run the software without
docker in case you prefer this option First install
`conda <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`__
and `docker <https://www.docker.com/>`__ - Next clone the repository in
your local

.. code:: bash

     git clone https://github.com/dreynes/AI-and-open-science.git

-  Change the first line of the config.json and change grobid for your
   ip or localhost

.. code:: bash

   "grobid_server": "http://grobid:8070", -> "grobid_server": "http://localhost:8070",

-  Open a terminal execute this command to deploy grobid

.. code:: bash

     docker pull lfoppiano/grobid:0.7.2
     docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

-  Next, install the grobid client

.. code:: bash

     git clone https://github.com/kermitt2/grobid_client_python
     cd grobid_client_python
     python3 setup.py install
     cd ..

-  Now, create an anaconda environment activate it and install the
   dependences

.. code:: bash

     conda create -n newenv
     conda activate newenv 
     python3 -m pip install --upgrade pip
     pip install -r requirements.txt 

-  To finish execute the python file

.. code:: bash

     python3 script.py

Workflow
========

.. figure:: https://github.com/dreynes/AI-and-open-science/blob/main/workflow/workflow.png?raw=true
   :alt: workflow

   workflow

.. |DOI| image:: https://zenodo.org/badge/599152576.svg
   :target: https://zenodo.org/badge/latestdoi/599152576
.. |Documentation Status| image:: https://readthedocs.org/projects/ai-and-open-science/badge/?version=latest
   :target: https://ai-and-open-science.readthedocs.io/en/latest/?badge=latest
.. |Python| image:: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
.. |GitHub| image:: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
