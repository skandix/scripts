#!/bin/bash

container=$1
ext_ip=$(docker exec -it $container /bin/sh -c "curl http://ipecho.net/plain")
rev_ip_chk=$(host $ext_ip | cut -d' ' -f5)

if [ $rev_ip_chk != "customer.tigerbackbone.com" ]
then 
    message="All Good\n$rev_ip_chk"
else 
    message=$(docker stop $container -q)
fi

msg_content=\"$message\"

url='discord-webhook-url'
curl -H "Content-Type: application/json" -X POST -d "{\"content\": $msg_content}" $url
