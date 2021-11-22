# build stage
FROM python:3.7.5-slim
RUN apt-get update \
&& apt-get install git -y \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*
RUN mkdir /app
RUN git clone https://github.com/abc7468/gu.git /app
WORKDIR /app
RUN pip3 install --upgrade pip \
&& pip3 install -r /app/requirements.txt
ENV FLASK_APP app.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
