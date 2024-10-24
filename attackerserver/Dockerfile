FROM python:3.7
COPY ./src /app
WORKDIR /app
ARG LPORT
ENV SERVERLPORT=${LPORT}
ENTRYPOINT python -m http.server ${SERVERLPORT} 2>&1 | tee httplog.txt