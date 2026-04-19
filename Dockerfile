FROM python:3.12-slim

RUN apt-get update && apt-get install -y nginx supervisor curl \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/sbin/nginx /usr/bin/nginx

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=.

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --clear

COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD ["supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]