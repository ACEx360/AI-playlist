# UserWarning: The shell tool has no safeguards by default. Use at your own risk.
# I care about my machine so further code will be in notebooks
from langchain_community.tools import ShellTool
shell_tool = ShellTool()
result = shell_tool.invoke("whoami")
print(f"{result}")