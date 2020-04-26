#!/bin/bash

if [[ ! -e app.py.pid ]]; then   # Check if the file already exists
    python app.py &                   #+and if so do not run another process.
    echo $! > app.py.pid
else
    echo -n "ERROR: The process is already running with pid "
    cat app.py.pid
    echo
fi