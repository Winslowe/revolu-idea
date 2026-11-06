# Contributing

I try to reply to issues within a few days.

## Setup

Python 3.10 or newer.

```bash
git clone https://github.com/jayhemnani9910/revolu-idea.git
cd revolu-idea
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt pytest ruff
```

You don't need any API keys to work on the code. The mock LLM and mock search run the whole graph:

```bash
LLM_PROVIDER=mock SEARCH_PROVIDER=mock python main.py "test topic"
```

## Checks

CI runs these on every push and pull request. Run them before you open a PR:

```bash
ruff check .
python -m pytest -q
```

Tests go in `tests/` as `test_*.py`. Tests must not call real LLM or search APIs; use the adapters in `adapters/mock_adapters.py`.

## Style

- 4-space indents, type hints on public functions.
- `snake_case` for modules and functions, `PascalCase` for classes.
- Graph nodes are async: `async def __call__(self, state: ResearchState) -> dict`.
- Provider code goes in `adapters/`. `agents/` and `graph/` only import from `ports/`.

## Pull requests

- Branch off `master`, one change per PR.
- Say what changed and how you tested it.
- Keep `.env` and any keys out of commits.

## Bugs

Open an issue with the command you ran, what you expected, what happened (paste the output), your Python version and OS, and which `LLM_PROVIDER` and `SEARCH_PROVIDER` you used.
