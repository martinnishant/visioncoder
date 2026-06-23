import json
import ollama

def generate_website(user_prompt):
    prompt = f"""
Generate a website.

Return ONLY valid JSON.

Format:

{{
    "index.html":"...",
    "style.css":"...",
    "script.js":"..."
}}

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
        ]
    )

    return response["message"]["content"]