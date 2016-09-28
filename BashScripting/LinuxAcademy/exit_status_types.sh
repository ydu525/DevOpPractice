#!/bin/bash
#to show exit status types
#set -e

expr 1 + 5
echo $?

rm not_exists.sh  
echo $?

expr 10 / 0
echo $?
