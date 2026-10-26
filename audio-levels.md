# Audio Levels, Honestly

Ask a room of packet operators why a
station does not work and the room says
one word: *levels*. The modem can be
perfect and the configuration flawless,
and if the audio arriving at it is a
whisper or a shout, the checksums fail
and the channel is silent. This chapter
is the honest version: what the level
does at both extremes, where a radio
offers its audio, and the gift Dire Wolf
gives you — a number, printed on every
single decode, that tells you where you
stand. Outcome: "it doesn't decode"
becomes a measurement instead of a mood.

## What the level does to the tones

Chapter 2's two tones have to survive
an FM radio, and FM adds its own rules.

- **Too quiet.** The tones sink towards
  the hiss. Bits blur; the checksum
  disagrees; frames vanish *silently* —
  nobody announces a near-miss. A quiet
  station looks exactly like an empty
  channel.
- **Too loud.** The transmitter
  **over-deviates** — the tones swing
  the carrier wider than the channel
  allows — and the audio chain clips,
  flattening the tones into something
  nearer square waves. Distorted tones
  decode badly at the far end and splash
  energy where neighbours live. A loud
  station is worse than a quiet one: it
  fails *and* it interferes.
- **Twisted.** Radios do not treat the
  two tones equally: FM's pre-emphasis
  and de-emphasis tilt them, so 1200 Hz
  and 2200 Hz can arrive at noticeably
  different strengths — **twist**. Good
  decoders tolerate some. Dire Wolf
  prints both tones' readings so you can
  see it (below).

There is no software setting that undoes
any of these at the source. There is
only getting the level right, which is
why this chapter exists.

## The number Dire Wolf gives you

Every decode carries its reading —
transcript `dire-wolf-lab/transcripts/t02-atest-decode.txt`:

```text
DECODED[1] 0:00.792 N0CALL audio level = 50(14/14)
```

A headline level, and in brackets the
two tones side by side: equal brackets,
a balanced signal. The lab's generated
audio reads a steady **50**, which is
the neighbourhood the project's
documentation steers you towards —
mid-scale, well clear of both the noise
floor and the clipping wall. (These are
file readings, not radio readings: the
lab had no radio, and the number means
the same thing in both places because
the decoder cannot tell where audio came
from.)

The noise run teaches the second half of
the lesson. In transcript t04, twelve
packets were generated with rising noise
added — and the readings on the ones
that still decoded *climbed*: 57, 66,
75, 84 and on, past 100. Noise is energy;
the meter counts it. So a level can be
"good" and the signal still drowning —
which is why three of the twelve never
decoded at all. Read the number as
*necessary, not sufficient*: mid-scale
and steady across similar stations is
healthy; mid-scale is not a promise.

## Where a radio offers its audio

Three sources, in the order a fixed
station should prefer them:

- **The data port.** Most mobile and
  base radios offer a packet/data socket
  with a **fixed-level** receive output —
  it ignores the volume knob, which is
  exactly what a modem wants: set the
  level once, and nobody's elbow changes
  it. Such ports usually carry two grades
  of audio: a 1200-baud pin (filtered,
  de-emphasised — right for this guide)
  and a 9600-baud pin (flat
  **discriminator** audio — right only
  for 9600). Using the wrong pin is a
  classic: 9600 into the filtered path
  decodes nothing, and now you know why.
- **The speaker or headphone socket.**
  Works, and beginners start here — but
  the level follows the volume knob, the
  audio has been through the radio's
  speech processing, and every listener
  who adjusts the volume re-tunes your
  modem. If you use it, mark the knob.
- **An interface in the middle.** The
  common station shape is radio → a small
  USB interface (sound device plus a
  **PTT** line that keys the transmitter)
  → computer. The interface's whole
  purpose is stable levels and clean
  keying; Dire Wolf's configuration
  names it as the ADEVICE and the PTT
  device (chapter 5). **VOX** — letting
  the sound of the tones key the radio —
  is the makeshift to avoid for packet:
  it wakes slowly, eats the start of
  transmissions, and hangs on noise.

This section is documented, not run: the
lab had no radio to wire. The wiring
diagrams for specific radios live in the
project documentation and the radio
manuals, and this guide will not invent
pinouts (README, "What it doesn't
cover").

## Setting a station by its numbers

For a real station, the working loop the
documentation teaches — and the lab's
file work rehearses — is:

1. Receive first. Watch the levels on
   stations you hear: similar stations at
   similar strength should read in the
   same mid-scale band, brackets roughly
   equal. One station far hotter than the
   rest is *their* problem; everything
   far from mid-scale is yours.
2. Adjust at the source — the interface's
   level controls or the radio's data
   port drive — not by shouting in
   software afterwards.
3. Transmit into a dummy load or a quiet
   frequency with a second receiver if
   you can, and set your own tones to be
   heard the way the good stations sound:
   Dire Wolf can send steady calibration
   tones (its `-x` option) while you set
   the transmit level for the customary
   modest deviation. Your own decode of
   your own signal, at level ~50 with
   even brackets, is the target picture.

Check: on the lab's files, `atest`
reports 50(14/14) on every clean packet
and the summary decodes 6 of 6. When
your station's heard traffic looks like
that line — mid-scale, balanced, whole —
the audio question is answered and any
remaining problem lives somewhere more
interesting.
