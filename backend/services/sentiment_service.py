def detect_sentiment(message):

    angry_words = [
        "ridiculous",
        "angry",
        "frustrated",
        "worst",
        "terrible",
        "hate",
        "disappointed",
        "useless"
    ]

    message = message.lower()

    for word in angry_words:
        if word in message:
            return "angry"

    return "normal"