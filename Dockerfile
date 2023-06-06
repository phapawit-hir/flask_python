FROM python:3.12.0b1-buster

WORKDIR /app
COPY ./ /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"  ]

