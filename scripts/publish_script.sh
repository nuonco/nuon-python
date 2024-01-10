#!/bin/sh
# Must be /bin/sh because this script is meant to be run in Alpine,
# which uses busybox and doesn't have bash.

python -m pip install build twine

python -m build

twine upload -r testpypi dist/*
# twine upload dist/* --non-interactive --username $NUONBOT_PYPI_USERNAME --password $NUONBOT_PYPI_PASSWORD
