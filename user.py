from llama_cpp import Llama
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "slm.gguf")

model = Llama(model_path=model_path, n_ctx=512, verbose=False)

user_input = input("Enter your question: ")

response = model.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "Generate a multiple choice question with 4 options (A, B, C, D). State the correct answer at the end as 'Answer: X'."
        },
        {"role": "user", "content": user_input},
    ],
    max_tokens=300,
    temperature=0.7,
)

quiz_text = response["choices"][0]["message"]["content"]
print(quiz_text)

user_input = input("Enter your answer (A, B, C, D): ").strip().upper()

match = re.search(r"Answer\s*:\s*([A-D])", quiz_text)

if match:
    correct_answer = match.group(1)
    if user_input == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
else:
    print("Correct answer could not be determined.")