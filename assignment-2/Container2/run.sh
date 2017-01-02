#!/bin/bash
echo "Running run.sh"
export PYTHONPATH=$PYTHONPATH:/
dude run
python sum.py
Rscript graphs.R
