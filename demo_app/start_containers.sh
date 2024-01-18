#!/bin/bash

docker-compose up -d

# Set the container names to wait for
CONTAINERS_TO_WAIT=("demo_app_container" "mysql_container" "cassandra_container")

# Function to check if a container is in a "running" state
is_container_running() {
    local container_name="$1"
    local container_status=$(docker inspect -f '{{.State.Status}}' "$container_name" 2>/dev/null)

    if [ "$container_status" == "running" ]; then
        return 0  # Container is running
    else
        return 1  # Container is not running
    fi
}

# Wait for all containers to be running
echo "Waiting for containers to be in a 'running' state..."
while true; do
    all_containers_running=true

    for container in "${CONTAINERS_TO_WAIT[@]}"; do
        if ! is_container_running "$container"; then
            all_containers_running=false
            break
        fi
    done

    if [ "$all_containers_running" = true ]; then
        echo "All containers are now running."
        break
    fi

    sleep 5  # Adjust the sleep duration as needed
done

echo "Waiting for db initialization"
sleep 30
docker exec -it cassandra_container cqlsh -f /docker-entrypoint-initdb.d/init_cassandra.cql