Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-pyportal_multissid/badge/?version=latest
    :target: https://circuitpython-pyportal_multissid.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/gmparis/CircuitPython_pyportal_multissid.svg?branch=master
    :target: https://travis-ci.com/gmparis/CircuitPython_pyportal_multissid
    :alt: Build Status

Allows PyPortal to connect to multiple SSIDs


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython PyPortal <https://github.com/adafruit/Adafruit_CircuitPython_PyPortal>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Usage Example
=============

This module implements a child class build upon Adafruit's PyPortal class.
The class implements just one method, overriding a base method, allowing
the PyPortal device to connect to more than one SSID. To use, invoke this
class where you would have used the PyPortal class. For example:

.. highlight:: python
    from pyportal_multissid import PyPortal_MultiSSID
    pyportal = PyPortal_MultiSSID(status_neopixel=board.NEOPIXEL)

Configure your "home" SSID as 'ssid' and 'password' as usual in your secrets file,
then add any additional networks (such as phone hotspot, "MiFi" devices,
or networks at other places you frequent) as described below.
The PyPortal then becomes portable.

The alteration of your secrets.py file is to include one extra key/value pair.
The key is 'hotspots' and the value is a list of paris ssid and password strings.
In the snippet below, lists are used, though tuples may be more economical.

.. highlight:: python
    secrets = {
        'hotspots': [
            ['myphonessid', 'thepassword'],
            ['mymifissid', 'itspassword'],
            ['myvacationhomessid', 'dontyouwish'],
        ],
    }

See examples/pyportal_multissid_simpletest.py

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/gmparis/CircuitPython_pyportal_multissid/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
