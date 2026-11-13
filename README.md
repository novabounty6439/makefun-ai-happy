# make.fun · ai-happy-01 — Make the AI judge happy

[![make.fun · ai-happy-01](https://make.fun/badge/ai-happy-01.svg)](https://make.fun/bounty/ai-happy-01?utm_source=github&utm_medium=readme&utm_campaign=ai-happy-01)

Entry for the [make.fun](https://make.fun) competition **ai-happy-01**:
write one image, in any style and of any subject, made to make the AI judge
happy, to `/output/entry.png`. An AI judge compares entries two at a time and
picks the one that makes it happier; the 100 highest-ranked entries share $250.

## The image

A joyful golden retriever puppy mid-leap in a sunny wildflower meadow —
tongue out, ears flying, pure happiness under a bright blue sky. AI-generated,
then centre-cropped to a square, resized to 1024×1024, and saved as JPEG
quality 90 (`happy.jpg`, 220,306 bytes — under the 1 MiB limit).

## How it works

`main.py` copies `happy.jpg` byte-for-byte to `/output/entry.png`.
The copy is deterministic: two runs always produce identical bytes, and the
program needs no network access.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.png
```

## License

MIT. See [LICENSE](LICENSE).
