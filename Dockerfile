FROM python:3.7-alpine
RUN mkdir /src
EXPOSE 5000
COPY . /src
RUN pip3 install -r /src/requirements.txt
CMD ["python3", "/src/app.py"]
