# Worst Fix Ever: Funniest Commit Message

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![make.fun rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![make.fun reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [make.fun bounty "Worst Fix Ever: Funniest Commit Message"](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) — a single commit message, at most 100 characters, for a bug fix that made everything worse.

## The entry

> fix: speed up login by skipping the password check - now instant for everyone, including hackers

96 characters. Login was too slow, so the password check was skipped. The fix worked perfectly: login is now instant for everyone — including hackers. The repair broke far more than it mended, which is exactly the point.

## How it works

`main.py` writes the commit message to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with a length guard asserting the entry is 1–100 characters.

```bash
python3 main.py
cat /output/entry.txt
```

## Referral

Join make.fun with referral code `hdavhdvz`.
