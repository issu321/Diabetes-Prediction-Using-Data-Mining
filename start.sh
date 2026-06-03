#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
source venv/bin/activate
echo "🚀 Starting Diabetes Prediction Application..."
echo "📱 Open your browser and navigate to: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the server"
echo ""
python3 -m streamlit run app.py
