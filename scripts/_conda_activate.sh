
#!/bin/bash

read enviroment <<< $(conda info --env | grep "*" | awk '{print $1}')
echo "$enviroment"
