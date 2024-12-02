
# Static Code Analysis App

## Project Overview
The Static Code Analysis App is designed to analyze Python code for maintainability, quality issues, and security vulnerabilities. It provides clear metrics, actionable insights, and an easy-to-use interface powered by Streamlit.

---

## Installation Instructions

### Prerequisites
1. Python 3.9 or later.
2. Streamlit, Radon, Bandit, and Flake8 installed.

### Setup
1. Clone the repository:
   ```bash
   git clone <GitHub-link>

	2.	Navigate to the project directory:

cd SWETeamDemo


	3.	Install the required dependencies:

pip install -r requirements.txt

### Usage Instructions

	1.	Run the application:

streamlit run analyzer.py


	2.	Open the URL provided by Streamlit in your browser.
	3.	Paste your Python code into the text box and click “Analyze.”

## Tabs

	•	Code Analysis: Displays raw metrics and maintainability indices.
	•	Code Quality: Highlights formatting and quality issues using Flake8.
	•	Security Vulnerability: Identifies security risks using Bandit.

## Examples

	•	Input vulnerable code to test security analysis:

eval("os.system('rm -rf /')")

## Team Members

	•	Andrew Gonzalez
	•	Christian Williams
	•	Hugo Padilla
	•	Calissa Huizar

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---