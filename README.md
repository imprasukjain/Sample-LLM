# Streamlit Question Answering App

This project implements a simple question-answering web application using Streamlit and HuggingFace. Users can ask questions and get responses generated from a language model.

## Features

- Ask questions in natural language and get answers generated from AI
- Backed by HuggingFace and state-of-the-art language models like Flan-T5
- Simple Streamlit interface to type questions and view answers
- Loads language model and credentials securely from the .env file

## Usage

### Prerequisites

- Python 3.6+
- [Streamlit](https://docs.streamlit.io/library/get-started/installation) installed
- HuggingFace Hub account and [API token](https://huggingface.co/settings/token) 

### Setup

1. Clone the repo
   ```bash
   git clone https://github.com/<imprasukjain>/Sample-LLM
   ```
2. Navigate into the project directory
   ```bash 
   cd app.py
   ```
3. Install requirements
   ```bash
   pip install -r requirement.txt 
   ```  
4. Create a `.env` file with your HuggingFace token
   ```
   HF_API_KEY=abcd1234
   ```
   
### Running the App

Execute the Streamlit app:

```bash
streamlit run app.py
```  

The app will now be viewable at http://localhost:8501. 

Ask questions in natural language and the latest AI capabilities from HuggingFace will generate relevant answers!

## License

This project is licensed under the [MIT license](LICENSE). Feel free to reuse and adapt the code for your own projects.
