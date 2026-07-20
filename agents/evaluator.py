import ollama


class EvaluatorAgent:

    def __init__(self, model="llama3.2"):
        self.model = model

    def evaluate(self, previous_review: str, current_review: str):

        prompt = f"""
You are evaluating whether a webpage has improved.

Previous Review:

{previous_review}

Current Review:

{current_review}

Your task:

1. Compare both reviews.

2. Decide whether the webpage improved.

Return ONLY this JSON:

{{
    "improved": true,
    "confidence": 0.92,
    "reason": "Spacing and button styling improved significantly."
}}
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
                "temperature": 0
            }
        )

        return response["message"]["content"]