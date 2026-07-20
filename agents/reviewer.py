import ollama

def review_ui(image_path):

    print("Sending image to LLaVA...")

    response = ollama.chat(
        model="llava",
        messages=[
            {
                "role":"user",
                "content": """
                You are an expert UI reviewer.

                Analyze this webpage screenshot.

                Do NOT describe the page.

                Only return:

                ISSUES:
                - issue 1
                - issue 2
                - issue 3

                If no issues exist, return:

                ISSUES:
                - No major issues found
                """,
                "images":[image_path]
            }
        ],
        options={
            "num_predict":100
        }
    )

    print("LLaVA finished")

    return response["message"]["content"]
# import ollama

# def review_ui(image_path):
#     print(f"Reviewing image: {image_path}")

#     response = ollama.chat(
#         model="llava",
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Describe this image.",
#                 "images": [image_path]
#             }
#         ]
#     )

#     print("LLaVA responded.")

#     return response["message"]["content"]