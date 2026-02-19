import os
from pathlib import Path

from openai import OpenAI


def read_failure_log() -> str:
    repo_root = Path(__file__).resolve().parents[1]
    failure_log_path = repo_root / "failure.log"
    return failure_log_path.read_text(encoding="utf-8")


def build_prompt(logs: str) -> str:
    return f"""
You are a DevOps assistant.
Analyze the following CI pipeline failure log.

Return:
1. Root Cause (1-2 lines)
2. Suggested Fix (1-2 lines)

Log:
{logs}
"""


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Configure it as an environment variable or GitHub Actions secret."
        )

    client = OpenAI(api_key=api_key)
    logs = read_failure_log()
    prompt = build_prompt(logs)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
