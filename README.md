<div align="center">
👁️‍🗨️ VisionCoder

A self-correcting multi-agent system that builds, critiques, and rewrites websites from a single prompt.

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=7C3AED&center=true&vCenter=true&width=720&lines=Prompt+in.+Website+out.;Coder+Agent+builds+it.;Vision+Agent+reviews+it.;Reflector+plans+fixes.;Fixer+rewrites+it.;All+locally.+All+autonomous." alt="Typing SVG" /><br/><p align="center"> <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Ollama-Local%20LLMs-000000?style=for-the-badge&logo=ollama&logoColor=white" /> <img src="https://img.shields.io/badge/LLaVA-Vision%20Model-FF6F00?style=for-the-badge&logo=openai&logoColor=white" /> <img src="https://img.shields.io/badge/Playwright-Headless%20Browser-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" /> <img src="https://img.shields.io/badge/Agents-Multi--Agent%20System-7C3AED?style=for-the-badge&logo=robotframework&logoColor=white" /> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" /> </p><p align="center"> <a href="#-demo"><b>🎬 Demo</b></a> • <a href="#-architecture"><b>🏗️ Architecture</b></a> • <a href="#-how-it-works"><b>⚙️ How it Works</b></a> • <a href="#-quick-start"><b>🚀 Quick Start</b></a> • <a href="#-tech-stack"><b>🧰 Tech Stack</b></a> </p></div>
🔥 What is VisionCoder?

VisionCoder is a fully local, multi-agent AI system that turns a single natural-language prompt into a polished, working website — and then critiques and improves itself by looking at what it just built.

It does this by orchestrating four specialised AI agents in a feedback loop:

Agent	Model	Role
🛠️ Coder	qwen2.5-coder	Generates HTML / CSS / JS from a prompt
👁️ Vision Reviewer	LLaVA	Inspects a screenshot and reports UI issues
🧠 Reflector / Planner	llama3.2	Converts review issues into a concrete fix-plan
🔧 Fixer	qwen2.5-coder	Rewrites the code to address every issue
The whole pipeline runs locally via Ollama — no API keys, no cloud costs, no data leaving your machine.

🎬 Demo

Run the app, type a prompt, and watch four agents collaborate in real time.

<p align="center"> <img src="screenshots/architecture.png" alt="VisionCoder architecture" width="820" /> </p><p align="center"> <sub>👆 The full self-correcting agent loop — coder → preview → vision review → plan → fix → save.</sub> </p><details> <summary><b>📸 Click here to see before / after screenshots from a real run</b></summary><br/>
Prompt: Build a portfolio site for a photographer with a dark theme and a gallery.

Before self-correction (v1)	After self-correction (v2)
v1	v2
The Vision Reviewer flagged issues like “images not aligned, contrast too low, CTA button invisible” → the Reflector turned those into a fix-plan → the Fixer rewrote the code → v2 looks like an actual product.

</details>
🏗️ Architecture

See the diagram above ☝️ — every box is a real Python module, every arrow is a function call in main.py.

The key idea: the system sees its own output and reasons about it — closing the gap between generation and quality.

⚙️ How it Works

The main.py orchestrator executes a fixed 10-step pipeline:

#	Step	Module	What happens
1	generate_website()	generator.py	Sends prompt to qwen2.5-coder → gets raw JSON
2	extract_json()	utils.py	Robust regex-based JSON extraction
3	save_project()	tools/file_writer.py	Writes index.html, style.css, script.js
4	preview_project()	tools/executor.py	Spins up python -m http.server 8000
5	capture_screenshot()	tools/screenshot.py	Headless Chromium captures current_ui.png
6	review_ui()	agents/reviewer.py	LLaVA critiques the screenshot
7	create_plan()	agents/reflector.py	llama3.2 drafts an improvement plan
8	FixAgent.fix_project()	agents/fixer.py	qwen2.5-coder rewrites the code
9	save_project()	tools/file_writer.py	Overwrites the workspace with the fix
10	Done	—	A better website now lives on disk
📂 Project Structure

text

