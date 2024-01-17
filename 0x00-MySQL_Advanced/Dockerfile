# Dockerfile

FROM ubuntu:18.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y mysql-server python3.7 wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Start MySQL service
CMD service mysql start && /bin/bash
