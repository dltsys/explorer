#!/bin/bash
docker-compose build && docker rm -f abe && docker-compose up -d
