FROM postgres:latest

ENV POSTGRES_USER=realuser
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_DB=TATTOOGO

WORKDIR /docker-entrypoint-initdb.d

COPY sql/1_setup.sql sql/2_populate.sql ./

EXPOSE 5432
