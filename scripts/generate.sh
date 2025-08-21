#/bin/bash

set -e
set -o pipefail
set -u

ENV="{$1:-prod}"


HOST="https://api.nuon.co"
if [ "$ENV" == "dev" ]; then
  HOST="http://localhost:8081"
elif [ "$ENV" == "stage" ]; then
  HOST="https://api.stage.nuon.co"
fi

SPEC="$HOST/oapi/v3"

config=`pwd`"/gen.yaml"
echo
echo "preparing to generate SDK"
echo ">   host: $HOST"
echo "> config: $config"

echo "> installing dependencies"
pipx install openapi-python-client --include-deps


echo "> spec: $SPEC"
echo "> generating"
openapi-python-client generate \
  --url $SPEC \
  --config $config \
  --output-path . \
  --overwrite \
  --meta uv

# save version to file for workflows to read from
cat pyproject.toml | grep version | sed -e 's/.*version = "\(.*\)"/\1/' > version.txt
