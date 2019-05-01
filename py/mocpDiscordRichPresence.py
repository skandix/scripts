from pypresence import Presence
from time import sleep
import moc

def discoPresence(client_id):
    RPC = Presence(client_id)
    RPC = Presence(client_id,pipe=0)

    RPC.connect()

    state = moc.get_info_dict()['state']
    if state == "PLAY":
        while True:
            artist = moc.get_info_dict()['artist']
            track = moc.get_info_dict()['songtitle']
            bitrate = moc.get_info_dict()['bitrate']
            rate = moc.get_info_dict()['rate']
            file = moc.get_info_dict()['file'].split('/')[-1]
            ext = file.split('.')[-1]
            
            if artist != "":
                print(RPC.update(details="Playing {:} - {:}".format(artist, track), state="{:} | {:} | {:}".format(bitrate, rate, ext)))
                sleep(5)

            else:
                print(RPC.update(details="{:}".format(file), state="{:} | {:}".format(bitrate, rate)))
                sleep(5)
    else:
        return

discoPresence("insert_your_client_id_HERE!")
