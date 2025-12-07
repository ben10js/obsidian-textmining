import os

def collect_md_files(vault_path):
    return [os.path.join(r, f)
            for r, _, files in os.walk(vault_path) for f in files if f.endswith('.md')]

