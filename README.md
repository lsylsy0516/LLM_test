# LLM_test
## How to use this repository
### 1. Clone the repository
```bash
git clone https://github.com/lsylsy0516/LLM_test.git
```
### 2. Install the required packages
```bash
pip install -r ./yolov5/requirements.txt
pip install openai  # 3.8
pip install anthropic
pip install socksio
pip install google-generativeai # 3.9 
```
### 3. Use YOLOv5 to create mask images
```bash
python my_detect.py
```
### 4. Create labels for the mask images
```bash
python txt_create.py
```
### 5. Use LLM Model to generate text and Compare(Now for GPT)
```bash
export OPENAI_API_KEY='your_openai_api_key'
export GEMINI_API_KEY='your_gemini_api_key'
export ANTHROPIC_API_KEY='your_claude_api_key'

python multi_gpt.py --model {gpt/gemini/claude}
```