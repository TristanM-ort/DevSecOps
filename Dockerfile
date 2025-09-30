FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# NETTOYAGE : Supprimer pip cache et outils inutiles en production
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip && \
    find /usr/local -name '*.pyc' -delete

COPY . .

EXPOSE 3000
CMD ["python", "app.py"]
