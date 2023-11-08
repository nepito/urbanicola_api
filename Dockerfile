FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
COPY ./requirements.txt /app/requirements.txt
COPY ./tests/data /app/data
RUN pip install --no-cache-dir --upgrade --requirement /app/requirements.txt
COPY ./app /app
