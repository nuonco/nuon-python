#/bin/bash

set -e
set -o pipefail
set -u

echo
echo "preparing to generate SDK"
echo

echo "> installing dependencies"
pipx install openapi-python-client --include-deps

SPEC=https://api.nuon.co/oapi/v3
# SPEC=https://ctl.stage.nuon.co/oapi/v3
# SPEC=http://host.docker.internal:8081/oapi/v3

echo "> spec: $SPEC"
echo "> generating"
openapi-python-client generate \
  --url $SPEC \
  --output-path . \
  --overwrite

# save version to file for workflows to read from
cat pyproject.toml | grep version | sed -e 's/.*version = "\(.*\)"/\1/' > version.txt
