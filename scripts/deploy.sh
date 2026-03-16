#!/bin/bash

echo "Stopping old containers..."

docker-compose down

echo "Starting new deployment..."

docker-compose up -d --build

echo "Deployment completed successfully"