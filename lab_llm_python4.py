import os
from llama_cpp import Llama

script_dir = os.path.dirname(os.path.abspath(__file__))

model = Llama(
    model_path=os.path.join(script_dir, "slm.gguf"),
    n_ctx=512,
    verbose=False
)
topic = input("Enter a topic: ")

response = model.create_chat_completion(
    messages=[{"role": "user", "content": topic}],
    max_tokens=200,
)

answer = response["choices"][0]["message"]["content"]
print("AI:", answer)

words = answer.split()
total_count = len(words)

long_count = 0
for word in words:
    if len(word) > 5:
        long_count += 1

percentage = (long_count / total_count) * 100 if total_count > 0 else 0

print(f"\nTotal words: {total_count}")
print(f"Long words (>5): {long_count}")
print(f"Percentage: {percentage:.1f}%")