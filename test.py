
from TextPrompt import TextPrompt

p = TextPrompt(
    label="Enter your name",
    placeholder="Name",
)

v = p.prompt()

print(v) # Output: Name