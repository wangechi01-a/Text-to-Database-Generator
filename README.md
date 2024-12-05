
# Natural Language to SQL Generator

QueryTranslator is a powerful application that transforms plain English text into SQL queries. Designed for data analysts, engineers, and database enthusiasts, it simplifies SQL query generation, enabling users to interact with databases using natural language commands.

---

## 🚀 Features

- **Natural Language Processing**: Converts plain English into SQL queries.
- **Real-Time Query Execution**: Executes SQL queries directly on your database.
- **User-Friendly Interface**: Built with [Streamlit](https://streamlit.io) for an interactive experience.
- **Customizable**: Supports various databases (e.g., SQLite, PostgreSQL, MySQL).

---

## 🛠️ How It Works

1. Enter a query in plain English (e.g., *"List all users' their names, phone numbers, email, address and registration_date"*).
2. QueryTranslator converts it into an SQL query (e.g., `List all users' names and emails." -> SELECT name, email FROM users;`).
3. View the results fetched from the connected database.

---

## 📂 Project Structure

```
QueryTranslator/
│
├── app.py               # Main application script
├── requirements.txt     # Dependencies
├── Dockerfile           # Optional: For containerization
├── README.md            # Project documentation
├── data/                # Folder for database files or CSVs
└── utils/               # Helper functions
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/QueryTranslator.git
cd QueryTranslator
```

### 2. Install Dependencies
Ensure you have Python 3.9+ installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Launch the App
Run the Streamlit app:
```bash
streamlit run app.py
```
The app will be accessible at `http://localhost:8501/`.

---

## 🖥️ Demo

Check out the live demo of QueryTranslator:  
**[Live Demo](https://github.com/user-attachments/assets/1f20e4e1-c7e0-4bc6-84c2-4e6de4faa084)**  



---

## 🧰 Requirements

- Python 3.9+
- Streamlit
- SQLAlchemy
- Google Gemini Pro API (optional: for NLP features)

---

## 🙌 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add a new feature'`.
4. Push your branch: `git push origin feature-name`.
5. Submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

