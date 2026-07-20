from playwright.sync_api import sync_playwright
import os

def capture_screenshot():
    os.makedirs("screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            viewport={
                "width": 800,
                "height": 600
            }
        )

        page.goto(
            "http://localhost:8000",
            wait_until="networkidle"
        )

        page.screenshot(
            path="screenshots/current_ui.png",
            full_page=True
        )

        browser.close()

    return "screenshots/current_ui.png"