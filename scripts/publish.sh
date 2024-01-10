#/bin/bash

docker run -w /local --rm -v ${PWD}:/local python:3.12.1-alpine /local/scripts/publish_script.sh
