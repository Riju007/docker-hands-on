FROM python:3.12-slim

# prevent python from writing bytecode files.
# python will not write .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# disable output buffering for real time log
ENV PYTHONUNBUFFERED=1

# set default log level
ENV LOG_LEVEL=INFO

RUN apt-get -y update && apt-get install -y curl

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
