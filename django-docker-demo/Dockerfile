# 1. Set the base image
FROM python:3.12-slim

# 2 set python envs
ENV PYTHONUNBUFFERED=1

# 3. Define a working directory
WORKDIR /app

# 4. Copy requirements file
COPY requirements.txt /app/requirements.txt

# 5. install required modules from requirements.txt
RUN pip install -r requirements.txt

# 6. copy the code into the designated folder
COPY . /app/

# 7. Expose 8000 port
EXPOSE 8000

# 8. run the django server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]