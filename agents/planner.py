import ollama


class PlannerAgent:
    """
    Converts a user's vague request into
    a detailed engineering specification.
    """

    def __init__(self, model="llama3.2"):
        self.model = model

    def create_plan(self, user_request: str) -> str:

        prompt = f"""
You are an expert Software Architect.

Convert the following request into a structured engineering specification.

User Request:
{user_request}

Your specification should include:

1. Project Type
2. Target Users
3. Features
4. UI Components
5. Color Theme
6. Layout
7. Responsiveness
8. Technical Requirements
9. Accessibility Notes

Be concise but complete.
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