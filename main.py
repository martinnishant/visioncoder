from pathlib import Path
from generator import generate_website
from tools.file_writer import save_project
from utils import extract_json
from tools.executor import preview_project
from tools.screenshot import capture_screenshot
from agents.reviewer import review_ui
from agents.reflector import create_plan
from agents.fixer import FixAgent

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

print("8. Loading current project...")

html = Path("workspace/index.html").read_text(encoding="utf-8")
css = Path("workspace/style.css").read_text(encoding="utf-8")
js = Path("workspace/script.js").read_text(encoding="utf-8")

print("9. Fixing project...")

fixer = FixAgent()

updated_files = fixer.fix_project(
    html=html,
    css=css,
    javascript=js,
    improvement_plan=plan
)

print("10. Saving improved project...")

save_project(updated_files)

print("Project improved successfully.")

print("\n===== IMPROVEMENT PLAN =====")
print(plan)
print("============================\n")

print(f"Screenshot saved: {screenshot_path}")

input("Press Enter to stop server...")

server.terminate()


print("\n==============================")
print("Self-Correction Cycle Complete!")
print("==============================")
