FROM python:3.11.9-slim-bookworm
WORKDIR /revhire
COPY . /revhire
RUN pip install -r /revhire/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]