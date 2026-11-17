train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


def count_moods(data):
    happy = 0
    sad = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy += 1
        elif mood == "Sad":
            sad += 1

    return happy, sad


# ---------------- LEVEL 2: GUESS THE MOOD ----------------

happy_words = [
    "full", "won", "surprise", "tasty", "excited",
    "selected", "learned", "favourite", "medal", "great"
]

sad_words = [
    "lost", "failed", "moving", "cancelled", "missed",
    "upset", "stopped", "lonely", "late", "exam"
]


def clean_sentence(sentence):
    words = sentence.lower().split()
    cleaned_words = []

    for word in words:
        new_word = ""

        for char in word:
            if char.isalnum():
                new_word += char

        if new_word:
            cleaned_words.append(new_word)

    return cleaned_words


def guess_mood(sentence):
    words = clean_sentence(sentence)

    happy_count = 0
    sad_count = 0

    for word in words:
        if word in happy_words:
            happy_count += 1

        if word in sad_words:
            sad_count += 1

    # If there is a tie, choose Sad.
    if happy_count > sad_count:
        return "Happy"
    else:
        return "Sad"


# ---------------- LEVEL 3: ACCURACY ----------------

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]


def calculate_accuracy(data):
    correct = 0

    for sentence, actual_mood in data:
        predicted_mood = guess_mood(sentence)

        if predicted_mood == actual_mood:
            correct += 1

    accuracy = (correct / len(data)) * 100
    return accuracy


# ---------------- MAIN PROGRAM ----------------

print("MOOD GUESSER")
print("Happy and Sad Sentence Detector")

print("\nLevel 1 - Training Data Count:")
print(count_moods(train_data))

print("\nLevel 2 - Enter Your Sentence:")
user_sentence = input("Type a sentence: ")

print("Predicted Mood:", guess_mood(user_sentence))

print("\nLevel 3 - Model Accuracy:")
print("Accuracy:", calculate_accuracy(practice_data), "%")
rain
