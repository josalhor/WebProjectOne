#/bin/bash

echo $(python3 -V)
rm -rf venv
mkdir -p venv
python3 -m venv venv
source ./venv/bin/activate
pip install wheel
pip install -r requirements.txt

