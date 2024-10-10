#!/usr/bin/env python3
import json
from collections import Counter

# Mapping from ASCII values to emoji names
emoji_map = {
    "42": "happy",
    "45": "neutral",
    "58": "sad"
}

def count_emojis(log_file_path):
    emoji_counts = Counter()
    
    # Read the log file
    with open(log_file_path, 'r') as file:
        for line in file:
            try:
                # Parse each line as JSON
                entry = json.loads(line)
                emoji_code = entry.get("emoji")
                # Map the emoji code to its name
                emoji_name = emoji_map.get(emoji_code, "unknown")
                # Count the occurrence
                emoji_counts[emoji_name] += 1
            except json.JSONDecodeError:
                continue

    return emoji_counts

# Example usage:
log_file_path = "/var/log/nginx/emoji_feedback.log"
emoji_counts = count_emojis(log_file_path)

# Display the results
print("Emoji Counts:")
for emoji, count in emoji_counts.items():
    print(f"{emoji}: {count}")

