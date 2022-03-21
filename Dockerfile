# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /todo_list_project

# Set the working directory to /todo_list_project
WORKDIR /todo_list_project

# Copy the current directory contents into the container at /music_service
ADD . /todo_list_project/

EXPOSE 8000

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN python manage.py migrate

# start server
# CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
