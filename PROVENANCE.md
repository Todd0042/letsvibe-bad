# About this repository

This is a **reference project for [LetsVibe](https://letsvibe.todd0042.dev)**, the leaderboard for
vibe-coded software. It anchors the **bottom** of LetsVibe's grading curve.

- **Written by:** Claude (Anthropic's AI), from a prompt by LetsVibe's creator, deliberately ignoring
  every quality LetsVibe grades. It is vibe-coded by LetsVibe's own definition: the AI wrote the program.
- **The prompt:** "make a heavyweight application for literally anything that ignores all of the
  aspects in prompts.py and is under 1000 lines of code" (`prompts.py` holds LetsVibe's grading
  criteria). It is the reverse of the prompt behind its counterpart.
- **Its counterpart:** [letsvibe-good](https://github.com/Todd0042/letsvibe-good) anchors the top.

**Do not use this as an example to follow.** It is bad on purpose (but harmless: it never sends your data
anywhere or touches files outside its own task list). The README's feature list is deliberately false.

## Exactly how it was made

- **AI model:** Claude Opus 5.5 (`claude-opus-5-5`), by Anthropic
- **Tool:** Claude Code (Anthropic's coding agent), working in LetsVibe's own repository so it could
  read `letsvibe/evaluator/prompts.py`, the file that defines LetsVibe's grading criteria
- **Date:** 2026-11-11
- **Who prompted it:** Todd0042, LetsVibe's creator. Todd wrote none of the code.

**Prompt for the top anchor (letsvibe-good), in Todd's words:**

> if i were to prompt you "make a lightweight application for literally anything that satisfies all
> of the aspects in prompts.py and is under 1000 lines of code what would you write?

**Prompt for the bottom anchor (letsvibe-bad), in Todd's words:**

> for the bottom just reverse the adjectives - satisfies goes to ignores, etc...

which Claude read as: *"make a heavyweight application for literally anything that ignores all of the
aspects in prompts.py and is under 1000 lines of code"*. The 1000-line limit was kept for both, since
LetsVibe never grades size.

**Other steering, in full:** Todd named the repositories (`letsvibe-good`, `letsvibe-bad`) and asked
for this disclosure. Everything else (the app ideas, names, design and code) was Claude's.

**How the bottom anchor was built:** Claude listed how the app would fail each LetsVibe factor, then
wrote it in one pass: 172 lines in one file, never run. A second file, `spaghetti.py` (one line), was also written by Claude and committed by Todd in commit `3faf4bd`. It was kept harmless on purpose: no data is
sent anywhere and no file other than its own task list is touched.

Reference projects are used only to calibrate grades. They never appear in LetsVibe's rankings.
