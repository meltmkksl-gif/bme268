import os
from llama_cpp import Llama

script_dir = os.path.dirname(os.path.abspath(__file__))

model = Llama(
    model_path=os.path.join(script_dir, "slm.gguf"),
    n_ctx=512,
    verbose=False
)
topic = input("Enter a topic: ")
score = 0

for i in range(3):
    print(f"\n--- Question {i + 1} / 3 ---")

    response = model.create_chat_completion(
        messages=[
            {
                "role": "system",
                "content": "Generate a multiple choice question with 4 options (A, B, C, D). Write the correct answer at the end as 'Answer: X'."
            },
            {"role": "user", "content": topic},
        ],
        max_tokens=256,
        temperature=0.9,
    )

    quiz_text = response["choices"][0]["message"]["content"]
    print(quiz_text)

    # doğru cevabı bul
    correct = "?"
    for line in quiz_text.split("\n"):
        if "Answer:" in line:
            correct = line.split("Answer:")[-1].strip()[0].upper()
            break

    user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

    if user_answer == correct:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {correct}")

print(f"\nFinal score: {score} / 3")