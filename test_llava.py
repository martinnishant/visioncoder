import ollama
import time

start = time.time()

response = ollama.chat(
    model="llava",
    messages=[
        {
            "role": "user",
            "content": "Describe this image.",
            "images": ["screenshots/current_ui.png"]
        }
    ]
)

print(response["message"]["content"])
print(f"Time: {time.time() - start:.2f} seconds")