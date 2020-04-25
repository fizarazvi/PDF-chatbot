#!/bin/bash

if [[ -e app.py.pid ]]; then   
    kill -9 $(cat app.py.pid)   
                               
    rm app.py.pid              
else
    echo "app.py is not running"
fi