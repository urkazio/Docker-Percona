FROM python:3.11-alpine
COPY . /app/
WORKDIR /app
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN python -m pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev linux-headers python3-dev libffi-dev openssl-dev
RUN pip install -r requirements.txt
CMD flask run