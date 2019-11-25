# for sorting inspera assesment into folders, rather than having everything in one dir... messy as hell
import os
import shutil

inspera = "InsperaAssessment_225538634"
os.chdir(inspera)

files = (sorted(os.listdir()))
docs = [x for x in sorted(os.listdir()) if "." in x and ".pdf" in x]
zips = [x for x in sorted(os.listdir()) if "." in x and ".zip" in x]

print (zips)

unique_groups = []

# Generate list of uniq group ids
for file in files:
    under = file.split('_')[0]
    if not under in unique_groups:
        unique_groups.append(under)

# make folders
for folder in unique_groups:
    os.mkdir(folder)

# move files into folders
for doc in docs:
    print (shutil.move(f"{doc}", f"{doc.split('_')[0]}/{doc}"))

for zap in zips:
    print (shutil.move(f"{zap}", f"{zap.split('_')[0]}/{zap}"))
