"""End-to-end run of the whole graph on the mock LLM and mock search. No keys, no network."""
import asyncio
from pathlib import Path

from config.settings import Settings
from container import Container
from main import run_research


def test_mock_run_writes_report(tmp_path):
    settings = Settings(llm_provider="mock", search_provider="mock", output_dir=str(tmp_path))
    container = Container(settings)

    final_state = asyncio.run(run_research("Why do startups fail?", container))
    report = final_state["final_report"]

    assert report.topic == "Why do startups fail?"
    assert report.verification_status == "VERIFIED"
    assert report.total_findings == 6

    path = Path(asyncio.run(container.storage.save_report(report)))
    assert path.exists()
    assert path.with_suffix(".md").exists()
