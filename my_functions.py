def y(c):
    return 842-c

def pol(sentence, cast):
    words = sentence.split()
    total_length = sum(len(word) for word in words) + len(words) - 1  # Include spaces
    half_length = total_length // 2
    current_length = 0
    for i, word in enumerate(words):
        current_length += len(word) + 1  # Add word length and a space
        if current_length >= half_length:
            part1 = ' '.join(words[:i + 1])
            part2 = ' '.join(words[i+ 1:])
            if cast == 1:
                return part1
            if cast == 2:
                return part2
    return sentence, ""  # Fallback if no split point is found
