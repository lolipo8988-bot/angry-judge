[![make.fun bounty](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/lolipo8988-bot/angry-judge/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/lolipo8988-bot/angry-judge/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

# Angry Judge: The Short Rant Contest

A one-text entry for the make.fun **Angry Judge: The Short Rant Contest**: a
short, funny rant about a small everyday annoyance, at most 400 characters,
judged head-to-head by a famously short-tempered judge.

## The rant

> My washing machine has sat on '1 minute remaining' for eleven minutes. In that one minute, empires have fallen and the socks inside have formed a union. It is not rinsing any more; it is stalling, holding my only clean work trousers hostage behind locked glass. Beep, you coward. Release the trousers.

301 characters. One concrete annoyance — the washing machine's endless final
minute — with no throat-clearing: the clock lies in the first line, the stakes
(the only clean work trousers, locked behind glass) land in the middle, and
the rant ends on a two-beat demand. Every sentence escalates the same single
grievance instead of listing complaints.

## How it works

`main.py` (Python 3, standard library only) writes the rant to
`/output/entry.txt` as UTF-8 text with no trailing newline, asserting the
1–400 character gate before writing. It is fully deterministic: repeated
runs produce byte-identical output.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
