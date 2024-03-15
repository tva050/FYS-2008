import re

# Open the file for reading
with open('c:/Users/trym7/OneDrive - UiT Office 365/skole/FYS-2008/Home Exam/prob3f_freq_domain.txt', 'r') as file:
    content = file.readlines()

# Remove leading and trailing whitespace characters from each line
content = [re.sub(r'^\s+|\s+$', '', line) for line in content]

# Open the file for writing and write the modified content
with open('c:/Users/trym7/OneDrive - UiT Office 365/skole/FYS-2008/Home Exam/prob3f_freq_domain.txt', 'w') as file:
    file.writelines('\n'.join(content))