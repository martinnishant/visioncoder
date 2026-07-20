from generator import generate_website
from tools.file_writer import save_project
from utils import extract_json
from tools.executor import preview_project
from tools.screenshot import capture_screenshot
from agents.reviewer import review_ui
from agents.reflector import create_plan

user_prompt = input("Enter project description: ")

print("1. Generating website...")
result = generate_website(user_prompt)

print("2. Parsing JSON...")
files = extract_json(result)

print("3. Saving files...")
save_project(files)

print("4. Starting server...")
server = preview_project()

print("5. Taking screenshot...")
screenshot_path = capture_screenshot()

print("6. Reviewing UI...")
review = review_ui(screenshot_path)

print("\n===== UI REVIEW =====")
print(review)
print("=====================\n")

print("7. Creating Improvement Plan...")
plan = create_plan(review)

print("\n===== IMPROVEMENT PLAN =====")
print(plan)
print("============================\n")

print(f"Screenshot saved: {screenshot_path}")

input("Press Enter to stop server...")

server.terminate()