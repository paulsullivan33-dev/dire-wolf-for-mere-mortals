# Limits

What Dire Wolf cannot do, and what it
must not be asked to do — the chapter
the rest of the guide has been
promising.

## It is not a radio

Everything Dire Wolf knows arrives as
audio through a sound device, and
everything it says leaves the same way.
It cannot hear a signal the receiver
never delivered — squelch shut, wrong
socket, a data port whose 1200-baud pin
you did not use — and it cannot be heard
beyond whatever the transmitter does
with its tones. Chapter 6's whole
discipline exists because the failure
modes live on the *analog* side of the
line, where no release notes apply.

## Software cannot un-distort

The several demodulators and the
optional bit repair of chapter 2 buy
real margin — decodes from signals a
simpler modem loses. They do not buy
indulgence. Audio clipped flat by an
overdriven interface, tones twisted by
the wrong tap, a channel full of
collisions: the checksum still votes,
and its majority is *no*. The lab's
noise file is the honest scale of it —
with clean generated audio the same
decoder took 6 of 6, and with noise
poured in it took 9 of 12 and would
take none of a worse file. Decoding is
recovery, not resurrection.

## A computer is not an appliance

A hardware TNC on a hilltop fails about
never. Dire Wolf runs on an operating
system: it can be rebooted by an update,
starved by a runaway log, killed by a
failing SD card, orphaned by a power
cut that corrupts the one file that
mattered. None of that is a defect —
the flexibility is the point — but a
digipeater or igate that a district
relies on is an *operations* problem,
not an install: watchdogs, backups of
the configuration, a way to reach the
site, and an owner who notices silence.
Chapter 11's duties assume a station
that stays up; keeping it up is yours.

## The doors do not check ID

Chapter 7's evidence cuts both ways. A
frame handed to the KISS door was
queued for transmission, unexamined —
`[0L] (Not AX.25)` and all. Dire Wolf's
own protections (chapter 1) govern the
packets *it* composes: beacons,
digipeating, gating. Frames composed by
a client are the client's compositions,
transmitted under the station's call
sign the moment they leave the door.
So the security of a Dire Wolf station
is the security of every program and
account that can reach its ports on
that machine — bind the doors to
localhost unless you mean otherwise,
and treat a new client program with
the suspicion you would give anything
that can key your transmitter, because
it can.

## APRS's own limits are inherited

No configuration fixes the protocol:
positions are public and permanent,
messages carry no promise of delivery,
encryption is prohibited on the amateur
bands in any case, and the channel is
one shared frequency where your
station's politeness is other stations'
bandwidth. And the legal edges vary by
country — third-party traffic, automatic
control of unattended stations,
identification intervals — in ways a
guide cannot flatten into one rule: the
rule of chapter 1 (licensed, your call
sign, your responsibility) is the floor,
and your own licence conditions are
the rest of the building.

Finally, the limit this guide imposed
on itself: its lab never transmitted,
never connected a radio, never ran the
digipeater or the igate it describes.
Those chapters are the documentation's
behaviour, honestly labelled, checked
against the software everywhere the
software could be made to speak without
a radio. The day you wire one up, your
station's transcripts outrank this
book's — which is, in the end, the
attitude the whole series is trying to
teach.
