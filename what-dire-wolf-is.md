# What Dire Wolf Is

In the 1980s, amateurs began sending data
over ordinary voice radios. The radio
knows only audio, so something had to sit
between the computer and the microphone
socket: a **TNC**, a terminal node
controller — a small computer in a box,
whose whole job was turning text into
two alternating tones for transmitting,
and tones back into text on receive. The
protocol it spoke is **AX.25**, packet
radio's link language, and the best-known
service built on it is **APRS**, the
Automatic Packet Reporting System:
stations beaconing their position,
weather, short messages and sensor
readings, repeated across the countryside
by other stations acting as relays.

**Dire Wolf is a TNC that is software.**
It runs on an ordinary computer — a
laptop, a desktop, a Raspberry Pi — and
uses a sound device as its radio
interface. Fed audio from a receiver, it
decodes AX.25 frames and prints them as
readable packets. Handed a packet to
send, it generates the tones and keys the
transmitter. Around that modem core it
grows the rest of a packet station: a
**digipeater** that repeats other
stations' packets, an **igate** that
carries traffic between radio and the
APRS internet system, beaconing,
telemetry, and two well-known doors —
**KISS** and **AGW** — through which
other programs use it as their modem.
It is free and open source, written by
John Langner, WB2OSZ, and named, in the
project's own joke, because a dire wolf
has very good hearing.

## Why anyone would do this

- **Joining APRS cheaply.** A radio, a
  computer you already own, and an audio
  cable are a working APRS station: your
  position on the map, messages to other
  stations, weather from your own
  sensors. The TNC is the free part.
- **A digipeater or igate for your
  area.** Hilltop relays and internet
  gateways are amateur radio's shared
  plumbing, and most of them are one
  volunteer's small computer running
  software like this (chapters 10
  and 11 — including the duties).
- **Understanding by hearing.** Packet
  radio is unusually legible: every
  packet is printed whole, addresses,
  path, payload and all. Running a
  decoder against traffic — or against
  recordings, as this guide's lab does —
  teaches the protocol faster than any
  diagram.
- **A modem for other programs.** Map
  clients, logging tools and trackers
  speak KISS or AGW. Dire Wolf is the
  ears and mouth they share (chapter 7).

## The rule, stated before everything else

A receive-only station harms no one. The
moment your station transmits — a beacon,
a repeated packet, a message gated from
the internet — it is radio transmission,
with everything that has always meant:

> **Transmit only with an amateur
> licence, under your own call sign,
> on frequencies and with modes your
> licence allows.**

Dire Wolf enforces a small, telling piece
of this itself. Its configuration takes
your call sign in **MYCALL**, and it
ships with the placeholder **N0CALL** —
which is not a call sign, and Dire Wolf
treats it as "not set". In this guide's
lab (chapter 5), running under the
placeholder earned four plain warnings:

```text
Config file: MYCALL must be set for channel 0 before beaconing is allowed.
Config file: MYCALL must be set for receive channel 0 before digipeating is allowed.
Config file: MYCALL must be set for transmit channel 0 before digipeating is allowed.
```

The software will happily decode all day
as nobody; it will not beacon or repeat
as nobody. That is the correct instinct,
and this guide follows it: the lab never
transmitted at all — its audio is files,
its one full start played to a silent
software sound device — and wherever a
later chapter describes transmitting, it
assumes a licensed reader using their
own call sign. The igate has its own
extension of the rule, and chapter 11
states it where it belongs: *what your
station forwards to the internet goes
out under your call sign and your
responsibility.*

## A first taste, with no radio at all

Dire Wolf ships with two tools that work
entirely in files, and this guide's lab
leaned on them hard. `gen_packets` turns
written packets into audio; `atest`
decodes audio back into packets. One
written packet from the lab:

```text
N0CALL>APDW17,WIDE2-2:!4449.98N/08930.02W# Bramble Hill lab site - fictional
```

becomes two seconds of two-tone warble in
a WAV file, and comes back out of `atest`
(chapter 8) as:

```text
[0] N0CALL>APDW17,WIDE2-2:!4449.98N/08930.02W# Bramble Hill lab site - fictional<0x0a>
```

Same line, having survived a round trip
through the same modulation a radio
would carry. Check: if those two lines
look like alphabet soup, that is expected
at this point — chapter 3 takes exactly
this line apart, field by field, and by
chapter 9 you will be writing them.

## Who it is for

The licensed amateur who wants on APRS
without buying a hardware TNC. The
volunteer keeping a district's digipeater
or igate alive. The curious listener who
wants to know what the warbling on
144.390 MHz is *saying*. The thread
through all three: one person, their own
station, and traffic they are entitled
to handle.

## What it is not

Dire Wolf is not a radio: it makes audio,
and a radio still has to carry it — with
all the wiring, levels and licensing
that implies (chapters 5 and 6). It is
not a guarantee of decodes: fed distorted
or whisper-quiet audio it fails like any
modem, and chapter 15 is honest about
where the fixing stops being software.
It is not an appliance: it runs on a
general-purpose operating system, with
updates, reboots and distractions, which
matters when a hilltop depends on it.
And it is not an excuse: "the software
sent it" has never been a defence for an
unlicensed transmission or a nuisance
beacon, and chapter 11 does not let the
igate pretend otherwise.
