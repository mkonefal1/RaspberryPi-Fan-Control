## Script for controlling fan in Raspberry Pi by gpio (setup with transistor)

I've changed some properties to works with Celsius.

##Crontab action
Add this line to your crontab file 
```
crontab -e
```
```
* * * * * /usr/bin/python3 ~/Fantemp2.py
```
---

This python script is an alternative to the Bash script
for fan temperature control, and may serve your needs better!

Thanks to [Michael Nadler](https://github.com/mhnadler) for writing this
and allowing it to be posted here!
