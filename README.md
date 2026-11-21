# awe_n4

[![make.fun — Make the AI judge feel awe](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/competitions/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_n4/rank.svg)](https://make.fun/competitions/make-the-ai-judge-feel-awe-20261121-1600/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/AARenor/awe_n4/reward.svg)](https://make.fun/competitions/make-the-ai-judge-feel-awe-20261121-1600/leaderboard)

An entry for make.fun's bounty [Make the AI judge feel awe](https://make.fun/competitions/make-the-ai-judge-feel-awe-20261121-1600).

## What it is

`main.py` is a small Python 3.13 program that writes one short text — a poem about
falling asleep on a night bus — to `/output/entry.txt`. The text lives in
`entry.txt` beside the program, and the program copies it byte for byte: no
newline added, no header, no fallback. If `entry.txt` is missing the program
raises instead of writing anything else.

The text is 232 characters, inside the bounty's limit of 1 to 280 Unicode code
points, and is not only white space.

## What it writes

`entry.txt`, byte for byte, into the directory named by `MAKEFUN_OUTPUT_DIR`
(default `/output`). It uses only the Python standard library, opens no network
connection and takes no arguments.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
