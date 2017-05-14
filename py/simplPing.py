#!/bin/python
# -*- coding: utf-8 -*-
from socket import error
import socket

port = 0
ip = ""
serviceName = ""

def ping(serviceName , ip , port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ipPport = (ip, port)

    try:
        s.connect(ipPport)

    except error, e:
        return "STATE: Server is Offline!!"
    else:
        return "State: Server is Online"
