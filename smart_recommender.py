import json
import os
import numpy as np

DB_FILE = "data/database.json"


def initialize_database():
    if os.path.exists(DB_FILE):
        return
    data = {
        "games": [
            {"id": 1,  "title": "Cyber-City 2088",         "tags": ["sci-fi", "rpg", "open-world", "action"],          "req_cpu": 8, "req_gpu": 8, "req_ram": 16},
            {"id": 2,  "title": "Farm Simulator X",         "tags": ["casual", "farming", "multiplayer", "relaxing"],   "req_cpu": 3, "req_gpu": 2, "req_ram": 4},
            {"id": 3,  "title": "Galactic Shooter",         "tags": ["action", "sci-fi", "fps", "multiplayer"],         "req_cpu": 6, "req_gpu": 6, "req_ram": 8},
            {"id": 4,  "title": "Fantasy Quest",            "tags": ["rpg", "fantasy", "open-world", "singleplayer"],   "req_cpu": 5, "req_gpu": 5, "req_ram": 8},
            {"id": 5,  "title": "Pixel Dungeon",            "tags": ["rpg", "pixel", "roguelike", "singleplayer"],      "req_cpu": 2, "req_gpu": 1, "req_ram": 2},
            {"id": 6,  "title": "Neon Racer Underground",   "tags": ["racing", "arcade", "multiplayer", "neon"],        "req_cpu": 5, "req_gpu": 6, "req_ram": 8},
            {"id": 7,  "title": "Shadow Protocol",          "tags": ["stealth", "action", "thriller", "singleplayer"],  "req_cpu": 7, "req_gpu": 7, "req_ram": 12},
            {"id": 8,  "title": "Minecraft Realms 2",       "tags": ["sandbox", "survival", "multiplayer", "casual"],   "req_cpu": 4, "req_gpu": 3, "req_ram": 8},
            {"id": 9,  "title": "Stellar Conquest",         "tags": ["strategy", "sci-fi", "4x", "singleplayer"],       "req_cpu": 6, "req_gpu": 4, "req_ram": 16},
            {"id": 10, "title": "Haunted Hollow",           "tags": ["horror", "survival", "puzzle", "singleplayer"],   "req_cpu": 5, "req_gpu": 5, "req_ram": 8},
            {"id": 11, "title": "Iron Battalion",           "tags": ["ww2", "strategy", "multiplayer", "simulation"],   "req_cpu": 7, "req_gpu": 6, "req_ram": 12},
            {"id": 12, "title": "Cursed Kingdoms",          "tags": ["dark-fantasy", "rpg", "souls-like", "singleplayer"], "req_cpu": 8, "req_gpu": 9, "req_ram": 16},
            {"id": 13, "title": "Velocity Strike",          "tags": ["fps", "esports", "competitive", "multiplayer"],   "req_cpu": 6, "req_gpu": 5, "req_ram": 8},
            {"id": 14, "title": "Ancient Horizons",         "tags": ["historical", "open-world", "adventure", "singleplayer"], "req_cpu": 9, "req_gpu": 9, "req_ram": 24},
            {"id": 15, "title": "Cozy Cafe Tycoon",         "tags": ["casual", "tycoon", "management", "relaxing"],     "req_cpu": 2, "req_gpu": 1, "req_ram": 4},
            {"id": 16, "title": "Deep Sea Chronicles",      "tags": ["exploration", "survival", "underwater", "singleplayer"], "req_cpu": 6, "req_gpu": 7, "req_ram": 12},
            {"id": 17, "title": "Mech Arena Wars",          "tags": ["mech", "action", "sci-fi", "multiplayer"],        "req_cpu": 7, "req_gpu": 8, "req_ram": 16},
            {"id": 18, "title": "Verdant Valley",           "tags": ["farming", "life-sim", "casual", "multiplayer"],   "req_cpu": 3, "req_gpu": 2, "req_ram": 4},
            {"id": 19, "title": "Quantum Break: Origins",   "tags": ["sci-fi", "puzzle", "time-travel", "singleplayer"], "req_cpu": 7, "req_gpu": 6, "req_ram": 12},
            {"id": 20, "title": "Battle Royale: Zero Hour", "tags": ["battle-royale", "fps", "survival", "multiplayer"], "req_cpu": 8, "req_gpu": 8, "req_ram": 16}
        ],
        "hardware": [
            {"type": "cpu", "name": "Budget Core i3",    "score": 3,  "price": "$100"},
            {"type": "cpu", "name": "Mid-Range Ryzen 5", "score": 6,  "price": "$200"},
            {"type": "cpu", "name": "High-End Core i9",  "score": 9,  "price": "$500"},
            {"type": "gpu", "name": "Basic GTX 1650",    "score": 4,  "price": "$150"},
            {"type": "gpu", "name": "Solid RTX 3060",    "score": 7,  "price": "$300"},
            {"type": "gpu", "name": "Ultra RTX 4090",    "score": 10, "price": "$1600"}
        ]
    }
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def load_database():
    with open(DB_FILE) as f:
        return json.load(f)


