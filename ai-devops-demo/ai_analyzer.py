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
