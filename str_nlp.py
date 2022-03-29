def remove_emoji (string):
    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F""]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)     