DP-WH-PS5 USB Events 
==============
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

![Screenshot_20221222-191841_WhatsApp](https://user-images.githubusercontent.com/70771067/210198015-92393df4-f2cd-4876-ae1a-201b318619cd.jpg)
