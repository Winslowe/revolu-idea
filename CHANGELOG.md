# Changelog

All notable changes to this project are listed here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
There are no tagged releases yet.

## [Unreleased]

### Added
- CI workflow: ruff lint and an end-to-end test of the whole graph on the mock LLM and mock search.
- Demo GIF, CONTRIBUTING.md, issue and pull request templates, this changelog.

### Changed
- README rewritten around a no-key mock run.
- `.gitignore` covers every `.env*` file except `.env.example`.

### Fixed
- Ruff errors: unused imports, a bare `except`, `==` type comparisons in the mock adapter.

### Removed
- AI assistant config files (`AGENTS.md`, `.github/copilot-instructions.md`).

## 2026-10-08

### Fixed
- `TEMPERATURE` setting now reaches the LLM calls.
- JSON extraction from LLM output handles braces inside strings.
- Exa search no longer crashes when a result has no score.
- Judge keeps evidence on an edge when confidence is below the threshold.
- Writer matches finding verdicts on node labels, not raw ids.
- Planner strips node ids and falls back to a generated id.
- Auditor visit cap follows `MAX_RECURSION_DEPTH`.
- A failed partial report is reported instead of swallowed.
- `LLM_MODEL=auto` without a model pool, and a missing search key, now fail with a clear error instead of silently using mock search.
- Landing page demo checks fetch errors, Mermaid diagrams parse, Pages workflow is valid YAML and deploys `docs/`.

### Removed
- Unused Ollama adapter and its settings.
- Jekyll Pages workflow.

## 2025-12-19

### Added
- GitHub Models as an LLM provider, with an `auto` model pool.
- GitHub Pages deployment workflow and a Live Demo link.

## 2025-12-18

### Added
- GitHub Pages landing page with an in-browser sample run.

## 2025-12-16

### Added
- DuckDuckGo search with a Wikipedia fallback.
- OpenAI-compatible LLM adapter and a fallback adapter that moves through a model pool.

### Fixed
- Workflow stability and report output.

## 2025-12-12

### Added
- First version: causal planner, adversary and supporter agents, judge, auditor and writer on LangGraph, with Tavily and Exa search, an Ollama adapter and mock adapters.
