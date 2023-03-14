FROM python:3.11-slim

# Makes sure that logs are shown immediately
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

EXPOSE 5000

WORKDIR /app

# This is for single-container deployments (multiple-workers)
CMD ["gunicorn", "main:app", \
     "--bind", "0.0.0.0:5000", \
     "--access-logfile", "-", \
     "--workers", "2"]
