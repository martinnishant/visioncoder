import json
import ollama


class CoderAgent:
    """
    Generates an entire project
    from an engineering specification.
    """

    def __init__(self, model="qwen2.5-coder:3b"):
        self.model = model

    def generate_project(self, specification: str):

        prompt = f"""
You are an expert Frontend Engineer.

Below is an engineering specification.

{specification}

Generate the project.

Rules:

Return ONLY JSON.

Format:

{{
    "index.html":"...",
    "style.css":"...",
    "script.js":"..."
}}

Do not use markdown.

Do not explain.

Return valid JSON only.
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0,
                "num_predict": 1500
            }
        )

        result = response["message"]["content"]

        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        return json.loads(result)