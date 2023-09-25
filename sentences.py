import re

product_review = '''This is a fine milk, but the product
  line appears to be limited in available colors. I
  could only find white.'''

def get_matches_for_pattern(pattern_object, items):
    return [item[0] for item in pattern_object.findall(items)]

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
sentences = get_matches_for_pattern(sentence_pattern, product_review)

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    words = get_matches_for_pattern(word_pattern, sentence)
    print(words)
