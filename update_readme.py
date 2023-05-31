#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

def generate_file_list():
    root_dir = '.'  # Set the root directory for the file list

    # List the files and directories in the root directory
    items = os.listdir(root_dir)

    # Sort the items alphabetically or based on your preferred order
    sorted_items = sorted(items)

    # Filter out directories and non-Markdown files
    files = [item for item in sorted_items if os.path.isfile(item) and item.endswith('.md')]

    # Generate the file list Markdown content
    file_list = "\n".join([f"- [{file}](./{file})" for file in files])

    return file_list

# Generate the file list
file_list_content = generate_file_list()

# Update the README.md file with the file list content
with open('README.md', 'w') as readme_file:
    readme_file.write(f"```{file_list_content}```\n")

