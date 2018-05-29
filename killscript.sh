kill -9 $(ps aux | grep '[a].out'| awk '{print $2}') && echo "Program killed"
