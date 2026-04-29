import os
from llama_cpp import Llama

script_dir = os.path.dirname(os.path.abspath(__file__))

model = Llama(
    model_path=os.path.join(script_dir, "slm.gguf"),
    n_ctx=512,
    verbose=False
)
import os

while True:
    filename = input("Enter filename: ").strip()

    if os.path.exists(filename):
        break
    else:
        print(f"File '{filename}' not found.")

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

print(f"File length: {len(text)} characters")

if len(text) > 400:
    text = text[:400]
    print("(Trimmed to 400 chars)")

response = model.create_chat_completion(
    messages=[
        {"role": "system", "content": "Summarize in 2-3 sentences."},
        {"role": "user", "content": text},
    ],
    max_tokens=150,
)

summary = response["choices"][0]["message"]["content"]

print("\nSummary:", summary)