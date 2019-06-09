# playingWithSenseHat

Playin around with a Raspberry Pi3 b+ and Sense Hat 

## File structure
```
.
├── configuration
│   ├── colorDefinitions.py
│   ├── ledImageArrays.py
│   └── __pycache__
├── LICENSE
├── README.md
├── senseHat.py
└── sensors
    ├── __pycache__
    └── sensors.py

4 directories, 6 files

```

## Getting started

The idea is to use the led arry to show infonformation from online and from the sensors.

### Prerequisites
* Physical Raspberry Pi and SenseHat
    * Raspberry Pi board
    * SenseHat board
    * Micro SD card with Raspbian

OR

* Virtualised 
    * Raspbian OS in a vm
    * Text editor of your choise
    * Sense Hat emulator

### Installing

1. Upgrade and update the os
```
sudo apt-get update
sudo apt-get upgrade
```

2. Pull the code from Git
```
git clone https://github.com/GeorgeManakanatas/playingWithSenseHat
```

3. fix Sense Hat problems
Sometimes the Sense Hat will not work properly and display a fixed rainbow pattern evena after startup. To deal with this a line meeds to be added to the /boot/config.txt file
```
nano boot/config.txt
```
At the end of the file add this line
```
dtoverlay = rpi-sense
```
and restart the installation now the leds must go dark after startup.

4. Make the code start on startup
In order to have the script run automatically on startup there needs to be an addition to the rc.local file
```
sudo nano /etc/rc.local
```
Add a command above the last line ( that should read: exit 0 ) in order to run the script
```
sudo python3 /path/to/the/file/senseHat.py &
```
It is importanty to not forget the & at the end in order to ecape the command.

## Liscense
This project is liscenced under the MIT Liscense - see [LICENCE](LICENCE) file for details
## Acknowledgements

