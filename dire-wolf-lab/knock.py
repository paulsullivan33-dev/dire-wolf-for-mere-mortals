"""Knock on Dire Wolf's two doors (chapter 7, transcript t07).

Run while Dire Wolf is up with null.conf. The KISS door
is spoken properly: one frame -- FEND, a port-0 data
command byte, the payload, FEND. The payload is plain
text, not an AX.25 frame; Dire Wolf will say exactly
that when it queues it, which is part of the evidence.
The AGW door is only connected to: this script does
not speak the AGW protocol, and Dire Wolf's log shows
what it makes of a client that connects and then says
nothing it can parse. The port numbers match null.conf
-- the standard 8000/8001 moved up by 10000, because
the lab machine already had a program on 8000.
"""

import socket

# KISS door.
frame = bytes([0xC0, 0x00]) + b"LABTEST off-air KISS door check" + bytes([0xC0])
s = socket.create_connection(("127.0.0.1", 18001), timeout=3)
s.sendall(frame)
print("KISS 18001: connected, sent one 34-byte frame")
s.close()

# AGW door: connect only.
a = socket.create_connection(("127.0.0.1", 18000), timeout=3)
print("AGW 18000: connected")
a.close()