def tag_similarity(user_tags, game_tags, all_known_tags):
    user_vec = np.array([1 if t in user_tags else 0 for t in all_known_tags])
    game_vec = np.array([1 if t in game_tags else 0 for t in all_known_tags])

    dot = np.dot(user_vec, game_vec)
    user_norm = np.linalg.norm(user_vec)
    game_norm = np.linalg.norm(game_vec)

    if user_norm == 0 or game_norm == 0:
        return 0.0

    return dot / (user_norm * game_norm)


def pc_meets_game_requirements(user_cpu, user_gpu, user_ram, game):
    return (
        user_cpu >= game["req_cpu"] and
        user_gpu >= game["req_gpu"] and
        user_ram >= game["req_ram"]
    )


def find_cheapest_sufficient_upgrade(hardware_list, component_type, min_score_needed):
    candidates = [
        h for h in hardware_list
        if h["type"] == component_type and h["score"] >= min_score_needed
    ]

    if not candidates:
        return None

    cheapest = candidates[0]
    for item in candidates[1:]:
        if item["score"] < cheapest["score"]:
            cheapest = item
    return cheapest


class GameRecommender:
    def __init__(self):
        db = load_database()
        self.games = db["games"]
        self.hardware = db["hardware"]
        self.known_tags = sorted({tag for game in self.games for tag in game["tags"]})
        self.user_cpu = 0
        self.user_gpu = 0
        self.user_ram = 0

    def set_pc_specs(self, cpu, gpu, ram):
        self.user_cpu = cpu
        self.user_gpu = gpu
        self.user_ram = ram

    def get_ranked_matches(self, user_tags):
        matches = []

        for game in self.games:
            score = tag_similarity(user_tags, game["tags"], self.known_tags)

            if score == 0:
                continue

            runnable = pc_meets_game_requirements(
                self.user_cpu, self.user_gpu, self.user_ram, game
            )
            matches.append({
                "title": game["title"],
                "match_score": score,
                "runnable": runnable,
                "req_cpu": game["req_cpu"],
                "req_gpu": game["req_gpu"],
            })

        matches.sort(key=lambda m: m["match_score"], reverse=True)
        return matches

    def get_upgrade_suggestions(self, req_cpu, req_gpu):
        cpu_upgrade = find_cheapest_sufficient_upgrade(self.hardware, "cpu", req_cpu)
        gpu_upgrade = find_cheapest_sufficient_upgrade(self.hardware, "gpu", req_gpu)
        return cpu_upgrade, gpu_upgrade


def prompt_pc_specs(recommender):
    print("Rate your hardware 1-10  (1 = potato, 10 = overkill).")
    while True:
        try:
            cpu = int(input("CPU score (1-10): "))
            gpu = int(input("GPU score (1-10): "))
            ram = int(input("RAM in GB: "))
        except ValueError:
            print("Numbers only.\n")
            continue

        if not (1 <= cpu <= 10 and 1 <= gpu <= 10 and ram > 0):
            print("CPU/GPU must be 1-10, RAM must be positive.\n")
            continue

        recommender.set_pc_specs(cpu, gpu, ram)
        break


def run_game_search(recommender):
    raw_input = input("Tags you like (e.g. sci-fi, rpg, action): ").lower()
    user_tags = [t.strip() for t in raw_input.split(',')]

    matches = recommender.get_ranked_matches(user_tags)

    if not matches:
        print("No matches. Try option 2 to see what tags exist.\n")
        return

    print(f"\n{len(matches)} match(es):\n")
    for i, match in enumerate(matches, 1):
        pct = round(match["match_score"] * 100)
        status = "OK" if match["runnable"] else "needs upgrade"
        print(f"{i}. {match['title']}  ({pct}% match, {status})")

        if match["runnable"]:
            continue

        cpu_upgrade, gpu_upgrade = recommender.get_upgrade_suggestions(
            match["req_cpu"], match["req_gpu"]
        )
        print("   To run this:")
        if recommender.user_cpu < match["req_cpu"] and cpu_upgrade:
            print(f"     CPU: {cpu_upgrade['name']} — {cpu_upgrade['price']}")
        if recommender.user_gpu < match["req_gpu"] and gpu_upgrade:
            print(f"     GPU: {gpu_upgrade['name']} — {gpu_upgrade['price']}")
    print()


def main():
    initialize_database()
    recommender = GameRecommender()

    print("\nGame & Hardware Recommender")
    print("-" * 28)

    prompt_pc_specs(recommender)

    while True:
        print("\n1. Find games")
        print("2. List tags")
        print("3. Quit")
        choice = input("> ").strip()

        if choice == '1':
            run_game_search(recommender)
        elif choice == '2':
            print(", ".join(recommender.known_tags))
        elif choice in ('3', 'exit', 'q'):
            break
        else:
            print("1, 2, or 3.")


if __name__ == "__main__":
    main()
