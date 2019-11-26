#!/bin/bash
 
# control section
  : ${1?"Usage $0 ProjectPath Version Date"}
  : ${2?"Usage $0 ProjectPath Version Date"}
  : ${3?"Usage $0 ProjectPath Version Date"}
  
echo Executing 'PreparaRelease' script
# Remember to change Data and Time
for FileName in `ls $1/Src/*.[c-h] $1/Inc/*.[c-h] $1/readme.txt`; do
  echo "Changing $FileName"
  awk -v ReleaseVerion=${2} '{if(($1 ~ /^\*/) && ($2=="\@version")) printf(" * @version\t%s\n",ReleaseVerion); else print;}' $FileName > pippo.txt
  mv pippo.txt $FileName
  awk -v ReleaseDate=${3} '{if(($1 ~ /^\*/) && ($2=="\@date")) printf(" * @date\t%s\n",ReleaseDate); else print;}' $FileName > pippo.txt
  mv pippo.txt $FileName
  rm -f pippo.txt
done
 
