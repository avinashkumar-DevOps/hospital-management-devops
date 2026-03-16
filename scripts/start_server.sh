#!/bin/bash

echo "======================================"
echo "Starting Hospital Management System"
echo "======================================"

APP_NAME="hospital_app"
MYSQL_CONTAINER="hospital_mysql"


echo "Checking Docker service..."

if ! systemctl is-active --quiet docker
then
    echo "Docker not running. Starting Docker..."
    sudo systemctl start docker
else
    echo "Docker already running"
fi


echo "--------------------------------------"
echo "Starting MySQL Container"
echo "--------------------------------------"

docker start $MYSQL_CONTAINER 2>/dev/null

if [ $? -ne 0 ]; then
    echo "MySQL container not found. Starting via docker-compose..."
    docker-compose up -d mysql
else
    echo "MySQL container started"
fi


echo "--------------------------------------"
echo "Starting Application Container"
echo "--------------------------------------"

docker start $APP_NAME 2>/dev/null

if [ $? -ne 0 ]; then
    echo "Application container not found. Running docker-compose..."
    docker-compose up -d app
else
    echo "Application container started"
fi


echo "--------------------------------------"
echo "Restarting Nginx"
echo "--------------------------------------"

sudo systemctl restart nginx


echo "--------------------------------------"
echo "Checking Application Status"
echo "--------------------------------------"

sleep 5

STATUS=$(curl -o /dev/null -s -w "%{http_code}" http://localhost:5000)

if [ $STATUS -eq 200 ]; then
    echo "Application is running successfully"
else
    echo "Application failed to start"
fi


echo "--------------------------------------"
echo "Running Containers"
echo "--------------------------------------"

docker ps


echo "--------------------------------------"
echo "Hospital Management System Started"
echo "Access Application:"
echo "http://localhost"
echo "--------------------------------------"