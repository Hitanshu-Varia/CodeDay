import datetime
import random
import os
import sys

def update_readme():
    readme_path = "README.md"

    if not os.path.isfile(readme_path):
        print("❌ README.md not found. Exiting...", file=sys.stderr)
        sys.exit(1)
    
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        emoji = random.choice(["🌱", "🌿", "🍃", "🧠", "⚡", "🖖", "🐍", "👨‍💻"])
        line = f"\n<!-- Daily ping at {timestamp} {emoji} -->"
        
        with open(readme_path, "a", encoding="utf-8") as f:
            f.write(line)
        
        print(f"✅ Successfully appended to README.md: {line.strip()}")

    except Exception as e:
        print(f"❌ Error while writing to README.md: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    update_readme()
