# Glossary

**AGW** — the host protocol of the AGWPE
packet engine: structured messages
behind a 36-byte header, by which client
programs use a modem (chapter 7).
Dire Wolf's AGW door is **AGWPORT**,
default 8000.

**AFSK** — audio frequency shift keying:
data sent as two alternating tones —
at 1200 baud, 1200 Hz and 2200 Hz, the
Bell 202 pair (chapter 2).

**APRS** — the Automatic Packet
Reporting System: stations publishing
positions, objects, messages, status
and telemetry as AX.25 broadcasts
(chapter 3).

**APRS-IS** — the APRS internet system:
the network of servers that gather
every igate's heard packets into one
worldwide stream (chapter 11).

**atest** — the project's bench
decoder: a WAV file in, decoded packets
out, at many times real speed
(chapter 8).

**AX.25** — the link-layer protocol of
amateur packet radio: addressed frames
with a checksum, carried as tones
(chapter 2).

**Beacon** — a packet a station sends
on a schedule to announce itself: a
position (PBEACON), an object
(OBEACON), or a moving tracker's
position (TBEACON) (chapter 12).

**Call sign / MYCALL** — the station's
licensed identity, set by the
configuration's **MYCALL** line. The
placeholder `N0CALL` means "not set",
and Dire Wolf will not beacon or
digipeat under it (chapters 1 and 5).

**Checksum (FCS)** — the frame check
sequence: a 16-bit sum over the frame.
Receiver and sender must agree, or the
frame is dropped entire (chapter 2).

**Data type identifier** — the first
character of an APRS payload, naming
its kind: `!` position, `;` object,
`:` message, `>` status, `T` telemetry
(chapter 3).

**decode_aprs** — the project's
explainer: one written packet in, a
plain-language reading out (chapter 3).

**Digipeater** — a station that repeats
packets whose path asks it to, so they
travel further than one radio hop
(chapter 10).

**Discriminator** — a radio's raw,
unfiltered receiver audio, tapped for
9600-baud packet; the filtered,
de-emphasised path serves 1200 baud
(chapter 6).

**FEND** — the frame-end byte (0xC0)
that wraps a KISS frame at both ends
(chapter 7).

**Fill-in digi** — a small digipeater
serving one-hop `WIDE1-1` requests,
lifting weak local stations to a wide
digipeater's earshot (chapter 10).

**Frame** — one complete AX.25 packet:
addresses, control, payload, checksum
(chapter 2).

**gen_packets** — the project's file
modulator: written packets in, packet
audio (a WAV) out (chapter 9).

**Igate** — an internet gateway
station: hears APRS on radio, posts it
to the APRS-IS, and (two-way) transmits
internet-side messages addressed to
locally heard stations (chapter 11).

**KISS** — Keep It Simple, Stupid: the
minimal host protocol that hands a TNC
complete frames, FEND-wrapped, and
leaves it only the tones (chapter 7).
Dire Wolf's TCP KISS door is
**KISSPORT**, default 8001.

**kissutil** — a small companion tool
for exchanging frames with a KISS port
through files (chapter 7).

**Mark and space** — the two tone
states of AFSK, one per bit value
(chapter 2).

**Null device** — ALSA's software sound
device that discards output and hears
silence; the lab's stand-in radio
(chapters 5 and 7).

**Object** — an APRS position report
that speaks for a thing without a
radio — a repeater, a summit — under a
name, kept true by the station that
sends it (chapters 3 and 12).

**Passcode** — the number an igate
presents to the APRS-IS, computed from
its call sign by a published algorithm:
an identifier, not a secret
(chapter 11).

**Path** — the list of relay requests
in a packet (`WIDE1-1`, `WIDE2-2`):
which digipeaters are asked, and how
many hops remain (chapters 2 and 10).

**PTT** — push-to-talk: the signal that
keys the transmitter, by serial line,
GPIO pin, USB interface or rig control
— or, makeshift, VOX (chapters 5
and 6).

**SSID** — the number after the dash in
an address (0–15), distinguishing one
licensee's stations: `-9` often a car,
`-5`, in this guide's fixture, a sensor
box (chapter 2).

**Symbol** — the map icon for a
station or object, chosen by a table
character and a code character inside
its position (chapter 3).

**Telemetry** — an APRS report of five
analog values and eight digital bits,
given names, units and scaling by the
station's PARM, UNIT, EQNS and BITS
messages (chapters 3 and 12).

**TNC** — terminal node controller: the
box, or in Dire Wolf's case the
program, that turns text into tones and
tones into text between computer and
radio (chapter 1).

**Twist** — the two AFSK tones arriving
at unequal strength, tilted by the
radio's audio path; Dire Wolf prints
both readings with each decode
(chapter 6).

**UI frame** — an unnumbered
information frame: a broadcast with no
connection and no acknowledgement at
the link level. APRS rides entirely in
UI frames (chapter 2).
