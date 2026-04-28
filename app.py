print("GenAI Data Project Started...")

import pandas as pd
import ollama

# Load CSV
df = pd.read_csv("data.csv")

# Convert data to text
data_text = df.to_string()

# AI function
def ask_ai(prompt):
    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

# MAIN LOOP
while True:
    query = input("\nAsk something about the data (type exit to stop): ")

    if query.lower() == "exit":
        break

    full_prompt = f"""
You are a data analyst.

Here is the dataset:
{data_text}

Answer this question:
{query}
"""

    answer = ask_ai(full_prompt)

    print("\n📊 AI Answer:\n", answer)