visioncoder/
│
├── main.py                    # 🧭 Orchestrator — wires the 10-step pipeline
├── graph.py                   # 🕸️  Optional graph representation of the pipeline
├── generator.py               # 🛠️  Coder Agent (qwen2.5-coder)
├── utils.py                   # 🔍  JSON extraction from LLM output
├── test_llava.py              # 👁️  Standalone LLaVA smoke test
├── requirements.txt           # 📦  Runtime dependencies
├── LICENSE                    # ⚖️  MIT
│
├── agents/                    # 🤖 Multi-agent brains
│   ├── reviewer.py            #   • Vision Reviewer (LLaVA)
│   ├── reflector.py           #   • Planner / Reflector (llama3.2)
│   └── fixer.py               #   • Fixer Agent (qwen2.5-coder)
│
├── tools/                     # 🧰 Side-effect utilities
│   ├── file_writer.py         #   • Writes JSON → workspace files
│   ├── executor.py            #   • Spawns local HTTP server
│   └── screenshot.py          #   • Playwright headless capture
│
├── workspace/                 # 🏠 Generated website lives here
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/               # 📸 Captured UI snapshots
│   └── current_ui.png
│
└── plans/                     # 🗒️  Improvement plans (per run)
└── reviews/                   # 📝  Reviewer outputs (per run)
🚀 Quick Start

1. Prerequisites

Python 3.10+
Ollama installed and running
Pull the three models used by the agents:
Bash

ollama pull qwen2.5-coder:7b
ollama pull llava
ollama pull llama3.2
💡 qwen2.5-coder:3b is also supported as a lighter fallback (see agents/fixer.py).

2. Install

Bash

git clone https://github.com/martinnishant/visioncoder.git
cd visioncoder
pip install -r requirements.txt
playwright install chromium
3. Run

Bash

python main.py
Then type a prompt when asked, e.g.:

text

> Enter project description: Build a minimalist landing page for a coffee shop with a hero, menu, and contact form.
Watch the agents do their thing. When it's done:

The website is at workspace/index.html
A screenshot is at screenshots/current_ui.png
The review is in reviews/
The plan is in plans/
Press Enter to shut down the local server.

🧰 Tech Stack

Core

🐍 Python 3.10+ — application layer
🦙 Ollama — local model serving
🧠 qwen2.5-coder — code generation & fixing
👁️ LLaVA — vision-language review
💬 llama3.2 — reasoning / planning
Tooling

🎭 Playwright — headless browser for screenshots
🌐 http.server — zero-dependency local preview
📄 Regex + JSON — robust model-output parsing
Design Principles

✅ 100% local — no external API calls
✅ Composable agents — each agent is one Python file
✅ Deterministic temperature — temperature=0 for reproducibility
✅ Self-correcting loop — generation is just the first pass
🗺️ Roadmap

 Multi-agent generate → review → fix loop
 Vision-based UI critique
 Local-only execution via Ollama
 Streaming agent outputs in a TUI dashboard
 Iterative fix loop (run reviewer again on the fixed site)
 Pluggable model registry (config.yaml)
 Optional cloud LLM fallback (OpenAI / Anthropic)
 Web UI wrapper (FastAPI + React)
🧠 Why this project matters

Most "AI website builders" stop at generation. VisionCoder closes the loop: it looks at what it built, judges it like a human reviewer, and rewrites it like an engineer.

That single change — adding a vision critic to a code generator — converts a toy demo into a system that gets visibly better with every iteration.

It also demonstrates, in one self-contained repo:

🤖 Multi-agent orchestration (agent roles + a fixed graph)
🧠 Prompt engineering for vision + code LLMs
🛠️ Tool use (file I/O, subprocess, browser automation)
🔁 Self-reflective / self-correcting AI (a real production pattern)
👤 Author

<div align="center">
Nishant Tomar
B.Tech CSE — AI & Data Engineering · Lovely Professional University

GitHub
LinkedIn
Email

</div>
⭐ Show your support

If VisionCoder caught your eye, give it a star — it helps more than you think.
And if you fork it, build something weird on top of it, and tag me — I want to see it.

<div align="center">
<sub>Built with 🧠 + ☕ by <a href="https://github.com/martinnishant">@martinnishant</a></sub>
</div>
