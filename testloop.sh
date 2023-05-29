#!/bin/zsh

echo "-----1: ----$1"
if [ $1 ]; then
    subdir=$1
else
    subdir=.
fi
# echo "-----subdir: ----$subdir"

while true; do
    clear
    # pytest -x -vv $subdir
    pytest  -x -vv $subdir
    fswatch ./**/*.py  -1
done