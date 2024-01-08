FROM python:3.11.3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

# Install netcat
RUN apt-get update && apt-get install -y netcat
RUN apt-get clean && rm -rf /var/lib/apt/lists/*


COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
CMD ["bash", "/app/entrypoint.sh"]

EXPOSE 8300
