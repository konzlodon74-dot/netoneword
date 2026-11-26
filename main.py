import os

ENTRY = "Scrollpocalypse"

assert ENTRY.strip() == ENTRY and ENTRY, "entry must be non-blank with no padding"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert not any(c.isspace() for c in ENTRY), "entry must be exactly one word, no whitespace"
assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(ENTRY.encode("utf-8"))
