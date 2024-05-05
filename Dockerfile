FROM python:3.7

WORKDIR /app

COPY . /app

COPY ./api /app/api

RUN pip3  install -r requirements.txt

RUN pip3  install uvicorn

EXPOSE 8000

CMD ["uvicorn", "api.main:my_app", "--host", "0.0.0.0", "--port", "8000"]