import re
html = input("Enter HTML: ")
titles = re.findall(r'<h[1-3]>(.*?)</h[1-3]>', html, re.I)
word_count = {}
for title in titles:
    words = re.findall(r'\b\w+\b', title.lower())
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
ranked = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("\nRanked Words:")
for word, count in ranked:
    print(word, ":", count)