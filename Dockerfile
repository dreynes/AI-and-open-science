FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3.10
RUN apt install -y python3-pip
RUN apt install -y git
RUN apt install -y wget

SHELL ["/bin/bash", "--login", "-c"]

RUN mkdir -p /home/root/project
WORKDIR /home/root/project
COPY ./requirements.txt /home/root/project
COPY ./script.py /home/root/project
COPY ./config.json /home/root/project

ENV CONDA_DIR=/home/root/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN chmod 0700 ~/miniconda.sh
RUN bash ~/miniconda.sh -b -p ${CONDA_DIR}
RUN rm ~/miniconda.sh
ENV PATH=$CONDA_DIR/bin:$PATH

RUN echo ". ${CONDA_DIR}/etc/profile.d/conda.sh" >> ~/.profile
RUN conda init bash

RUN conda update --name base --channel defaults conda 
RUN conda create -n newenv
RUN conda clean --all --yes

RUN conda activate newenv && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    git clone https://github.com/kermitt2/grobid_client_python && \
    cd grobid_client_python && \
    python3 setup.py install && \
    cd ..

COPY ./script.sh /home/root/project
RUN chmod 0700 /home/root/project/script.sh
ENTRYPOINT ["/home/root/project/script.sh"]
