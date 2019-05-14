#!/usr/bin/env bash

URL=http://127.0.0.1/my-video

if ! type ab > /dev/null; then
    echo "Please install ab";
fi;

# Wait a little bit in case if services started up with delay
sleep 2
ab -t 10 -n 1001 -c 10 ${URL}

# Wait until sync happens
sleep 2
result=$(curl -s ${URL} | jq -r ".view_count")

if [[ "${result}" -ge "1000" ]]; then
    echo "✅ Sent 1001 requests, got ${result} (one additional query) views."
else
    echo "💥 Test failed, expected ~1001 got ${result}."
fi;
