#!/Users/markgrover/Desktop/Automate_task/venv/bin/python3.5

# Add Bullets to text pasted to clipboard

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for line in range(len(lines)):
    lines[line] = '# | ' + lines[line]

text = '\n'.join(lines)
pyperclip.copy(text)
print("            +--------------------------+              \n"
      "            |                          |              \n"
      "            |~~~~~~~~~~~~~~~~~~~~~~~~~~|              \n"
      "            |                          |              \n"
      "            |     PYTHON ROCKS BABY    |              \n"
      "            |~~~~~~~~~~~~~~~~~~~~~~~~~~|              \n"
      "            |       +-----------+      |              \n"
      "            |       |COMMENTIZED|      |              \n"
      "            +-------+-----------+------+               ")
