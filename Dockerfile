FROM python:3.11.2-alpine3.17
WORKDIR /app
RUN apk update \ 
    && pip install --upgrade pip 

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]