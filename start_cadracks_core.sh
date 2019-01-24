#!/usr/bin/env bash

xhost +local:cadracks_core
docker start cadracks_core
docker exec -it cadracks_core /bin/bash