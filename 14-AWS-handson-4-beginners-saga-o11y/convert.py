import sys

filepath = "/Users/tetsuya/Documents/src/handson-manual/14-AWS-handson-4-beginners-saga-o11y/14-AWS-handson-4-beginners-saga-o11y.md"

with open(filepath, 'r') as f:
    text = f.read()

lines = text.split('\n')
new_lines = []
in_note_block = False

for line in lines:
    if line.startswith("> [!NOTE]") or line.startswith("> [!TIP]"):
        in_note_block = True
        new_lines.append("Positive")
    elif line.startswith("> [!WARNING]"):
        in_note_block = True
        new_lines.append("Negative")
    elif in_note_block:
        if line.startswith(">"):
            content = line[1:]
            if content.startswith(" "):
                content = content[1:]
            new_lines.append(f": {content}" if content else ":")
        else:
            in_note_block = False
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(filepath, 'w') as f:
    f.write('\n'.join(new_lines))
