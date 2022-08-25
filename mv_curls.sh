#!/usr/bin/env bash

cd ./csv
for f in *.txt2; do
    mv -- "$f" "${f%.txt2}.txt"
done