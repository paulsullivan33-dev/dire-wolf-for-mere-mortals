# Packet Radio and AX.25

By the end of this chapter you can look
at a raw packet line and name its parts:
who sent it, who it is for, which relays
it asks for, and where the payload
begins. Everything later — APRS, the
configuration file, the troubleshooting —
stands on this one page of mechanics.

## The problem a TNC solves

A voice radio moves sound. A computer
moves bytes. Packet radio's founding
trick is to make bytes into sound sturdy
enough to survive a noisy radio channel:
send one of two tones for a **mark** bit
and the other for a **space** bit, a few
hundred or thousand times a second. At
1200 **baud** — the rate almost all VHF
packet uses — the tones are 1200 Hz and
2200 Hz, the **Bell 202** standard, a
scheme called **AFSK**: audio frequency
shift keying. The receiving end listens
for which tone is playing, recovers the
bits, and rebuilds the bytes. Faster
packet exists — 9600 baud replaces the
tones with the data signal shaping the
radio's frequency directly — but 1200
baud AFSK is the dialect APRS speaks,
and the one this guide stays with.

## AX.25, the envelope

Bits alone are not a conversation. The
protocol that frames them is **AX.25**, a
descendant of the wired X.25 protocol,
adapted for a medium where anyone can
transmit and nobody owns the channel. An
AX.25 **frame** — one packet — carries:

- **Addresses.** A destination and a
  source, each a call sign plus an
  **SSID**: a number from 0 to 15 riding
  after a dash, so one licensee's several
  stations can be told apart (N0CALL-9
  might be the car, N0CALL-5 a sensor
  box, plain N0CALL the home station —
  the assignments are convention, not
  law). Between source and payload sit
  up to eight **digipeater addresses**:
  the relays the packet asks to be
  repeated by, in order. Chapter 10 lives
  here.
- **A control and protocol field.** APRS
  rides in **UI frames** — unnumbered
  information frames: fire-and-forget
  broadcasts with no connection, no
  acknowledgement at this level, no
  guarantee. A beacon does not know or
  care who heard it. (AX.25 also defines
  connected mode, a polite two-way
  session older packet BBSs used; APRS
  does not, and this guide does not
  either.)
- **The information field.** The payload:
  up to 256 bytes that are the actual
  message — in APRS, one line of text in
  a strict format (chapter 3).
- **A checksum.** A 16-bit **FCS** —
  frame check sequence — computed over
  the whole frame. The receiver computes
  it again; if the two disagree, the
  frame is dropped silently. This is why
  a slightly-too-noisy packet does not
  arrive slightly wrong. It does not
  arrive.

On the air the frame is wrapped for the
radio's sake: flag bytes mark its start
and end, extra bits are stuffed in so
the data cannot imitate a flag, and the
bit stream is encoded (**NRZI**) so the
tones carry the clock as well as the
data. You will never type any of that.
Dire Wolf and every other TNC do it for
you — but when chapter 6 talks about
audio, this is the machinery the audio
feeds.

## What Dire Wolf adds as a modem

A hardware TNC of 1990 did exactly this
and no more. Dire Wolf cheats, legally,
in three ways worth knowing:

- **Several demodulators at once.** For
  each channel it runs more than one
  decoding profile over the same audio —
  the lab's transcripts show profiles
  labelled A and A+ — and keeps the copy
  whose checksum passes. Real signals
  arrive with twist, drift and distortion;
  different decoders forgive different
  sins.
- **A second chance for broken frames.**
  `atest` reports a **Fix Bits level** on
  every run; at level 0, the lab's
  setting, nothing was repaired — frames
  passed or failed as received. The
  documentation describes optional repair
  of frames with one or two wrong bits,
  verified against the checksum after
  the flip. The lab left it off, so what
  you see in its transcripts is the
  decoder unassisted.
- **Honest reporting.** Every decoded
  packet is printed with the audio level
  it was heard at. Chapter 6 is built on
  that one number.

Check: the lab's loop (transcripts
`dire-wolf-lab/transcripts/t01-gen-packets.txt`
and `t02-atest-decode.txt`) took six
written frames through modulation and
back, and `atest`'s summary reads "6
packets decoded" — the checksums agreed
at both ends, which is the whole of this
chapter demonstrated in one line.

## The written form

On paper — in logs, in Dire Wolf's
output, in this guide — a frame is
written in **TNC-2 style**, the monitor
format every packet program understands:

```text
SOURCE>DESTINATION,PATH:payload
```

Read the lab's first packet once more,
with names on the parts:

```text
N0CALL>APDW17,WIDE2-2:!4449.98N/08930.02W# Bramble Hill lab site - fictional
```

- `N0CALL` — the source. (The placeholder.
  Chapter 1 has already scolded it.)
- `APDW17` — the destination field. In
  APRS this is rarely a station; it is a
  label naming the software or device
  that made the packet — here, Dire Wolf
  version 1.7.
- `WIDE2-2` — the path: the relays
  requested. *WIDE2-2* asks wide-area
  digipeaters to repeat it, twice over.
  Chapter 10 explains the arithmetic.
- Everything after the colon is payload:
  a position and a comment, in APRS's
  compressed little grammar — the whole
  of chapter 3.

Hold on to that shape. Every packet in
this guide, heard or invented, has it.
