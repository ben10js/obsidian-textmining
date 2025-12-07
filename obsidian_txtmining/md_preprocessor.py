import re

def preprocess_markdown(text):
    # Remove YAML front matter
    text = re.sub(r'---\n(.*?)\n---', '', text, flags=re.DOTALL)
    # Remove images and links
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    # Remove formatting (*, **, _, __, ~~)
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
    text = re.sub(r'~~(.*?)~~', r'\1', text)
    # Remove headers, blockquotes, lists, numbered lists
    text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*>\s.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*[-*+]\s', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s', '', text, flags=re.MULTILINE)
    # Remove code blocks, inline code
    text = re.sub(r'``````', '', text, flags=re.DOTALL)
    text = re.sub(r'`(.*?)`', r'\1', text)
    # Remove horizontal rules
    text = re.sub(r'^-{3,}\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\*{3,}\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^={3,}\s*$', '', text, flags=re.MULTILINE)
    # Remove tables
    text = re.sub(r'^\|.*\|.*$', '', text, flags=re.MULTILINE)
    # Remove footnotes
    text = re.sub(r'\[\^.+?\](?::\s*.*)?', '', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Reduce multiple newlines to single newline
    text = re.sub(r'\n\s*\n', '\n', text)
    return text

