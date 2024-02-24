FROM python:3.11.8-slim
RUN apt-get update && apt-get install -y curl
COPY backend /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements/prod.txt
CMD ["flask", "--app", "main", "run", "-h", "backend"]