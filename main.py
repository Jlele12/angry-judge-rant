import os

RANT = (
    "Meeting's at 2. At 2:04 the tiny voice: \"you're muted.\" I unmute, "
    "it's my turn to say \"sorry, you go.\" We both go. Nobody goes. Then "
    "\"can everyone see my screen?\" I cannot. You're sharing the folder "
    "that holds the slide, not the slide. Forty minutes. Six slides. Read "
    "aloud. Verbatim. Email was fine. Email was always fine."
)
assert len(RANT) <= 400

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(RANT)
