#/bin/bash

SPEC=https://ctl.prod.nuon.co/oapi/v3
#SPEC=https://ctl.stage.nuon.co/oapi/v3
#SPEC=http://host.docker.internal:8081/oapi/v3

docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli:latest-release generate \
  -i $SPEC \
  -g python \
  -o /local \
  --package-name nuon \
  -t /local/scripts/templates

# save version to file for workflows to read from
cat pyproject.toml | grep version | sed -e 's/.*version = "\(.*\)"/\1/' > version.txt
