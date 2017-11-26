FROM python:3.6-jessie

WORKDIR /demo

ADD swagger-ui-dist ./swagger-ui-dist
ADD requirements.txt .
RUN pip install -r requirements.txt

RUN groupadd demouser
RUN useradd -g demouser demouser
RUN chown -R demouser:demouser /demo

USER demouser

ENTRYPOINT ["python", "server.py", "docker"]
