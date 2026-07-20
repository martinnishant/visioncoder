import ollama
import json


class FixAgent:
    """
    Responsible for improving an existing project.

    Inputs:
        - HTML
        - CSS
        - JavaScript
        - Improvement Plan

    Output:
        Dictionary containing:
            index.html
            style.css
            script.js
    """

    def __init__(self, model="qwen2.5-coder:3b"):
        self.model = model

    def fix_project(
        self,
        html: str,
        css: str,
        javascript: str,
        improvement_plan: str
    ):

        prompt = f"""
You are a Senior Frontend Engineer.

Your job is to improve an existing website.

------------------------
CURRENT HTML
------------------------

{html}

------------------------
CURRENT CSS
------------------------

{css}

------------------------
CURRENT JAVASCRIPT
------------------------

{javascript}

------------------------
IMPROVEMENT PLAN
------------------------

{improvement_plan}

Requirements:

1. Apply EVERY improvement.

2. Preserve functionality.

3. Do NOT remove existing features.

4. Improve only what is necessary.

5. Return ONLY valid JSON.

Example format:

{{
    "index.html":"...",
    "style.css":"...",
    "script.js":"..."
}}

No markdown.

No explanations.

No code fences.
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