#!/bin/bash

# Install base dependencies
sudo apt update
sudo apt install -y python3-pip libatlas-base-dev

# Python dependencies
pip3 install -r ../edge_computing/requirements.txt

# Configure audio
sudo usermod -a -G audio $USER
sudo raspi-config nonint do_i2c 0  # Enable I2C for sensors