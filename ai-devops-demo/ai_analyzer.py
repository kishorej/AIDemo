import openai

client = openai.OpenAI(api_key="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")

with open("AIDemo/AIDemo/failure.log", "r") as f:
    logs = f.read()

prompt = f"""
You are a DevOps assistant.
Analyze the following CI pipeline failure log.

Return:
1. Root Cause (1-2 lines)
2. Suggested Fix (1-2 lines)

Log:
{logs}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
