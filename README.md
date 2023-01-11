# tello-fleet-shutdown

This Python script should cause any Tello Drones nearby to automatically land. It currently only works if the Drone has the default SSID and password.

# Installation

Download the <code>shutdown.py</code> file and install the corresponding dependency for your device:
<p><code>pip install winwifi</code> for Windows</p>
<p><code>pip install macwifi</code> for MacOS</p>
    
Note: If using MacOS you will also need to run the following commands in the terminal before running the script:
<p><code>cd /usr/local/bin/</code></p>
<p><code>sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport</code></p>

# Usage

Run the script using <code>python shutdown.py</code>.

This should loop through all available wireless networks and connect to each one that begins with <code>TELLO-</code>.

Once connected, it will send the land command and then move on to the next network in the list until it has caused all Tello Drones to land.
