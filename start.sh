#!/bin/bash

# Start XQuartz
open -a Xquartz

# Wait for XQuartz to start
sleep 2

# Start XQuartz in listen mode
/opt/X11/bin/Xquartz :0 -listen tcp

# Allow connections from localhost
xhost +localhost
