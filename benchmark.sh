
#!/bin/bash

# check if apache benchmark exists
command -v ab >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }

# run benchmark
ab -p post_loc.txt -T application/json -c 10 -n 2000 http://localhost:8080/send
