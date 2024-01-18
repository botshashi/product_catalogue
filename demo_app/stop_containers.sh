
#!/bin/bash

CONTAINERS_TO_STOP=("demo_app_container" "mysql_container" "cassandra_container")

# Stop each container
for container in "${CONTAINERS_TO_STOP[@]}"; do
    docker stop "$container"
done
