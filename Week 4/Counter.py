text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

def word_frequency(text):
    text = text.lower()
    cleaned = ""
    for ch in text:
        if ch.isalpha() or ch == " " or ch == "\n":
            cleaned = cleaned + ch
        else:
            cleaned = cleaned + " "

    words = cleaned.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    sorted_words = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    return sorted_words[:3]

top_words = word_frequency(text)
print("Top 3 words:")
for word, count in top_words:
    print(f"{word} — {count} times")