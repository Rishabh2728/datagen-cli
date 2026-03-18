<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B0000,100:4B0082&height=200&section=header&text=DataGen%20CLI&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35" />
</p>

<p align="center">
  <b>Schema-driven synthetic data generation for developers & data scientists</b>
</p>

<p align="center">
  ⚡ Python API & CLI • 📊 DataFrame Ready • 🔍 Strict Validation • 📁 CSV / JSON / Excel
</p>

---

# 🚀 DataGen CLI

> Built an official Python library with **12K+ downloads** — designed to solve a real problem faced by data science students and developers:  
> **getting clean, structured, and usable datasets instantly.**

---

## ✨ About

Most tools generate random, unrealistic data.

**DataGen CLI is different.**

👉 Define your own schema  
👉 Generate meaningful, constraint-aware datasets  
👉 Use directly in Python or via CLI  

---

## 🔥 Key Features

- 🧠 **Schema-driven generation**
- 📊 **Returns pandas DataFrame**
- 💻 **Python + CLI support**
- 📁 Export to **CSV, JSON, Excel**
- 🔍 **Strict validation system**
- ⚡ Lightweight & fast
- 🧪 Fully tested (**24/24 tests passed**)

---

## ⚡ Quick Demo

### 🐍 Python

```python
from datagen import generate

schema = {
    "name": {"type": "name"},
    "age": {"type": "int", "min": 18, "max": 60},
    "salary": {"type": "float", "min": 30000, "max": 100000}
}

df = generate(schema=schema, rows=5)
print(df)
💻 CLI
datagen generate schema.json --rows 100 --output data.csv
🧾 Example Output
        name   age    salary
0   Rahul Sharma   25   54000
1   Priya Verma   32   72000
2   Aman Gupta    28   61000
🧩 Architecture
datagen/
│
├── core/
│   ├── engine.py
│   ├── defaults.py
│   ├── schema_normalizer.py
│   └── schema_validator.py
│
├── cli/
│   ├── app.py
│   └── main.py
│
├── __init__.py
│
tests/
├── test_cli.py
└── test_core.py
⚙️ Phase 1 — Core Engine (Completed ✅)
✔️ Implemented

Schema-driven engine (DataGenerationEngine)

Python API (generate() → DataFrame)

CLI (Typer-based interface)

Schema normalization

Strict validation system

File export support

Testing suite

🔒 Validation Rules

✔️ min <= max for numeric fields

✔️ Precision must be positive

✔️ Date ranges must be valid

✔️ Choice fields must not be empty

✔️ Unsupported types are rejected

🚀 Installation
pip install datagen
💻 CLI Commands
Command	Description
generate	Generate dataset
preview	Preview sample data
validate	Validate schema
📤 Export Formats

CSV

JSON

Excel (.xlsx)

⚡ Performance

⚡ Lightweight package (KBs only)

🚀 Tested with 1 crore rows × 17 columns

🧠 Efficient memory usage

🔮 Roadmap
Phase 2 (Next)

🌍 Region-based datasets (India 🇮🇳, US 🇺🇸)

🔗 Relationship-aware data
(city → state, salary → role)

Phase 3

🤖 Smart generation (learning from real datasets)

🧪 Testing
24 passed, 0 failed ✅

Includes:

Core engine tests

CLI tests

Validation tests

🤝 Contributing
git clone https://github.com/your-username/datagen-cli
cd datagen-cli
pip install -r requirements.txt
👨‍💻 Author

Rishabh Kumar

Built to solve a real-world problem faced during learning data science

Already helping thousands generate datasets instantly

Now evolving into a full-scale synthetic data engine

⭐ Support

If this project helped you:

👉 Star the repo
👉 Share it
👉 Use it in your projects

💡 Vision

Data shouldn’t be the bottleneck.
It should be generated instantly.