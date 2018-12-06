FROM python:3.6
RUN mkdir /src
EXPOSE 5000
COPY . /src
RUN pip3 install -r /src/requirements.txt
CMD ["python3", "/src/app.py"]