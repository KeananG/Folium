#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

# Get the current working directory as the root directory
root_directory = os.getcwd()

# Generate the directory tree
directory_tree = ''
for root, dirs, files in os.walk(root_directory):
    level = root.replace(root_directory, '').count(os.sep)
    indent = '    ' * (level - 1)
    directory_tree += f'{indent}├── {os.path.basename(root)}\n'
    sub_indent = '    ' * level
    for file in files:
        directory_tree += f'{sub_indent}├── {file}\n'

# Update the README.md file
readme_file = os.path.join(root_directory, 'README.md')
with open(readme_file, 'r') as file:
    readme_content = file.read()

updated_readme_content = readme_content.replace('```directory_structure```', directory_tree)

with open(readme_file, 'w') as file:
    file.write(updated_readme_content)

print('README.md file updated successfully.')

