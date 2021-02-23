/*
admin login for this app:
username: biprajit163
password: djangoRestAPI
*/


CREATE DATABASE proxy_db;
CREATE USER proxy_db_user WITH PASSWORD 'proxy_db';
GRANT ALL PRIVILEGES ON DATABASE proxy_db TO proxy_db_user;