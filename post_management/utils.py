import re
from django.utils.text import slugify

def generate_slug(text):
    text = slugify(text, allow_unicode=True)
    text = re.sub(r'[^\w\s\-\u0600-\u06FF\U0001F300-\U0001F6FF]', '', text)
    text = text.replace(' ', '-')
    text = re.sub(r'-+', '-', text)
    return text[:200]