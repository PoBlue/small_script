#!/bin/bash
SERVICE=$1

ps -x | grep -v grep | grep -v bash | grep $1 > /dev/null
result=$?
if ! [ "${result}" -eq "0" ]
then
    exit 1
fi