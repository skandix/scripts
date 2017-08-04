# Here's a list of handy regex expressions...
>fyi, some of them are old and some are new.

Used to match images used in articles, g
```regex
ur'(?!<\w{4}\s\w{8}\S+)(?:image|twitter|facebook)"\s\w{7}\S{2}[\w\d\S]+[.jpg|.png|.gif|.jpeg|]'
``` 
