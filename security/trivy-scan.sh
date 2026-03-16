#!/bin/bash

echo "Running Trivy Security Scan..."

trivy image hospital-app

echo "Scan Completed"