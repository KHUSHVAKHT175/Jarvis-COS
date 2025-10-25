import json
import os

MEMORY_FILE = "src/core/memory_state.json"

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
