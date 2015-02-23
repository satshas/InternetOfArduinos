# Internet of Arduinos

Internet of Arduinos (IoA for friends :) is an Internet of Things Python framework where "Things" are Arduinos, or other MCU controlled devices.

It's in a very early development stage, for now it supports basically HTTP(S) REST to Serial communication.

This framework is developed as pyDev project, so you can easily import it in Eclipse.

Here is a demonstration video: [Python Internet of Arduinos](https://www.youtube.com/watch?v=UISNnQExkLo)

# Features

* configurable HTTP server
* configurable serial connection 
* HTTP and HTTPS REST API support
* configurable REST API endpoint
* built-in Python certificate generator
* JSON response
* directly returns serial received data

# Installation

You need to install the following Python packages in order to execute IoA:

    $ pip install web.py
	$ pip install pyOpenSSL
	$ pip install pySerial

You need to be sudo on Linux. 

If pyOpenSSL fails to install on debian based Linux distros with error: 

error: Setup script exited with error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

you'll need to install these:

	$ sudo apt-get install libffi-dev
	$ sudo apt-get install libssl-dev
	$ sudo apt-get install python-dev

# How to use

Before execution you may want to look at configuration file in order to change something.

Here is an example of **config.xml**:

```xml
    <?xml version="1.0" encoding="UTF-8"?>
	<config>
		<server>
			<network port="8080" hostname="127.0.0.1"/>
			<url path="/2serial" parameter="data"/>
			<!-- <ssl certificate="../../myapp.crt" key="../../myapp.key"/> -->
		</server>
		<serial port="/dev/ttyACM0" speed="9600" wait_for_response="True"/>
	</config>
```

To execute the web server just launch **main.py** with:

$ PYTHONPATH=/path/to/IoA python main.py

or execute it with pyDev inside Eclipse.

# License

This work is licensed under [LGPL v2.1](https://www.gnu.org/licenses/lgpl-2.1.html)
