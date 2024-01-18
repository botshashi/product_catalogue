# product_catalogue
Simple product catalogue service written in django

## Steps to run the pizza_app

1. **Clone the repository:**
   ```bash
    git clone https://github.com/botshashi/product_catalogue.git
    ```
2. **Navigate to the project directory:**
   ```bash
    cd product_catalogue/demo_app
    ```
3. **Run startup script for running containers and db initialization:**
   ```bash
    chmod +x start_containers.sh
   ./start_containers.sh
   
   In case of any issue, wait for containers to become healthy, (docker ps)
   and initialize cassandra keyspace: 
   docker exec -it cassandra_container cqlsh -f /docker-entrypoint-initdb.d/init_cassandra.cql
    ```
4. **Stopping all containers:**
   ```bash
    chmod +x stop_containers.sh
    ./stop_containers.sh
    ```
# API Documentation

### Base URI
 http://localhost:5000

### GET /api/register
Endpoint for registering user
#### Request Body: <br>
```buildoutcfg
 {"username" : "sk", "email" : "sdk@gmail.com","first_name": "abc","last_name": "def", "password": "xyz"}
```

### POST /api/login
Endpoint for user login
#### Request Body: <br>
```buildoutcfg
 {"username" : "sk","password": "xyz"}
```
#### Response Body: <br>
```buildoutcfg
 {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.x8TMFbr5Bm_xUz6XQtLDn3YQcLYmKYW4E8nhyZepvyQ"
 }
```


### POST /api/products/add
Endpoint for adding new product.
#### Request headers: <br>
```buildoutcfg
 Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.x8TMFbr5Bm_xUz6XQtLDn3YQcLYmKYW4E8nhyZepvyQ
```
#### Request Body: <br>
```buildoutcfg
 {"product_name" : "p1","description": "sample desc", "price": 123.50, "quantity": 1}
```

### GET /api/products
Endpoint for getting product list.
#### Request headers: <br>
```buildoutcfg
 Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.x8TMFbr5Bm_xUz6XQtLDn3YQcLYmKYW4E8nhyZepvyQ
```

#### Response: <br>
```buildoutcfg
 {
    "products": [
        "c07f5478-aef4-4bb4-9ecc-6e518d514963",
        "c07f5478-aef4-4bb4-9ecc-6e518d514962",
        "c07f5478-aef4-4bb4-9ecc-6e518d514961"
    ]
 }
```

### GET /api/product
Endpoint for getting product detail given product_id.
#### Request headers: <br>
```buildoutcfg
 Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.x8TMFbr5Bm_xUz6XQtLDn3YQcLYmKYW4E8nhyZepvyQ
```
#### Request parameters: <br>
```buildoutcfg
 product_id: "c07f5478-aef4-4bb4-9ecc-6e518d514963"
```

#### Response: <br>
```buildoutcfg
 {
    "product": {
        "name": "samsung pro",
        "description": "128gb, 16 GB",
        "price": "12300.0",
        "status": "in stock"
    }
 }
```
<br>
<br>
