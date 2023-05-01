#!/bin/bash

# Update package list
sudo apt update

# Install Python 3
sudo apt install -y python3

# Install Git
sudo apt install -y git

# Clone the project from GitHub
git clone https://github.com/your_username/your_project.git

# Install Python dependencies using pip
cd your_project
pip install -r requirements.txt

# Run the application
python main.py
