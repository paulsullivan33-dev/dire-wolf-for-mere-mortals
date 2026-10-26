# The Configuration File

One plain text file describes the whole
station: who it is, where its radio is,
how fast to talk, what to repeat, where
its doors are, what to announce. This
chapter walks the lab's file —
`dire-wolf-lab/direwolf.conf`, kept in
the repository — section by section, and
then runs it, because the parser has
opinions and they are worth hearing.
Outcome: you can write a configuration
of your own, and read Dire Wolf's
complaints about it like sentences,
because they are.

## MYCALL — who the station is

```text
MYCALL N0CALL
```

One line, and the most consequential in
the file. Every packet the station
*bothers* to originate, repeat or gate
carries this call sign (plus an SSID,
written `MYCALL N0CALL-1` style, when a
station needs one). The lab's value is
the placeholder on purpose — `N0CALL` is
what Dire Wolf's own examples print for
"not set yet" — and chapter 1 has
already shown what the program thinks of
it. Yours is your real call sign. There
is no second step where it asks again.

## ADEVICE and ACHANNELS — where the radio is

```text
ADEVICE plughw:1,0
ACHANNELS 1
```

**ADEVICE** names the sound device:
here an ALSA address, card 1, device 0 —
the shape a USB radio interface takes on
Linux. A machine with one built-in sound
card and one USB interface usually wants
the USB one, and the project's
documentation shows how to list devices
and pick. **ACHANNELS** says how many
radio channels ride on that device: 1 for
one radio on a mono or stereo pair used
together; a stereo device can carry two
radios, one per side, which is how one
computer runs a 2-metre and a 70-centimetre
station side by side. The lab machine
has no sound card at all — remember that
when the run comes.

## CHANNEL and MODEM — how fast, which tones

```text
CHANNEL 0
MODEM 1200
```

Each block starting **CHANNEL** defines
one radio channel: its audio, its speed,
its push-to-talk. **MODEM 1200** is the
VHF standard of chapter 2 — AFSK at 1200
baud. The same line takes 300 (HF
packet, different tones), 2400, 4800 and
9600 (which expects a radio's flat
*discriminator* audio rather than its
speaker output — chapter 6 returns to
why). A block can also carry the **PTT**
line — which serial line, GPIO pin or
rig-control path keys the transmitter.
The lab file omits it, there being no
transmitter; the null-device run
(transcript t07, chapter 7) shows Dire
Wolf noticing the omission and carrying
on, because a receive-only station
needs no key.

## DIGIPEAT — one rule of the repeater

```text
DIGIPEAT 0 0 ^WIDE[3-7]-[1-7]$ ^WIDE[12]-[1]$
```

One line turns the station into a
digipeater. It reads: *for packets
arriving on channel 0 and leaving on
channel 0, repeat those whose path asks
for it, under these patterns* — the
patterns here are the fill-in WIDE
behaviour the project documentation
recommends, and chapter 10 explains the
paradigm they implement. What matters in
this chapter is that the line is
*accepted or rejected by the parser like
everything else*, and that Dire Wolf
cross-checks it against MYCALL before
arming anything. Hold that thought for
the run below.

## AGWPORT and KISSPORT — the doors

```text
AGWPORT 8000
KISSPORT 8001
```

Two lines open the doors of chapter 7 on
their standard numbers: 8000 for AGW
clients, 8001 for KISS over TCP. They
cost nothing while nothing connects. A
serial KISS port or the pseudo-terminal
door are alternative lines, documented
in the project manual and not used here.

## PBEACON — what the station announces

```text
PBEACON delay=1 every=30 overlay=S symbol="digi" lat=44.8330 long=-89.5003 comment="Bramble Hill lab site - fictional"
```

One long line is one beacon: wait
`delay` minutes after starting, repeat
`every` so often (times are minutes, or
minutes:seconds), at this position, with
this map symbol and comment. Chapter 12
takes beacons apart properly — including
the other kinds, for objects and for
trackers that move. Here it completes
the file: identity, audio, channel,
repeater rule, doors, announcement. A
station entire, in forty lines with its
comments.

## The run: the parser reads it aloud

Transcript `dire-wolf-lab/transcripts/t05-config-parse.txt`,
against this exact file:

```text
Reading config file direwolf.conf
Config file: MYCALL must be set for channel 0 before beaconing is allowed.
Config file: MYCALL must be set for receive channel 0 before digipeating is allowed.
Config file: MYCALL must be set for transmit channel 0 before digipeating is allowed.
Config file: Beaconing should be configured for channel 0 when digipeating is enabled.
Audio device for both receive and transmit: plughw:1,0  (channel 0)
ALSA lib confmisc.c:165:(snd_config_get_card) Cannot get card index for 1
Could not open audio device plughw:1,0 for input
Pointless to continue without audio device.
```

Read it as three acts. **Nothing in the
file was rejected**: every line parsed,
including the digipeater rule and the
long beacon. **The cross-checks ran**:
because `N0CALL` counts as unset, the
beacon is disarmed and the digipeater is
disarmed on both its receive and
transmit sides, and the fourth message
notes the pairing looks incomplete —
four sentences, one cause, all of them
chapter 1's rule wearing overalls.
**Then the hardware is consulted**, and
the machine's missing sound card ends
the run. On a real station the same
script continues to the channel summary
and the doors opening — transcript t07
shows that second half, against the
silent software device.

And the parser is as plain about syntax
as about sense. Transcript t06 changed
one letter — `MYCALL` to `MYCAL`, with
`sed` — and got:

```text
Config file: Unrecognized command 'MYCAL' on line 10.
```

It names the word and the line. When
Dire Wolf refuses your file, it is
rarely being mysterious; it is being
*literal*, and the fix is usually the
one it just described.

Check: run your own file the same way.
You have passed this chapter when the
only remaining complaint is about
hardware you have genuinely not
connected — or, better, when there are
no complaints and two doors are open.
