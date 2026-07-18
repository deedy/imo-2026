# Kimi K3 — IMO 2026 runs (6/6 solved)

Runs of Moonshot AI's `kimi-k3` (via the OpenAI-compatible API) on the six IMO 2026
problems, archived in the same per-problem layout as the sibling model directories.

**Provenance / caveats — these runs did NOT use the AutoFyn stack.** They were driven
by a lightweight single-context tool loop (bash / write_file / read_file, workspace-
scoped, network access blocked) built with Claude Code; there is no orchestrator, no
subagents, and no round-based context resets (problem 3 got one manual second round
seeded from its round-1 disk state). Every model turn and tool call is recorded
verbatim in each problem's `logs.jsonl` (`harness` field in the run record). Runs were
capped at 60 turns / 110 minutes per problem, with a soft "finalize now" warning at
75 minutes.

Problem statements were taken verbatim from `tempcollab/proval` `problems.jsonl`
(`imo-2026-01` … `imo-2026-06`, branch `parallel-approach-v2`).

## Results

| Problem | Status | Notes |
|---|---|---|
| 1 | solved (~20 min) | answer matches sibling runs; independent termination argument |
| 2 | solved (~85 min) | trig/power-of-a-point computational proof |
| 3 | solved (4 rounds; ~5.5 h total) | c = 2^n/(2^{n+1}−1), matching the sibling runs. Rounds 1–3 lost their in-context proof work to time caps / a balance outage; round 4 ran under a "proof-writing only, checkpoint every section" directive, recovered state from the prior rounds' logs, fixed a gap in its own Part A sketch, and completed both bounds |
| 4 | solved (~50 min) | characterization θ = 180°/n matches sibling runs, same n−1 bound |
| 5 | solved (~50 min) | f(x) = x + c, c ≥ 0; matches sibling runs |
| 6 | solved (~1.6 h retry after a stream-timeout round; hardened harness with checkpoint nudges) | enumeration/reduction to finitely many minimal elements of S_∞, stabilization lemma proved |

Solutions have NOT been independently verified by human reviewers (unlike the
medalist-reviewed sibling results for problems 1–3); "solved" reflects the model's own
completed, self-checked write-up in `current.md`.
