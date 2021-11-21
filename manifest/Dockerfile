FROM 299522382061.dkr.ecr.ap-northeast-3.amazonaws.com/test-flask:v3
WORKDIR /app
ENV FLASK_APP app.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
