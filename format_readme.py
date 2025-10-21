from py_markdown_table.markdown_table import markdown_table
import os

data = """\
# deep-ml  
Problem solved in www.deep-ml.com

"""

table = []

problems = os.listdir("problems")
for problem in problems:
    problem_path = os.path.join("problems", problem)
    problem_name = problem.split(".")[0]
    with open(problem_path, "r") as f:
        problem_data = f.readline()
        url = f.readline().strip()
        table.append(
            {
                "problem_id": int(problem_name),
                "problem_url": f"[🔗]({url})",
                "solution": f"[./problems/{problem}](./problems/{problem})",
            }
        )

table = sorted(table, key=lambda x: x["problem_id"])

data += markdown_table(table).set_params(row_sep="markdown", newline_char="  \n").get_markdown().strip("```")

with open("README.md", "w") as f:
    f.write(data)
