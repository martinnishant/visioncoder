import ollama


def create_plan(review: str):

    prompt = f"""
You are a senior frontend architect.

A UI reviewer found these issues:

{review}

Your task:

Convert these issues into a technical improvement plan.

Return ONLY bullet points.

Example:

- Increase button padding
- Center the login card
- Improve spacing
- Add consistent border radius
"""

    response = ollama.chat(
        model="llama3.2",
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