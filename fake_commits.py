import os
import random
from datetime import datetime, timedelta

start_date = datetime(2025, 10, 24)
end_date = datetime(2026, 2, 12)

# Use the absolute path for the workspace
repo_path = "/Users/aryanpatel/Desktop/YT_insights"

os.chdir(repo_path)

current_date = start_date

commit_count = 0

while current_date <= end_date:
    # randomly skip days (30% chance)
    if random.random() < 0.3:
        current_date += timedelta(days=random.choice([1,2,3]))
        continue

    commits_today = random.randint(1, 4)

    for _ in range(commits_today):
        commit_time = current_date + timedelta(
            hours=random.randint(9, 22),
            minutes=random.randint(0, 59)
        )

        date_str = commit_time.strftime("%Y-%m-%d %H:%M:%S")

        # make a small change
        with open("dummy.txt", "a") as f:
            f.write(f"commit {commit_count}\n")

        os.system("git add dummy.txt") # Changed this from git add . to prevent accidental commits of other files
        os.system(
            f'GIT_AUTHOR_DATE="{date_str}" GIT_COMMITTER_DATE="{date_str}" '
            f'git commit -m "update {commit_count}"'
        )

        commit_count += 1

    current_date += timedelta(days=1)

print("Done!")
