import os, argparse

audioExt = ['.mp3', '.wav', '.flac']

parser = argparse.ArgumentParser()
parser.add_argument("--dir", "-dir", help="what music dir do you want to generate a playlist file of")

args = parser.parse_args()

for root, dirs, files in  os.walk(args.dir):
    for name in files:
        for ext in audioExt:
            if ext in name:
                with open(args.dir+'playlist.m3u','a+') as file:
                    file.write(os.path.join(root,name))
                    file.write("\n")
            else:
                pass

    print ("Done")
