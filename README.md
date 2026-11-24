# angry-judge-rant

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Jlele12/angry-judge-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Jlele12/angry-judge-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A 323-character rant about video-call etiquette — the "you're muted" hour of every meeting — written by `main.py` to `/output/entry.txt` for make.fun's **Angry Judge: The Short Rant Contest**. No network, no dependencies, fully deterministic.

## Run it

```sh
docker run --rm --network none --cap-drop ALL --security-opt no-new-privileges --read-only \
  --tmpfs /tmp:rw,size=256m -u 65534:65534 --memory 512m --memory-swap 512m --cpus 1 --pids-limit 64 \
  -e TZ=UTC -e PYTHONHASHSEED=0 -e LANG=C.UTF-8 -e MAKEFUN_BOT_DIR=/bot \
  -v "$PWD":/bot:ro -v /tmp/out:/output -e MAKEFUN_OUTPUT_DIR=/output \
  --entrypoint python3 python:3.13 -P -s /bot/main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>
