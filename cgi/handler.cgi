#!/bin/sh
echo "Content-Type: text/plain"
echo
echo "Handler CGI responding"
echo
echo "SCRIPT_NAME: ${SCRIPT_NAME}"
echo "PATH_INFO: ${PATH_INFO}"
echo "REQUEST_METHOD: ${REQUEST_METHOD}"
echo "QUERY_STRING: ${QUERY_STRING}"
echo
echo "Environment variables (partial):"
env | awk '/^HTTP_/{print} /^REMOTE_ADDR$/{print} /^SERVER_NAME$/{print}/^REQ/{print}' | sort
