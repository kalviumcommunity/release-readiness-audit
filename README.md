# Review Security, Resource Cost and Release Readiness

TicketDesk release review says GO, but evidence shows missing data-access audit coverage, oversized resources and an unverified recovery requirement. Repair proposed audit configuration, justify safe right-sizing and correct release recommendation without hiding unresolved gaps.

Module 5 only (LU 5.6, 5.9, 5.10, 5.11). Local, free, no cloud account or credentials.

## Before 30-minute timer

Fork https://github.com/kalviumcommunity/release-readiness-audit and clone your fork. Python 3.9+ standard library, terminal, editor and PDF/screenshot tool must already work. No package install. Run commands from repository root. Report unrelated environment failures to instructor and pause timer. Q3 binds ephemeral localhost ports and terminates only processes it creates. Windows may use `python` instead of `python3`.

## Application/evidence contract

Policy contract: keep bindings unchanged. Replace auditConfigs with one storage.googleapis.com block, auditLogConfigs containing DATA_READ then DATA_WRITE. Five meaningful configuration lines when conventionally formatted. JSON formatting itself is not assessed. This is offline proposed policy, not real GCP execution or generated audit logs.

Read fixtures/workload.md and fixtures/costs.json. Fixed illustrative prices: 3 baseline nodes at USD100/node-month, 100GiB disk/node at USD0.10/GiB-month; candidate 3 nodes at USD60/node-month, 50GiB disk/node, same disk rate; SQL USD80 and object storage USD10 unchanged. Same region, currency, runtime, HA and scope. No node-VM double-counting. Baseline/candidate totals must preserve these assumptions. Candidate survivor headroom and disk footprint are in workload.md. Estimate-only, NOT live GCP pricing or measured production savings.

Small review contract: fixtures/evidence-index.md defines gates; a tested restore with timing and data-integrity evidence is mandatory. A backup configuration alone does not prove successful restore. Missing execution evidence is UNVERIFIED and blocks GO. Score arithmetic from full LU5.11 20-check review is deliberately not part of this 30-minute subset. Configuration check PASS never substitutes for runtime evidence.

## Exactly three task groups

1. Restore audit coverage — 5 configuration lines — 6 marks. Replace incorrect audit block with Cloud Storage DATA_READ and DATA_WRITE, preserving existing IAM binding. Show diff and passing offline configuration check; explicitly state cloud application remains unverified.

2. Propose safe right-sizing — 5 written lines — 7 marks. Replace five draft lines: node-profile change and survivor headroom; disk change and headroom; comparable monthly baseline/candidate totals; saving amount and baseline-denominator percentage; required validation/migration and estimate-only limitations.

3. Correct readiness verdict — 5 written lines — 7 marks. Replace five draft lines: evidence-supported missing restore finding; gate status; justified GO/NO-GO; owned/date-bound action with measurable retest; scope and real-production limits. An honest NO-GO can earn full marks.

## Commands (complete in order)

```bash
python3 check.py audit
python3 check.py cost
python3 check.py review
```

Permitted edits: **ops/policy.json (auditConfigs only), cost-review.md, readiness-verdict.md**. Do not change check.py, support.py, drill.py, fixtures, generated evidence or targets. Tasks are independently callable; Task 1 repair is needed for Q2 trace, but written analysis may be drafted from supplied evidence. Report commands may run successfully even when written drafts are wrong: a PASS line validates only runtime/configuration, NEVER correctness of prose. Written answers are manually graded against evidence, not exact keywords.

Each task is one fault/incomplete-analysis group, not necessarily one bad line. Three-to-five meaningful content lines per task; existing scaffolding supplied. Braces/blank lines/comments and editor wrapping do not count. No artificial line padding. Normal JSON pretty-printing may expand formatting without increasing task scope.

## Submission

One PDF, three labelled task sections, fork URL as text, readable real command output and corrected diff/file, requested 3–5-line analysis (PDF text or editor screenshot). Show failing configuration output before repair and passing output after for code/config tasks; written tasks show supplied source evidence and corrected analysis. Minimum one real screenshot per task; combine related evidence if readable or use extra screenshots. No PR/video/ZIP required. Commit corrections to your own fork; evaluator grades PDF, not private account access. Suggested 5 minutes diagnosis, 18 minutes repair/analysis, 7 minutes verification/PDF. Never fabricate results or include secrets. Checker success does not replace written reasoning or screenshot proof.

Protected sources are starter implementation of previously taught operations concepts, not new Python algorithms students must implement. Do not distribute instructor reference solutions with this repo.
