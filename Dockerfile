FROM python:3
COPY requirements.txt /opt/app/requirements.txt
COPY . /opt/app
WORKDIR /opt/app
RUN apt-get -y update
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]