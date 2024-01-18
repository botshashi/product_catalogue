
CREATE KEYSPACE IF NOT EXISTS demo_app_keyspace
WITH replication = {
   'class': 'SimpleStrategy',
   'replication_factor': 1
};

use demo_app_keyspace;

CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    price DECIMAL,
    stock_quantity INT
);

insert into products (product_id, description, name, price, stock_quantity) values ('c07f5478-aef4-4bb4-9ecc-6e518d514961', '128gb, 16 GB', 'iphone20', 12300.0, 1);
insert into products (product_id, description, name, price, stock_quantity) values ('c07f5478-aef4-4bb4-9ecc-6e518d514962', '128gb, 16 GB', 'mi5', 12000.0, 1);
insert into products (product_id, description, name, price, stock_quantity) values ('c07f5478-aef4-4bb4-9ecc-6e518d514963', '128gb, 16 GB', 'samsung pro', 12300.0, 1);