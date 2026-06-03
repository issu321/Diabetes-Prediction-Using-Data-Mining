#!/bin/bash
# =============================================================================
# Diabetes Prediction Using Data Mining - Installation Script (Linux/Mac)
# Project ID: EDUFYPML007
# Developed By: EduPhonix-Solution
# GitHub: https://github.com/issu321
# Repository: https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
echo "============================================================================="
echo "  🩺 DIABETES PREDICTION USING DATA MINING - INSTALLER"
echo "  Project ID: EDUFYPML007"
echo "  Developed By: EduPhonix-Solution"
echo "============================================================================="
echo -e "${NC}"

pip install -r requirements.txt

echo -e "${GREEN}✅ All dependencies installed successfully!${NC}"

echo -e "${YELLOW}🔄 Training machine learning models...${NC}"
python3 train_model.py

echo -e "${GREEN}✅ Models trained and saved successfully!${NC}"

cat > start.sh << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
source venv/bin/activate
echo "🚀 Starting Diabetes Prediction Application..."
echo "📱 Open your browser and navigate to: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the server"
echo ""
python3 -m streamlit run app.py
EOF

chmod +x start.sh

echo ""
echo -e "${GREEN}=============================================================================${NC}"
echo -e "${GREEN}  ✅ INSTALLATION COMPLETED SUCCESSFULLY!${NC}"
echo -e "${GREEN}=============================================================================${NC}"
echo ""
echo -e "${BLUE}🚀 To start the application, run:${NC}"
echo -e "${YELLOW}   ./start.sh${NC}"
echo ""
echo -e "${BLUE}📱 The application will be available at:${NC}"
echo -e "${YELLOW}   http://localhost:8501${NC}"
echo ""
echo -e "${BLUE}📝 Or manually activate and run:${NC}"
echo -e "${YELLOW}   source venv/bin/activate${NC}"
echo -e "${YELLOW}   streamlit run app.py${NC}"
echo ""
echo -e "${BLUE}👨‍💻 Developer: EduPhonix-Solution${NC}"
echo -e "${BLUE}🐙 GitHub: https://github.com/issu321${NC}"
echo -e "${BLUE}📁 Repository: https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining${NC}"
echo ""
