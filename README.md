# The Robot Apology

A make.fun free bounty entry (u-suga-the-robot-apology-dd96bb59, $2 prize).

## What it is

A tiny Python program that writes a two-line robot confession to
`/output/entry.txt`:

1. One sentence in which a household robot apologizes for one specific
   mistake — setting an alarm for 6 p.m. instead of 6 a.m., so its owner
   missed the train to her sister's wedding rehearsal.
2. One sentence naming what it learned and what it will do differently:
   it now says the hour back with a.m. or p.m. attached before
   confirming it, and asks its owner to repeat any morning time twice
   before it sets it.

The mistake is small, exact, and human-scale; the lesson follows from
that exact slip instead of promising vaguely to do better; and the voice
is a machine noticing its own error, rueful rather than cute.

## Run it

```sh
python3 main.py
```

It creates `/output` when missing and writes `/output/entry.txt`
(UTF-8, two lines, well under the 400-character gate).

## Check it

```sh
python3 main.py
cat /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t),'chars,',len(t.splitlines()),'lines')"
```

## License

MIT — see LICENSE.
