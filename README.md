# Real-Time Collaborative Code Editor

A FastAPI-based platform for real-time code collaboration with AI-assisted debugging using OpenAI.

## Setup Instructions
1. Clone the repo: `git clone <repo-url>`
2. Install Docker and Docker Compose.
3. Set your OpenAI API key:
   - Edit `docker-compose.yml` and replace `your-openai-api-key-here` with your key from [platform.openai.com](https://platform.openai.com).
   - Alternatively, set it as an environment variable: `export OPENAI_API_KEY=your-key`
4. Run: `docker-compose up --build`
5. Access the app at `http://localhost:8000`
6. View API docs at `http://localhost:8000/docs`

## Running Tests
- Install pytest: `pip install pytest`
- Run: `pytest tests/`

## Run using main.py
- Run: `python main.py`
- Set your OpenAI API key:
   [platform.openai.com](https://platform.openai.com)
   replace your api key[using cmd] : $env:OPENAI_API_KEY="sk-..."

