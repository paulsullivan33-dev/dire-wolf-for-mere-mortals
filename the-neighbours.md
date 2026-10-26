# The Neighbours

Dire Wolf is one way to be a TNC. An
honest map of the others, and what each
sees that it doesn't:

## The hardware TNC

The box this software replaces
(Kantronics' KPC-3+ is the shape most
packet veterans picture; MFJ and
Timewave made their own). It is a small
computer with one job, and its virtues
are a box's virtues: it draws little
power, boots into duty instantly,
survives a decade in a hilltop hut, and
cannot be distracted by an operating
system's updates. In **KISS mode** it is
the same dumb pipe as chapter 7 (and
speaks the same protocol — KISS was
invented for it); in its own host mode
it adds mailboxes and nodes from its
era. Its limits are its era: the decoder
is whatever the firmware holds, fixed
forever, and against weak, twisted,
real-world signals the difference
between a 1990s modem chip and Dire
Wolf's several parallel demodulators is
the difference between a station that
hears the valley and one that hears the
strong half of it. A Pi running Dire
Wolf is the modern answer to the same
budget line — smarter, cheaper, and one
SD card's health away from silence
(chapter 15).

## SoundModem

Andrey Kopanchuk's (UZ7HO) **SoundModem**
is Dire Wolf's closest living relative:
a sound-card modem for Windows,
well-regarded decoders, and a host side
that speaks **AGW** — which is why so
many clients offer an "AGW" connection
and mean his program as readily as this
one. The choice between them is mostly
geography: SoundModem is a Windows
program with a settings window; Dire
Wolf is a configuration file that runs
anywhere Unix does, with the digipeater
and igate built in rather than bolted
on. Its cross-platform descendant,
**QtSoundModem**, carries the same
modems to Linux desktops.

## The TNC inside the radio

Several APRS radios — Kenwood's and
Yaesu's APRS lines are the standard
examples — carry the whole station in
the box: GPS, TNC, APRS menus, a small
screen with the map's worth reduced to
lists. As a *portable* station nothing
in this guide competes: no laptop, no
cables, no levels to set, because the
factory set them. The trade is openness:
the decoder is fixed, the logs are the
radio's, the doors to other programs
are whatever the maker exposed (some
models will lend their TNC to a computer
over USB or Bluetooth, in KISS — at
which point the radio has become the
expensive soundless cousin of chapter
7's modem). And a **tracker** like the
Byonics TinyTrak is the radio-side
minimalist: a small board that only
*originates* — GPS in, position packets
out, nothing decoded, nothing heard.

## A receiver that is only software

One more neighbour, worth naming because
the package itself ships an example
configuration shaped for it
(`sdr.conf`, in the distribution's
documentation): an **SDR** receiver —
an RTL-SDR dongle and tuning software —
feeding its audio into Dire Wolf, most
often as a receive-only igate. No
transmitter at all, a receiver that
never wears out its front end on a
keyer, and the cheapest seat from which
to watch a whole district's traffic
(chapter 11's duties still apply: what
the igate posts, it posts under a call
sign). The RTL-SDR guide in this series
covers the receiver side.

The pattern across all four: the modem
is a commodity now. What you are
choosing is where the intelligence
lives, what it costs to keep alive on a
hilltop, and whose decoder you trust
with the weak ones.
