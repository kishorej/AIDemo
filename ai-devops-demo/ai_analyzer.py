import openai

client = openai.OpenAI(api_key="YOUR_API_KEY")

with open("../../failure.log", "r") as f:
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
