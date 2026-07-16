# studio-sandbox-conformance

Disposable sandbox repository for `ai-studio-os` Day-5 Gate-A1 Hermes/
`studio-toolplane` conformance runs.

This repo holds no production code. Its only purpose is to be a real git
remote that the Hermes wrapper can clone into a per-run workspace and exercise
`read_repo_area` / `write_code` / `run_tests` / `commit_checkpoint` against,
under a task packet's `file_boundaries`/`allowed_tools` constraints.

Expect this repo's history to be reset or the repo itself deleted and
recreated as conformance runs proceed - nothing here is meant to be kept
long-term.

See `ai-studio-os`'s `documentation/evidence/day5/` for the governing task
packets and role card.
