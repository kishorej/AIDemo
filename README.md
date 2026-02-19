# AIDemo

Demo for using OpenAI to analyze CI failure logs.

## GitHub Actions setup

1. Add an `OPENAI_API_KEY` repository secret.
2. Run the CI workflow. It will:
   - execute tests and save `failure.log`,
   - call `ai-devops-demo/ai_analyzer.py` to summarize root cause and fix.

The analyzer reads the API key from the `OPENAI_API_KEY` environment variable.
