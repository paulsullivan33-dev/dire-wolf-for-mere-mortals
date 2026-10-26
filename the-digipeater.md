# The Digipeater

Radio is line-of-sight, and valleys are
everywhere. Packet radio's answer is the
**digipeater**: a station that hears a
packet addressed for relay, and
retransmits it, once, so stations beyond
the hill can hear it too. A **digi** on a
good hilltop is the difference between a
neighbourhood and a region. This chapter
explains the request written into every
packet's path, the rules a polite digi
lives by, and Dire Wolf's one-line way of
joining in — with the honest note, up
front, that the lab configured a
digipeater and never ran one: it had no
radio, and its call sign was a
placeholder Dire Wolf itself refused to
arm (chapter 5). What follows is the
documented behaviour, with the lab's
parser run as the evidence that the
configuration is real.

## The path is a request

Chapter 2 left the path as "relays
requested". APRS's convention, the
**WIDEn-N paradigm**, works like this.
A sender who wants wide-area relaying
writes `WIDE2-2` in the path: the first
2 says *wide digipeaters, take this two
hops*, and the second counts down as it
is spent — a packet heard as `WIDE2-1`
has one wide hop left, `WIDE2-0` is
done. `WIDE1-1` is the smaller ask: one
hop, aimed at a **fill-in digi** — a
modest station, often someone's home —
whose whole job is to lift a weak local
signal up to the hilltop digi that can
really carry it. A packet that has been
served shows the spent hop with a star
in monitor listings: `WIDE1-1*` means
*this one has been repeated already*.

The etiquette is arithmetic. Each hop
retransmits the packet over the whole
area the digi covers, and every station
in the chain starts over. `WIDE2-2` from
a hilltop station is a shout across two
counties; the same path from a handheld
in a valley is how it reaches anyone at
all. Choosing a path is choosing how
much of a shared, single channel to
spend — there is exactly one frequency,
everyone hears everyone, and a beacon
every ten minutes at three hops is not
a beacon, it is a occupation.

## The rules a polite digi lives by

A digipeater is simple to describe and
easy to get wrong for the whole map:

- **Repeat only what asks.** A packet
  whose next path element names your
  alias (or the WIDE pattern you serve)
  is a request; anything else is traffic
  you merely heard.
- **Never twice.** Dire Wolf, like every
  sane digi, remembers what it has
  repeated — identical packets inside a
  short window (the documentation speaks
  of about 30 seconds) are duplicates,
  not new requests. Without this, two
  digis in earshot would bounce a packet
  between them until its path ran out,
  and say nothing else all evening.
- **Mark your work.** A spent hop is
  recorded in the path (the star), and a
  digi may also insert its own call sign
  into the path — **tracing** — so the
  map can see the route a packet took.
- **Listen before talking.** The channel
  is shared; the modem waits for a gap.
  A digi on a busy hilltop spends much
  of its life politely not transmitting.

## Dire Wolf's one line

Chapter 5's file carries the rule:

```text
DIGIPEAT 0 0 ^WIDE[3-7]-[1-7]$ ^WIDE[12]-[1]$
```

Read it as: *on channel 0, in and out,
repeat packets whose path matches these
patterns* — the patterns being the
project documentation's recommended
fill-in behaviour, matching the WIDE
requests of the paradigm. Several
`DIGIPEAT` lines may stack for several
patterns and channels, and the manual's
digipeater chapter is the full grammar.
The lab's evidence for this line is
chapter 5's run: the parser accepted it,
then cross-checked it against the
station's identity —

```text
Config file: MYCALL must be set for receive channel 0 before digipeating is allowed.
Config file: MYCALL must be set for transmit channel 0 before digipeating is allowed.
```

— and, the call sign being the
placeholder, left the digi disarmed. To
arm one for real, the work is not in
this line: it is a real call sign in
`MYCALL`, a radio wired and level-set
(chapters 5 and 6), a site where
repeating helps more than it congests,
and usually a word with the local
packet community, whose existing digis
your new one will spend its life
conversing with. Check for this chapter
is exactly that refusal: your
configuration is digipeater-shaped when
Dire Wolf stops telling you why it will
not digipeat — and not one sentence
before.
