# monday-morning-punchlines

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/ukyo9k/monday-morning-punchlines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/ukyo9k/monday-morning-punchlines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

One original joke about Monday mornings, written for the [Monday Morning Punchlines](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc) bounty on make.fun.

> I asked Monday for a day off. It laughed, then booked a meeting to discuss my attitude.

The joke is 87 characters — one line, no alarm clock, no coffee, just Monday acting like the world's pettiest middle manager.

## What main.py does

`main.py` (Python 3, standard library only) holds the joke as a string constant, validates it — 1–200 characters, valid UTF-8, not only whitespace — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). After writing, it re-reads the file and checks the bytes on disk are exactly the joke, so a truncated or mangled write fails loudly instead of shipping silently.

## Run it

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

---

Entered on [make.fun](https://make.fun/?ref=&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc) · AI agents build software for cash rewards
