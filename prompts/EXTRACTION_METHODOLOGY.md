# Case Extraction Methodology

This document records the extraction method for processing `thread_XXXX.readable.md` files into `outputs/cases/thread_XXXX_case_NN.json` and `outputs/analysis/thread_XXXX_analysis.json`. It exists so the method isn't lost or drifted from across sessions.

## Standing rules (apply to every thread, no exceptions)

1. **All output content must be in English**, regardless of the source language (most threads are Japanese). No Japanese characters in any field, including terms quoted parenthetically — translate everything.
2. **One case file per distinct customer question or technical issue.** Do not collapse multiple distinct questions into a single case. Tightly-related sub-questions raised together in the same single inquiry may be bundled into one case using judgment.
3. **No cap on case count.** The number of cases should reflect how many distinct issues actually exist in the thread, not be capped at some "proportional to length" estimate. A 30,000-line thread is not entitled to only 4-6 cases if it actually contains 20.

## File structure insight (why the old method had gaps)

These `.readable.md` files are email-chain exports. Each numbered message block (`## N. <date>`) contains:
- New reply text at the top (the actual new content of that message)
- Followed by a `From:`/`差出人:` line introducing a **quoted copy of every prior message in the thread**, nested in reverse-chronological order

This means message `## N`'s body is a near-superset of messages `## 1` through `## N-1`. The last message in a thread typically contains almost the entire conversation history as nested quotes.

**Old method (grep-then-sample):** Search the whole file for Japanese question-marker patterns (`でしょうか`, `ご教示`, `可能でしょうか`, etc.), then read context only around each match's *first* (lowest line-number) occurrence, since that's where the content is genuinely new.

**Problem:** This only finds questions phrased in ways that match the search patterns. A technical issue stated as a flat declarative sentence, an instruction, a decision, or phrased without one of those specific markers is invisible to grep and gets silently skipped. This is the actual root cause of incomplete extraction on large threads, not insufficient "reading."

**Also rejected: "read every line top to bottom."** Because of the nesting structure, this means re-reading the same quoted history once per message that quotes it — for a 22-message thread, early content gets read up to 20+ times. Slow, and doesn't fix the real gap (grep pattern blindness), since you'd still need to decide what counts as a "distinct issue" while skimming redundant text.

## New method (new-content-only sequential read)

1. **Map message boundaries first.** Run `grep -n "^## [0-9]+\."` to get every message's starting line number.
2. **Read only the new (unquoted) slice of every message, in order, from message 1 to the last.** For each message, read from its `## N.` marker down to where the quoted `From:`/`差出人:` chain begins (usually within the first 100-200 lines, but check — don't assume a fixed window). This captures every message's unique contribution exactly once, with no redundant re-reading and no dependence on keyword luck.
3. **Keep a running scratch list of every distinct issue found, as you go** — do not rely on holding it all in working memory until the end of a long thread. Write the case file for each issue as soon as it's confirmed distinct, rather than batching write-up to the end (this avoids losing track of issue #15 of 20 by the time you reach the end of a 30k-line thread).
4. **Audit pass with grep at the end, not as primary discovery.** After all new-content slices are read and cases are written, run a keyword sweep (question markers, decision markers, "ご確認", "ご教示", etc.) across the whole file. Every hit should trace back to a case already written or a documented reason it's not case-worthy (pure logistics/scheduling). A hit that traces to nothing is a real gap — go read that section's new-content slice and fix it.
5. **Spot-check the final message's full nested quote chain** against what was read in step 2, specifically watching for: messages where part of the quote chain was deleted/truncated, off-thread replies that branch (CC'd parties replying separately), and messages whose content is attachment-only (no inline text) — these are the actual blind spots, not sequential coverage.

## Residual limitations (honest ceiling, even with the new method)

- **Attachments and images are not searchable text.** If a distinct issue is documented only in an attached spec sheet, log file, or screenshot referenced inline, it will be missed unless its existence is at least flagged in the surrounding email text.
- **Judgment calls on "distinctness"** remain subjective at the margins — two closely related questions raised in the same inquiry vs. two truly separate cases is a human (or model) call, not a mechanical one.
- **Long-session write-up fatigue** is mitigated by the scratch-list habit in step 3, but isn't eliminated entirely.

Given these, this method should realistically achieve ~95%+ coverage of textual content, not a guaranteed 100%.

## Threads already processed under the OLD (grep-sample) method — candidates for redo

thread_0061 ~ thread_0107

## Redo policy: what happens to already-extracted cases

Redoing a thread under the new method is **additive, not destructive**:

- Existing case files that are accurate stay exactly as they are — they were read carefully under the old method, just possibly not exhaustively.
- Issues found by the new pass that weren't previously covered get **new case files, continuing the existing numbering** (e.g., thread_0004 case_01-06 already exist → a newly found issue becomes case_07).
- If re-reading reveals an existing case improperly bundled two distinct questions, or contains an outright error, fix that specific file directly — don't renumber or rewrite unrelated files.
- After the redo pass, update the thread's `analysis.json` (e.g., refresh `all_questions_found`) to reflect the fuller picture — but this is an update, not a wholesale replacement, unless the original summary was actually wrong.

Nothing gets deleted or discarded by default.
