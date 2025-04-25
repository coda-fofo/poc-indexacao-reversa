# Database

```bash
docker run -p 5432:5432 -e POSTGRES_USER=realuser -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=TATTOOGO postgres     
```

```bash
docker build -t rabisko-database .
docker run -p 5432:5432 --network=rabisko_network --name=rabisko-database rabisko-database
```