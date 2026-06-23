from generator import generate_website
from file_writer import save_project
from utils import extract_json
from executor import preview_project

user_prompt = input("Enter project description: ")

result = generate_website(user_prompt)

files = extract_json(result)

save_project(files)

print("Project generated successfully.")

server = preview_project()

input("Press Enter to stop server...")

server.terminate()