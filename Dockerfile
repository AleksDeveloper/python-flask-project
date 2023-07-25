FROM python:3.11.4

#Where the working directory will be
WORKDIR /app

#copy the requirements.txt to the working directory
COPY requirements.txt /app

#see python version, update pip and install requirements for the app
RUN python --version
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#Set environment variables inside the container
RUN echo $MY_OUTLOOK_EMAIL
ENV MY_OUTLOOK_EMAIL=$MY_OUTLOOK_EMAIL
ENV MY_OUTLOOK_PASSWORD=$MY_OUTLOOK_PASSWORD
ENV MY_UPLOADS_PATH=$MY_UPLOADS_PATH

COPY . .
#Execute this command, to start the flask app, running in all addresses, mapped to port 8000
CMD ["sh", "-c", "python -m flask run -h 0.0.0.0 -p 8000"]