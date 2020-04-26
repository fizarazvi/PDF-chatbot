#!/bin/bash

if [[ -e Tictactoe.py.pid ]]; then   
    ./kill.sh
    ./start.sh

else
     echo "App not running"

fi
