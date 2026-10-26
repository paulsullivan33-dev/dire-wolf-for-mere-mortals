# Dire Wolf for Mere Mortals

A packet station used to need a box of
electronics between the computer and the
radio: a **TNC**, a terminal node
controller, which turned text into tones
and tones back into text. **Dire Wolf**
is that box, rewritten as software. It
listens to a radio through a sound
device, decodes the beeps of **packet
radio** into **AX.25** frames, and makes
frames back into beeps for transmitting.
On top of that it understands **APRS** —
the Automatic Packet Reporting System —
and can repeat other stations' packets
as a **digipeater**, or carry them
between radio and internet as an
**igate**.

This guide explains the moving parts in
plain language: how a packet is built,
how APRS packs a position, a message or
a weather reading into one short line,
how Dire Wolf is configured, and how its
two doors — **KISS** and **AGW** — let
other programs use it as their modem.
Two duties are stated as plainly as the
technique, because they are part of the
technique: you transmit only under your
own call sign and licence, and an igate
operator answers for everything their
station forwards to the internet.

The lab behind this guide kept its feet
off the air entirely. It installed **Dire
Wolf 1.7** from its operating system's
packages on a small Linux machine with
no radio and no sound card, and worked
with audio files and a silent software
sound device instead. With the project's
own **`gen_packets`** tool it turned six
written **APRS** packets — an invented
hilltop site, an invented rover, an
object, a message, a status line and a
telemetry report, all under the
placeholder call **N0CALL** — into 4.7
seconds of 1200-baud audio, then decoded
that audio back with **`atest`**: six
packets in, six packets out. It added
noise to twelve more packets until the
decoder honestly gave up on three of
them. It ran the real program against
the lab's configuration file and
recorded the checks Dire Wolf makes
before it ever touches a sound device —
including its refusal to beacon or
digipeat for a station whose call sign
is still the placeholder. It started the
program against a silent software audio
device so both network doors opened,
knocked on the **KISS** door with a real
frame from a small script, and watched
Dire Wolf take the frame in and queue it
to transmit.

What the lab could not do, it did not
fake. No radio was connected, nothing
was transmitted, digipeating and
igating were configured and explained
but never operated, and the application
programs of chapter 13 are described
from their documentation. Wherever a
chapter leans on reading rather than
running, it says so, and `criteria.md`
keeps the full ledger.

## What this guide covers

- [**What Dire Wolf is**](what-dire-wolf-is.md) —
  the software TNC, what it replaces,
  and the licence rule that is part of
  the tool, not an afterthought
- [**Packet radio and AX.25**](packet-radio-and-ax25.md) —
  frames, addresses, checksums, tones:
  how text survives a trip through a
  radio channel
- [**APRS in plain terms**](aprs-in-plain-terms.md) —
  positions, objects, messages, status
  and telemetry, taken apart line by
  line from real decoded output
- [**Installing Dire Wolf**](installing-dire-wolf.md) —
  packages and source builds, and the
  companion tools the install brings
  with it
- [**The configuration file**](the-configuration-file.md) —
  the lab's own configuration, section
  by section, with the parser's
  complaints read aloud
- [**Audio levels, honestly**](audio-levels.md) —
  the setting that makes or breaks a
  packet station, and how Dire Wolf
  reports it on every decode
- [**KISS and AGW — the two doors**](kiss-and-agw.md) —
  how other programs hand frames to the
  modem, both doors opened and knocked
  on in the lab
- [**Your first decode**](your-first-decode.md) —
  decoding a recording with `atest`,
  and reading what it tells you
- [**Making a packet and hearing it back**](making-a-packet.md) —
  writing packets as text, turning them
  into audio with `gen_packets`, and
  closing the loop
- [**The digipeater**](the-digipeater.md) —
  repeating other stations' packets:
  WIDE paths, fill-in digis, and the
  rules that keep a shared channel sane
- [**The igate and its responsibilities**](the-igate.md) —
  carrying traffic between radio and
  the APRS internet system, and what the
  operator answers for
- [**Beacons and telemetry**](beacons-and-telemetry.md) —
  announcing your station, objects that
  speak for places, and numbers from
  sensors
- [**Connecting applications**](connecting-applications.md) —
  map clients and other programs that
  sit on top of the modem, in outline
- [**The neighbours**](the-neighbours.md) —
  hardware TNCs, SoundModem, and the
  TNCs built into radios: what each
  does that Dire Wolf doesn't, and
  vice versa
- [**Limits**](limits.md) — a decoder is
  not a radio, software cannot fix a
  bad cable, and the legal edge of
  running infrastructure for strangers
- [**Troubleshooting**](troubleshooting.md) —
  silence from a healthy program, the
  port that was already taken, the
  call-sign placeholder that disables
  half the station, and other traps
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Transmitting without a licence, or
under any call sign but your own — that
is not a harder chapter of this book,
and chapter 1 explains why the software
itself refuses to help. Wiring diagrams
for specific radios are pointed at, not
drawn: the radio manuals and the
project's own documentation carry them,
and a wrong pinout is worse than none.
Running a high-site digipeater or a
two-way igate for a whole region —
siting, coordination, duty of care — is
described in its duties but taught only
at the scale of one careful station.

## How to use this guide

Read chapters 1 to 3 for the model
before installing anything: a packet is
much easier to debug once you know what
one is. Chapters 8 and 9 are the lab
chapters — run them with nothing but
files, in the same sitting as the
install, before a radio is ever
connected. Chapter 6 deserves its
reputation: most "packet doesn't work"
is audio level, and Dire Wolf tells you
the number on every decode if you let
it. Chapters 10 and 11 are the
responsibility chapters: read them
before your station repeats or forwards
a single packet for anyone else. The
lab's files live in `dire-wolf-lab/` —
its configuration, its packet texts,
the audio it generated, and every
transcript — and its notes are
`examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Ham Radio for Mere Mortals](https://paulsullivan33-dev.github.io/ham-radio-for-mere-mortals/)
- [Meshtastic for Mere Mortals](https://paulsullivan33-dev.github.io/meshtastic-for-mere-mortals/)
- [RTL-SDR for Mere Mortals](https://paulsullivan33-dev.github.io/rtl-sdr-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/dire-wolf-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/dire-wolf-for-mere-mortals/blob/main/LICENSE-CODE).
