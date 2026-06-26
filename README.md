# MalayalamLang

MalayalamLang is a small programming language project that allows users to write code using Malayalam keywords instead of Python keywords.

The project currently supports both Malayalam script and Roman Malayalam script. Internally, the code is translated into Python and executed, and the output is displayed back to the user through a web-based IDE.

## Why I Built This

The goal of this project is to make programming more accessible to Malayalam speakers and to explore concepts from programming language design such as translation, interpretation, lexing, parsing, and compiler construction.

## Current Features

* Malayalam keywords
* Roman Malayalam keywords
* Variables
* Print statements
* If / Else conditions
* For loops
* While loops
* Functions
* Web-based IDE

## Example

Malayalam Script:

```python
എ = 10
ബി = 20

കാണിക്കുക(എ + ബി)
```

Roman Malayalam Script:

```python
a = 10
b = 20

kanikkuka(a + b)
```

Both programs produce:

```text
30
```

## Project Structure

```text
backend/
    main.py
    translator.py
    keywords_malayalam.py
    keywords_latin.py

frontend/
    index.html
    ide.html
    style.css
    script.js

examples/
```

## How It Works

1. The user writes code in Malayalam or Roman Malayalam.
2. The translator replaces Malayalam keywords with their Python equivalents.
3. The translated Python code is executed.
4. The output is captured and displayed in the selected script.

## Future Work

The current version is based on keyword translation. Future versions may include:

* Lexer
* Parser
* AST generation
* Custom interpreter
* Syntax highlighting
* Better error messages
* Auto-completion

## Author

Sreeshant Nair

Computer Science (AI & Data Science) Student

GitHub: Sreeshant786
