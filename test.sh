#!/bin/sh

alias gcf='/Users/yusuke/.nvm/versions/node/v6.11.1/lib/node_modules/@google-cloud/functions-emulator/bin/functions'
echo '--------DEPLOY START----------'
gcf deploy helloWorld --trigger-http
echo '---------DEPLOY END-----------'
echo ''
echo '-------CALL helloWorld--------'
gcf call helloWorld
echo '----------CALL END------------'
echo ''
echo ''
echo '------------LOGS--------------'
gcf logs read
echo '----------LOGS END------------'
echo ''
echo '----------all CLEAR-----------'
gcf clear

