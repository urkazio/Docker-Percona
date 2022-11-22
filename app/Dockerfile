FROM python:3.11-alpine
WORKDIR /datos
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt /datos/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 3306
COPY app.py /datos/
CMD flask run