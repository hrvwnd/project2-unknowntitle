FROM python:3.8.0
WORKDIR /opt/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
COPY . .