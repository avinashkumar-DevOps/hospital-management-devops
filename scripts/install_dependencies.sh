#!/bin/bash

echo "====================================="
echo "Starting Server Dependency Setup"
echo "====================================="

# Update system
echo "Updating system packages..."
sudo apt update -y


# Install Python
echo "Installing Python..."
sudo apt install -y python3 python3-pip python3-venv


# Install Git
echo "Installing Git..."
sudo apt install -y git


# Install MySQL Client
echo "Installing MySQL client..."
sudo apt install -y mysql-client


# Install Nginx
echo "Installing Nginx..."
sudo apt install -y nginx


# Install Docker
echo "Installing Docker..."

sudo apt install -y \
apt-transport-https \
ca-certificates \
curl \
software-properties-common


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"


sudo apt update -y

sudo apt install -y docker-ce


# Enable Docker
sudo systemctl start docker
sudo systemctl enable docker


# Add current user to docker group
sudo usermod -aG docker $USER


# Install Docker Compose
echo "Installing Docker Compose..."

sudo curl -L "https://github.com/docker/compose/releases/download/2.27.0/docker-compose-$(uname -s)-$(uname -m)" \
-o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose


# Verify installations
echo "====================================="
echo "Verifying installations"
echo "====================================="

python3 --version
pip3 --version
docker --version
docker-compose --version
nginx -v
git --version


echo "====================================="
echo "All dependencies installed successfully"
echo "====================================="