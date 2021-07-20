#!/usr/bin/env sh
find . -iname '*.mp3' -exec sh -c 'curfname="{}";\
length=`mp3info -p "%m" "$curfname" 2>&1`; \
errors=`mp3info -p "%b" "$curfname" 2>&1`; \
notmp3=`echo $errors | grep corrupt`;
songLength=10 # Specify a value, if a songs length is greater than the value it will be deleted.
if [ "$notmp3" ]; \
  then rm -rfv "$curfname"; \
else \
  if [ $errors -gt 0 ];\
     then rm -rfv "$curfname"; \
  fi; \
  if [ $length -gt $songLength ];\
     then rm -rfv "$curfname"; \
  fi; \
fi' \;
