# KISS and AGW — The Two Doors

A modem that only its own screen can use
is a dead end. Dire Wolf's real working
life is as the shared ears and mouth for
other programs — the map client that
draws stations, the tracker that reports
a balloon, the message program that
types. Those programs do not share
Dire Wolf's terminal. They knock on one
of two doors, and this chapter opens
both, in the lab, with a ten-line script
standing in for a real client. Outcome:
you know what a client actually hands
the modem — a frame, nothing more
magical — and where the modem's
responsibility ends.

## KISS: the frame, the whole frame

**KISS** — Keep It Simple, Stupid — is a
protocol from packet radio's early years
(Mike Chepponis, K3MC, and Phil Karn,
KA9Q), and it is barely a protocol at
all. The host program composes a
complete AX.25 frame, wraps it in a
**FEND** byte (0xC0) at each end with one
command byte after the first FEND — low
nibble 0 means "this is data" — and
sends the bytes to the TNC. The TNC's
job shrinks to modulation and keying:
the intelligence lives in the program,
the modem is a pipe with tones. KISS
arrives over a serial port, over a
pseudo-terminal (Dire Wolf's `-p`), or —
the shape the lab used — over **TCP**,
default port 8001, opened by the
**KISSPORT** line of chapter 5.

## AGW: the richer door

**AGW** is the protocol of AGWPE, George
Rossopoulos's (SV2AGW) long-lived Windows
packet engine, and half the packet
software ever written learned to speak
it. Where KISS hands over raw frames,
an AGW client registers its call sign
with the engine and exchanges structured
messages — connect, send data, report
what was heard — each behind a fixed
**36-byte header**. Dire Wolf implements
the engine's side of the conversation:
**AGWPORT** (default 8000) opens the
door, and clients written for AGWPE find
a familiar landlord. Same modem behind
both doors; the difference is how much
of AX.25 the client wants to own.

## The lab knocks

The lab machine has no radio, so this
run used the configuration variant
`dire-wolf-lab/null.conf`: the ALSA
**null** device, a software sound card
that discards its input and hears
silence, standing where the radio would
be. (One wrinkle, recorded honestly: the
build machine already had a program on
port 8000, so `null.conf` moves both
doors up — AGW on 18000, KISS on 18001.
The numbers are configuration, not
doctrine.) Transcript
`dire-wolf-lab/transcripts/t07-kiss-and-agw.txt`
is the run, and the top of it is the
second half of chapter 5's story — with
an audio device that opens, Dire Wolf
completes its start:

```text
Audio device for both receive and transmit: null  (channel 0)
Channel 0: 1200 baud, AFSK 1200 & 2200 Hz, A+, 44100 sample rate.
Note: PTT not configured for channel 0. (Ignore this if using VOX.)
Ready to accept AGW client application 0 on port 18000 ...
Ready to accept KISS TCP client application 0 on port 18001 ...
```

Then `dire-wolf-lab/knock.py` knocks.
On the KISS door it speaks properly —
one frame, FEND-wrapped, a plain-text
payload — and Dire Wolf's debug log
shows the frame arriving whole:

```text
Attached to KISS TCP client application 0 on port 18001 ...
<<< Data frame from KISS client application, channel 0, total length = 34
  000:  c0 00 4c 41 42 54 45 53 54 20 6f 66 66 2d 61 69  ..LABTEST off-ai
  010:  72 20 4b 49 53 53 20 64 6f 6f 72 20 63 68 65 63  r KISS door chec
  020:  6b c0                                            k.
```

and then the modem doing the only job
KISS leaves it — queuing the frame for
the transmitter, with an honest
annotation, since the lab's payload was
text rather than a composed AX.25 frame:

```text
[0L] (Not AX.25)LABTEST off-air KISS door check
```

The AGW knock is the counter-lesson.
`knock.py` merely connects — speaks no
AGW — and Dire Wolf attaches the client,
waits for its first 36-byte header, and
gives up in writing:

```text
Attached to AGW client application 0...
Error getting message header from AGW client application 0.
Tried to read 36 bytes but got only 0.
Closing connection.
```

A door is not a conversation. Chapter 13
puts real clients on these doors; the
lab's point is smaller and load-bearing —
both doors are real, frames cross them
unchanged, and the modem neither knows
nor cares what program sent them. (One
quirk the same transcript shows: this
build also announced a KISS listener on
the default 8001 alongside the
configured 18001. The lab knocked only
on the door it configured.)

Check: with your own station running,
`kissutil` — the fifth tool of chapter 4 —
exchanges frames with a KISS port from
files, and is the quickest way to prove
the door works before blaming a client.
What the lab proved stands in for it
here: a frame offered at the door was
received, dumped byte for byte, and
queued — by a modem playing to an empty
room, on a machine with no radio at all.
