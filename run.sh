#!/bin/bash
docker run -it --env DISPLAY=$DISPLAY  -v $PWD/.env:/.env -v /tmp/.X11-uni/:/tmp/.X11-unix --net=host --rm gideons/easy-rewards
