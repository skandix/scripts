#!/usr/bin/env python3
import argparse
import wgconfig.wgexec as wgexec # pip3 install wgconfig

parser = argparse.ArgumentParser()
parser.add_argument('--ip')
parser.add_argument('--owner')
args = parser.parse_args()

client_private_key, client_public_key = (wgexec.generate_keypair())
server_private_key, server_public_key = ("<redacted>", "<redacted>") # can also just read from file

client_config = f"""
[Interface]
Address = 10.13.37.{args.ip}/32
PrivateKey = {client_private_key}

[Peer]
PublicKey = {server_public_key}
Endpoint = 1.2.3.4:52345 # edit this
AllowedIPs = 0.0.0.0/0 # edit this

# This is for if you're behind a NAT and
# want the connection to be kept alive.
PersistentKeepalive = 25
"""

server_config = f"""
[Peer]
        PublicKey = {client_public_key}
        AllowedIPs = 10.13.37.{args.ip}/32
"""


print (f"### PASTE INTO {args.owner}.conf ###")
print (client_config)
print ("### END ###\n")

print ("### PASTE INTO wg0.conf ###")
print (server_config)
print ("### END ###")

print ("SAVE, and run ## wg-quick down wg0 && wg-quick up wg0 ##")
