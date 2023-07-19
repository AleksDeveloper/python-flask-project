FROM python:3-alpine3.10

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . .
CMD ["ash", "-c", "python -m flask run -h 0.0.0.0 -p 8000"]