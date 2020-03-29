FROM ubuntu:18.04

WORKDIR /code

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN  apt-get -y update \
  && apt-get install -y zip unzip \
  && rm -rf /var/lib/apt/lists/*

# Copy the files to docker image
COPY requirements.txt requirements.txt
COPY app.py ./
COPY finalized_model.zip ./

RUN unzip finalized_model.zip
# Install the python requirements
RUN pip3 install -r requirements.txt


CMD ["python3", "app.py"]