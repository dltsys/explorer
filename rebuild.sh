#!/bin/bash
sudo mkdir data-db
sudo chmod a+rwX data-db
docker-compose build
docker rm -f abe
docker-compose up -d
