# The MIT License (MIT)
#
# Copyright (c) 2019 Gregory M Paris
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`pyportal_multissid`
================================================================================

Allows PyPortal to connect to multiple SSIDs


* Author(s): Gregory M Paris

Implementation Notes
--------------------

**Hardware:**

* `Adafruit PyPortal <https://www.adafruit.com/product/4116>`_
* `Adafruit PyPortal Titano <https://www.adafruit.com/product/4444>`_
* `Adafruit PyPortal Pynt <https://www.adafruit.com/product/4465>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's PyPortal library:
  https://github.com/adafruit/Adafruit_CircuitPython_PyPortal
"""
# To add additional known networks, make changes similar to below
# in your secrets.py file. Keep what is already there, including
# entries for 'ssid' and 'password'.
#secrets = {
#    'hotspots': (
#        ('ssid2name', 'ssid2password'), # replace with your info
#        ('ssid3name', 'ssid3password'), # replace with your info
#        # repeat for any additional SSIDs
#    ),
#}

import time
from secrets import secrets
from adafruit_pyportal import PyPortal

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/gmparis/CircuitPython_pyportal_multissid.git"

# pylint: disable=too-few-public-methods, invalid-name
class PyPortal_MultiSSID(PyPortal):
    """Overrides PyPortal class method to allow for multiple SSIDs.
    """
    def _connect_esp(self):
        if self._esp.is_connected:
            self.neo_status((0, 0, 100)) # blue = connected
            return
        # Utilize base class method if there is no need for this extension.
        if 'hotspots' not in secrets \
                or secrets['ssid'] == 'CHANGE ME' \
                or secrets['password'] == 'CHANGE ME':
            super()._connect_esp()
            return
        # Construct a set of known SSIDs from secrets 'ssid' and 'hotspots'.
        # 'hotspots' must be a list of (ssid, password) tuples.
        # Repeatedly scan and attempt to connect to each until success.
        secret_list = [secrets]
        for ssid, password in secrets['hotspots']:
            secret_list.append({'ssid': ssid, 'password': password})
        want_ssids = {w['ssid'] for w in secret_list}
        while not self._esp.is_connected:
            self.neo_status((100, 0, 0)) # red = not connected
            self._esp.scan_networks()
            avail_ssids = {str(w['ssid'], 'utf-8')
                           for w in self._esp.get_scan_networks()}
            if not avail_ssids & want_ssids:
                print('No recognized networks available. Waiting...')
                time.sleep(3)
                continue
            for secret in secret_list:
                ssid = secret['ssid']
                if ssid not in avail_ssids:
                    continue
                print('Attempting connection to ' + ssid + '...')
                try:
                    self._esp.connect(secret)
                # pylint: disable=unused-variable
                except RuntimeError as error:
                    print('...retrying...')
                    time.sleep(3)
                    continue
                if self._esp.is_connected:
                    self.neo_status((0, 0, 100)) # blue = connected
                    print('...connected')
                    return  # success!
