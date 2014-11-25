#!/bin/bash

clear

FILE=$1
TABLE=$2

TMP=/tmp/code
cp $FILE $TMP
chmod +w $TMP

cat $TABLE | while read line; do
 CODE=${line:0:1}
 TEXT=${line:3:1}

 if [ $TEXT != $CODE ]; then
   REGEX=`echo s/$CODE/$TEXT/g`
   sed -i '' -e $REGEX $TMP
 fi
done

cat $TMP
rm $TMP
