DP-WH-PS5 USB Events 
=============

Basically DP-WH-PS5 communicates the buttons pressed by the user via the USB adapter

Now, would it be possible to read this data from the USB adapter in Windows?
I think the answer is yes, using wireshark and its USBPcap add-on we can intercept
the packets that are sent from the USB adapter to the host (your pc). 

I really have no idea what this would be for possibly to enable spatial audio features, to change the audio output when turning the headset on or off, 
or to balance the audio coming from any voice chat program (Discord) and any other program.

Intercepted packages 
* Headset connection
* headset disconnection
* Headset volume up
* lower headset volume
* Activate headset microphone
* Deactivate headset microphone
* Increase sound volume Game
* Low game sound volume (Increase chat sound volume)

Searching a bit I found the pywinusb.hid project and its raw_data.py example is perfect to read HID events with python
https://github.com/rene-aguirre/pywinusb

![CHEEMS BONK](https://media1.tenor.com/images/4dee992174206c66cb208bee31174b8d/tenor.gif?itemid=18805247)
