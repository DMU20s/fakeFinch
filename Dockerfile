FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /app
RUN pip install fastapi uvicorn
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "800"]