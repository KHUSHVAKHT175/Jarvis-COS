import json
import os

# Минимальный реестр модулей
module_registry = {
    "Dialog": "modules.dialog",
    "Scheduler": "modules.scheduler",
    "Logic": "modules.logic"
}

age_requirements = {
    "Dialog": 0,
    "Scheduler": 0,
    "Logic": 0
}

MEMORY_FILE = "src/core/memory_state.json"

# ---------------- Memory ----------------
class HybridMemory:
    def __init__(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                try:
                    saved = json.load(f)
                except Exception:
                    saved = {}
            self.cache = saved.get("cache", {})
            self.archive = saved.get("archive", {})
            self.weights = saved.get("weights", {})
        else:
            self.cache = {}
            self.archive = {}
            self.weights = {}

    def store(self, task, result):
        self.cache[task["name"]] = result
        self.weights[task["name"]] = self.weights.get(task["name"], 1.0) + 0.1
        if len(self.cache) > 10:
            key, val = self.cache.popitem()
            self.archive[key] = val
        self.save()

    def get(self, key):
        return self.cache.get(key) or self.archive.get(key)

    def save(self):
        state = {
            "cache": self.cache,
            "archive": self.archive,
            "weights": self.weights
        }
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)

    def clear_all(self):
        self.cache = {}
        self.archive = {}
        self.weights = {}
        self.save()

# ---------------- Module Loader ----------------
def load_allowed_modules(user_age):
    allowed = {}
    for name, path in module_registry.items():
        if user_age >= age_requirements.get(name, 0):
            try:
                allowed[name] = __import__(path, fromlist=[""])
            except Exception:
                allowed[name] = None  # Если модуль не найден
    return allowed

# ---------------- Main ----------------
def main():
    print("=" * 32)
    print(" JARVIS‑COS Minimal: Терминальный запуск")
    print("=" * 32)

    try:
        user_age = int(input("Введите возраст пользователя: "))
    except Exception:
        user_age = 0

    modules = load_allowed_modules(user_age)
    memory = HybridMemory()

    print(f"\n[Jarvis‑COS Minimal] Модули: {list(modules.keys())}")
    print("Команды: 'chat', 'exit', 'status'\n")

    while True:
        cmd = input("Jarvis‑COS> ").strip()
        if cmd == "chat":
            if modules.get("Dialog"):
                modules["Dialog"].chat(memory)
            else:
                print("Модуль Dialog не доступен.")
        elif cmd == "status":
            print(f"[Memory] Cache: {list(memory.cache.keys())}")
            print(f"[Memory] Archive: {list(memory.archive.keys())}")
        elif cmd in ("exit", "shutdown", "stop"):
            print("[Jarvis‑COS Minimal] Завершение работы. Goodbye!")
            break
        else:
            print("[Jarvis‑COS Minimal] Только 'chat', 'status' или 'exit'.")

if __name__ == "__main__":
    main()
