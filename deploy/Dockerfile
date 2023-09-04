FROM continuumio/miniconda3

RUN apt update

RUN apt install -y unzip

RUN apt install -y curl

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN git clone https://github.com/braiso-22/reflex-example

WORKDIR /reflex-example

RUN conda env create -n reflex -f environment.yml

SHELL ["conda", "run", "-n", "reflex", "/bin/bash", "-c"]

RUN reflex init

CMD ["conda", "run", "-n", "reflex", "/bin/bash", "-c", "reflex run"]