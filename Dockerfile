FROM python:3.9.17-slim-bullseye

WORKDIR /app
COPY ./ /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"  ]

