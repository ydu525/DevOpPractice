#!/bin/sh
MYUSERNAME=$USER
MYPASSWORD="123"
STARTOFSCRIPT=`date`
echo "My login name for this application is: $MYUSERNAME"
echo "My login password for this application is:$MYPASSWORD"
echo "I start this script at: $STARTOFSCRIPT"
ENDOFSCRIPT=`date`
echo "I end this script at: $ENDOFSCRIPT"
