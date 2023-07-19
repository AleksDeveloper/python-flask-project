FROM python:latest

WORKDIR /app

COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
CMD ["ash", "-c", "python -m flask run -h 0.0.0.0 -p 8000"]