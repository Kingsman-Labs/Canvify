#!/usr/bin/env bash
# One-command local dev environment setup
set -e
cd backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
cd ../frontend && npm install
echo "Setup complete. Run 'uvicorn main:app --reload' in backend/ and 'npm run dev' in frontend/"
