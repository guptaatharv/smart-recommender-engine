# 🚀 Smart Game & Hardware Recommender Engine

A Command-Line Interface (CLI) application built in Python that uses Machine Learning concepts to recommend video games based on user preferences. Furthermore, it checks if your PC can run the recommended games and suggests targeted hardware upgrades if needed!

This was built as a Bring Your Own Project (BYOP) for a 1st-year B.Tech Computer Science course.

## 📌 Project Statement
Gamers often purchase games they cannot run, while PC users hesitate to upgrade because they don't know which specific parts bottleneck their favorite genres. This project aims to bridge that gap. It utilizes **Cosine Similarity** to recommend games based on personal taste, evaluates the user's current PC specifications, and automatically suggests targeted hardware upgrades if a system bottleneck is detected.

## ✨ Features
* **AI Recommendation Logic:** Uses **NumPy** to calculate Cosine Similarity between user tag preferences and game genres.
* **Hardware Evaluation:** Compares user PC specifications (CPU, GPU, RAM) against minimum game requirements.
* **Smart Upgrade Suggestions:** If a user's PC falls short, the engine searches the database to recommend the cheapest CPU or GPU upgrade required to play the game.
* **Automated Data Storage:** Automatically generates a local `mock_database.json` file to store game and hardware data.
* **Robust Error Handling:** Safely handles incorrect user inputs without crashing the application.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `numpy`, `json`, `os`
* **Architecture:** Modular Object-Oriented Programming (OOP) / CLI

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/smart-recommender-engine.git
