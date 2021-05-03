FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY . /app/Backend/

WORKDIR /app/Backend/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]