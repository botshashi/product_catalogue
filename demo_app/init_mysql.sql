
CREATE DATABASE IF NOT EXISTS demo_app;
USE demo_app;

CREATE USER 'demo_app_user'@'%' IDENTIFIED BY 'demo_pass';

GRANT ALL PRIVILEGES ON demo_app.* TO 'demo_app_user'@'%';


