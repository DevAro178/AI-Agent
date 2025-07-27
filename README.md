# 🧠 AI Agent

A command-line AI coding agent that uses the Gemini API to interact with and manipulate a Python project directory. It supports reading, writing, executing, and listing files—all securely sandboxed within a specified directory.

---

## 🔧 Features

* 🔍 List directory contents and file details
* 📄 Read file content with a character limit
* 📝 Write or overwrite files safely
* ▶️ Execute Python scripts with optional arguments
* 🔄 Iterative function-call resolution using Gemini 2.0 Flash
* 🧪 Built-in unit tests for included calculator application
* 📦 Modular function-based architecture

---

## 🗂️ Project Structure

```
.
├── main.py                    # Main CLI entrypoint for the agent
├── tests.py                   # Tests core utility functions
├── calculator/                # Sample sandboxed project
│   ├── main.py
│   ├── tests.py
│   ├── README.md
│   ├── lorem.txt
│   ├── pkg/
│   │   ├── calculator.py
│   │   ├── render.py
│   │   └── morelorem.txt
├── functions/                 # Custom Gemini-compatible tools
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   ├── run_python_file.py
│   ├── call_function.py
│   ├── is_subdir.py
│   ├── config.py
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install python-dotenv google-generativeai
```

### 2. Set Up Environment Variable

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 3. Run the Agent

```bash
python main.py "Evaluate '3 + 5' using calculator" --verbose
```

The agent will attempt to resolve your request using Gemini’s function calling and the available tools.

---

## 📁 The `calculator/` App

A sample sandbox project the agent can interact with. It contains:

* A `Calculator` class that evaluates infix expressions
* A terminal-style result renderer
* Unit tests covering arithmetic and edge cases

Run it manually with:

```bash
python calculator/main.py "2 * 3 + 5"
```

Or test it with:

```bash
python calculator/tests.py
```

---

## 📜 Tools Defined for Gemini

Each tool is registered with a schema and securely scoped to operate within the `calculator/` directory:

* `get_files_info`: List file names, sizes, and whether they're directories
* `get_file_content`: Read the contents of a file (up to 10,000 characters)
* `write_file`: Create or overwrite a file with new content
* `run_python_file`: Execute any `.py` script with optional arguments

---

## 🧪 Testing Utility Functions

To test the core tool functions outside the AI loop:

```bash
python tests.py
```

---

## ⚠️ Security Notice

All tools are restricted to the `calculator/` subdirectory using path resolution logic. Attempts to access or modify files outside this scope will return an error.

---

## 📄 License

MIT License. Feel free to reuse and modify.
