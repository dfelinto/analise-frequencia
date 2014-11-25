#!/bin/bash

ABC=`echo "ABCDEFGHIJKLMNOPQRSTUVWYXZ" | grep -o .`
FILE=$1
for i in $ABC; do echo $i ' _ ' `tr -d -c $i < $FILE | awk '{ print length; }'`; done
