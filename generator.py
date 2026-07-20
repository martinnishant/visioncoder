import ollama


def generate_website(user_prompt):

    print("Connecting to qwen2.5-coder...")

    prompt = f"""
Generate a small website.

Return ONLY JSON.

Do not add markdown.

Format:

{{
"index.html":"html code",
"style.css":"css code",
"script.js":"javascript code"
}}

Keep code short.

Task:
{user_prompt}
"""

    response = ollama.chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature":0,
            "num_predict":800
        }
    )

    print("Model response received")

    return response["message"]["content"]