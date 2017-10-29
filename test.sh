#!/bin/sh

alias gcf='/Users/yusuke/.nvm/versions/node/v6.11.1/lib/node_modules/@google-cloud/functions-emulator/bin/functions'
echo '-------deploy START...--------'
gcf deploy helloWorld --trigger-http
echo '---------deploy end-----------'
echo ''
echo '------call helloWorld---------'
gcf call helloWorld
echo ''
echo ''
echo '-------------LOGS-------------'
gcf logs read --limit=100
echo ''
echo '---------all clear------------'
gcf clear

