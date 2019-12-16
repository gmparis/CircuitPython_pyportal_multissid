"""Simple test of PyPortal_MultiSSID
"""

# This test requires a secrets.py file on your PyPortal.
# At a minimum, the secrets dictionary in that file will contain:
#   * Your Adafruit IO username and key, required for get_local_time()
#   * The ssid and password of your "home" network.
#   * A hotspots entry that will be a list of ssid/password tuples
#       corresponding to "away" networks, such as your phone operating
#       as a hotspot, a "MiFi" device, or any other place you expect
#       the device to operate.
# Note: Places like hotels and Starbucks are not supported because
#   they require visiting a sign-in page and interacting with it.
#   This class is for known, passphrase-protected networks with
#   no web-based sign-in.

import time
import board
from pyportal_multissid import PyPortal_MultiSSID

# PyPortal_MultiSSID class is invoked exactly the same way as PyPortal.
pyportal = PyPortal_MultiSSID(status_neopixel=board.NEOPIXEL)
while True:
    try:
        pyportal.get_local_time()
    except RuntimeError:
        print('get_local_time failed...')
    time.sleep(60)

