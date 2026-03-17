# 🚀 DataGen CLI — Synthetic Dataset Generator

**Built by:** Rishabh Kumar
**Version:** 0.1.3
**License:** MIT (Non-Commercial) — For commercial use, contact: `rishabh.contact.info@gmail.com`

---

## 📌 Overview

**DataGen CLI** is a powerful command-line tool for generating realistic synthetic datasets with customizable columns, formats, and sizes.

It is designed for:

* 🧑‍💻 Developers (testing APIs & apps)
* 📊 Data Scientists (model training & experiments)
* 🏫 Students (projects & assignments)

---

## ✨ Key Features

* 🔹 **50+ Predefined Columns**

  * Customer data, sales, finance, logs, weather & more

* 🔹 **Multiple Export Formats**

  * CSV, Excel (XLSX), JSON

* 🔹 **Interactive CLI**

  * Easy-to-use prompts (no complex commands)

* 🔹 **Realistic Fake Data**

  * Powered by Faker for human-like datasets

* 🔹 **Custom Date Ranges**

  * Generate time-based data easily

* 🔹 **Lightweight & Fast**

  * Generates thousands to millions of rows efficiently

---

## ⚡ Installation

Install using pip:

```bash
pip install datagen-cli
```

Verify installation:

```bash
datagen --help
```

---

## 🚀 Quick Start

Run the generator:

```bash
datagen generate
```

---

## 🧪 Example Usage

### Step 1: Start CLI

```bash
datagen generate
```

### Step 2: Provide inputs

```text
Enter number of rows to generate: 10000
Enter start date (YYYY-MM-DD): 2022-01-01
Enter end date (YYYY-MM-DD): 2024-12-31

Available Columns:
1. OrderID   2. CustomerName   3. Country   4. Sales   5. Profit ...

Enter column numbers to include: 1,2,4,5

Enter folder path: ./data/
Enter file name: sample_data
Choose format (csv/xlsx/json): csv
```

### Output:

```text
Data generated successfully and saved to:
./data/sample_data.csv
```

---

## 📊 Supported Column Categories

| Category      | Examples                         |
| ------------- | -------------------------------- |
| Customer Data | Name, Email, Gender, Age, City   |
| Sales Data    | OrderID, Sales, Profit, Discount |
| Employment    | EmployeeName, Salary, JobTitle   |
| Logs          | IP_Address, Browser, LoginTime   |
| Weather       | Temperature, Humidity            |
| Finance       | AccountBalance, CreditScore      |
| Misc          | BooleanFlag, RandomText          |

---

## 🛠 Tech Stack

| Component       | Library  |
| --------------- | -------- |
| CLI Framework   | Typer    |
| Terminal UI     | Rich     |
| Fake Data       | Faker    |
| Data Processing | Pandas   |
| Excel Support   | OpenPyXL |

---

## 📦 Project Structure

```bash
datagen/
│
├── main.py          # CLI entry point
├── __init__.py
```

---

## 📈 Future Improvements (Roadmap)

* 🔥 Schema-based data generation
* 🌍 Region-specific datasets (India, US, etc.)
* 🔗 Column relationships (city → state mapping)
* ⚡ High-performance large dataset streaming
* 🧩 Plugin system for custom generators

---

## 👨‍💻 Developer

**Rishabh Kumar**
📧 Email: [rishabh.contact.info@gmail.com](mailto:rishabh.contact.info@gmail.com)
🌐 GitHub: https://github.com/Rishabh2728

---

## 📜 License

This project is licensed under **MIT (Non-Commercial Use Only)**.

For commercial licensing:
📩 Contact: `rishabh.contact.info@gmail.com`

---

## 🤝 Contributing

Contributions are welcome!

```bash
git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature
```

---

## 💡 Note

> Good datasets lead to better models.

**DataGen CLI helps you build, test, and experiment faster with clean and realistic synthetic data.**
