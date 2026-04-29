import os
from llama_cpp import Llama

script_dir = os.path.dirname(os.path.abspath(__file__))

model = Llama(
    model_path=os.path.join(script_dir, "slm.gguf"),
    n_ctx=512,
    verbose=False
)
temperatures = [0.1, 0.5, 1.0, 1.5]
question = "What makes a good engineer?"

for i in range(len(temperatures)):
    temp = temperatures[i]

    response = model.create_chat_completion(
        messages=[{"role": "user", "content": question}],
        max_tokens=100,
        temperature=temp,
    )

    answer = response["choices"][0]["message"]["content"]

    print(f"\n--- Temperature {temp} ---")
    print(answer)

choice = int(input("\nWhich was best? (1-4): "))

if choice == 1:
    print("You prefer precise answers.")
elif choice == 2 or choice == 3:
    print("You prefer balanced answers.")
elif choice == 4:
    print("You prefer creative answers.")
else:
    print("Invalid choice.")