import os

# Directory containing the source files
src_dir = "problems"

# Initialize the README content
readme_content = """# AtCoder Practice

This folder contains my solutions to AtCoder problems using Python to solve.

## Solved Problems (Total: {total_solved})
| # | Problem | Solution |
|---|---------|----------|
"""

# List all files in the src directory
table_rows = []
for filename in sorted(os.listdir(src_dir)):
    if filename.endswith(".py"):
        # Extract contest and problem name
        contest, problem = filename.split("_", 1)
        problem = problem.replace(".py", "")
        title_name = contest + "_" + problem

        # Format the table row
        row = f"| {title_name} | [Description](https://atcoder.jp/contests/{contest}/tasks) | [Solution]({src_dir}/{filename}) |\n"

        table_rows.append(((contest, problem), row))

# Sort the table rows by contest and problem name and add them to the README content
table_rows.sort(key=lambda x: x[0])
total_solved = len(table_rows)
readme_content = readme_content.format(total_solved=total_solved)
for _, row in table_rows:
    readme_content += row

# Write the content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
