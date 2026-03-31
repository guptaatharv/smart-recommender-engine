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
2. **Navigate to the directory:**
   ```bash
   cd smart-recommender-engine
3. **Install the required dependencies**
   ```bash
   Install the required dependencies
4. **Run the application:**
   ```bash
   python smart_recommender.py


## 🎮 How It Works (Usage)

### 🖥️ Step 1: Enter System Specifications
Upon launching the CLI, you will be prompted to:
- Rate your **CPU** (out of 10)
- Rate your **GPU** (out of 10)
- Enter your **RAM** (in GB)
  ![Terminal Output](output/pc_making_requirements_out.png)

---

### 🎯 Step 2: Choose an Action
- Select `1` from the main menu to search for games

---

### 🎨 Step 3: Enter Preferences
- Input genres you like  
  *(e.g., sci-fi, action, rpg)*

---

### 📊 Step 4: View Results
The engine will display:

- 🎮 A **ranked list of recommended games**
- 📈 A **Match Percentage** for each game

#### Compatibility Indicators:
- ✅ Your PC **can run the game**
- ❌ Your PC **cannot run the game**
  - Includes **specific hardware upgrade suggestions**
