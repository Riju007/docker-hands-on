# --------- Builder Stage --------------------
# 1. Set the base image
FROM python:3.12-slim AS builder

# 2. Define a working directory
WORKDIR /app

# system deps needed only to build wheels.
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# 3. Copy requirements file
COPY requirements.txt /app/requirements.txt

# 4. install required modules from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ----------------------------- Runtime Stage --------------------------
# 1. Set the base image
FROM python:3.12-slim

# 2. Define a working directory
WORKDIR /app

# 3. copy only installed packages from builder
COPY --from=builder  /usr/local /usr/local

# 4. copy the code into the designated folder
COPY . /app/

# 5 set python envs
ENV PYTHONUNBUFFERED=1

# 6. Expose 8000 port
EXPOSE 8000

# 7. run the django server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]