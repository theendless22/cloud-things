#why only run this as a script when we can complicate it further by dockerizing it.

FROM python:latest

LABEL owner="theendless"

WORKDIR /supe-project/src
COPY ./main.py /supe-project/src/

RUN pip install --upgrade pip
#RUN pip install python3-tk
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "/main.py"]

#Clone this repo and from within this folder, run: docker run <name>
