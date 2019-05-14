#!/usr/bin/env bash

URL=http://127.0.0.1/my-video

if ! type ab > /dev/null; then
    echo "Please install ab";
fi;

ab -t 10 -n 10000 -c 10 http://127.0.0.1/my-video

sleep 1
result=$(curl ${URL})
expected="{\"view_count\":1001}"

if [[ ${result} == *"${expected}"* ]]; then
    echo "✅ Sent 10001 requests, got 10001 as expected"
else
    echo "💥 Test failed, expected and actual results didn't match"
fi;
