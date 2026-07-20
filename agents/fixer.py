import ollama

def improve_code(review, html, css, js):

    prompt = f"""
You are a senior frontend engineer.

Review feedback:

{review}

Current HTML:

{html}

Current CSS:

{css}

Current JS:

{js}

Improve the website.

Return ONLY JSON:

{{
    "index.html":"...",
    "style.css":"...",
    "script.js":"..."
}}
"""

    response = ollama.chat(
        model="qwen2.5-coder:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]