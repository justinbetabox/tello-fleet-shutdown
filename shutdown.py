from sys import platform
import socket
import threading
import time

if platform == "darwin":
    import macwifi
elif platform == "win32":
    import winwifi

def get_aps():
    output_data = []
    if platform == "darwin":
        output = macwifi.list()
        output_lines = output.split("\n")[1:-1]
        for each_line in output_lines:
            split_line = [e for e in each_line.split(" ") if e != ""]
            if (split_line[0].startswith("TELLO-")):
                output_data.append(split_line)
    elif platform == "win32":
        output = winwifi.WinWiFi.scan()
        for network in output:
            if network.ssid.startswith("TELLO-"):
                output_data.append(network.ssid)
    return(output_data)

def connect(ssid):
    if platform == "darwin":
        macwifi.connect(ssid[0], "")
    elif platform == "win32":
        winwifi.WinWiFi.add_profile(ssid)
        winwifi.WinWiFi.connect(ssid, "")


# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding="utf-8"))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock.close()
      print("Error receiving: " + str(e))
      break


# IP and port of Tello
tello_address = ("192.168.10.1", 8889)

# IP and port of local computer
local_address = ("", 9000)

ssids = get_aps()

for ssid in ssids:
    connect(ssid)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the local address and port
    sock.bind(local_address)

    # Create and start a listening thread that runs in the background
    # This utilizes our receive functions and will continuously monitor for incoming messages
    receiveThread = threading.Thread(target=receive)
    receiveThread.daemon = True
    receiveThread.start()

    send("command", 0)
    send("land", 0)