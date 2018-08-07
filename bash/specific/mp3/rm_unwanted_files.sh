#!/bin/zsh
find . -iname '*.mp3' -exec sh -c 'curfname="{}";\
length=`mp3info -p "%m" "$curfname" 2>&1`; \
errors=`mp3info -p "%b" "$curfname" 2>&1`; \
notmp3=`echo $errors | grep corrupt`; \
if [ "$notmp3" ]; \
  then rm -rfv "$curfname"; \
else \
  if [ $errors -gt 0 ];\
     then rm -rfv "$curfname"; \
  fi; \
  if [ $length -gt 10 ];\
     then rm -rfv "$curfname"; \
  fi; \
fi' \;
