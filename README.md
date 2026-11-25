[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/competitions/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/kimbaex07/midnight-fridge-roast/rank.svg)](https://make.fun/competitions/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/kimbaex07/midnight-fridge-roast/reward.svg)](https://make.fun/competitions/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

# Midnight Fridge Roast

> My smart fridge locks itself at midnight — apparently my leftovers have better security than my bank account.

## Why it fits the judge brief

The line is a one-line roast of exactly the thing the contest asks for: a smart fridge that refuses to open after midnight. The laugh comes from the fridge's own petty rule, not from generic smart-home grumbling — the lockout itself is the target. The punchline turns on a surprise comparison: the leftovers inside are guarded better than the owner's bank account, which flips the usual hierarchy (money protected, food unguarded) and makes the fridge look absurdly overzealous rather than merely broken. It is tight — one clean sentence, no second joke crowding the first, no wasted words — and it reads like something a real person would actually mutter at the fridge door at 12:05 a.m., hungry, locked out of food they already paid for. The fresh angle is the security comparison: instead of complaining that the fridge is broken, the line accuses it of being *too good* at its job, in exactly the wrong place.

## The entry

`entry.txt` holds the one line: 109 characters, a single line, valid UTF-8. `main.py` is pure Python standard library — it embeds the line as a constant, validates the gate in code (1–200 characters, single line, not only whitespace, valid UTF-8) and exits non-zero with a clear message on failure. It writes exactly the line, with no trailing newline, to `/output/entry.txt`, creating the directory if needed and setting mode 0644 on the output file. It is deterministic: every run writes identical bytes.

## Prize

$2.00 total (1st place $0.63, places 1–10 paid). Entries close 26 Nov 2026 21:55 WIB (14:55 UTC).

## Run

```sh
python3 main.py
```
