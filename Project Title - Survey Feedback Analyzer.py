# ============================================
# Survey Feedback Analyzer
# ============================================

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


more_feedbacks = int(input("How many more feedbacks do you want to add? "))

for i in range(more_feedbacks):

    print("\nEnter feedback", i + 1)

    name = input("Enter Name: ")
    feedback = input("Enter Feedback: ")

    # Validate rating
    while True:
        rating = int(input("Enter Rating (1-5): "))

        if 1 <= rating <= 5:
            break
        else:
            print("Rating must be between 1 and 5.")

    # Automatically generate serial number
    s_no = len(feedback_data['S_No']) + 1

    # Append data
    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    # Remove extra spaces and leading/trailing spaces
    text = ' '.join(text.split())

    # Update cleaned feedback
    feedback_data['Feedback'][i] = text

def count_word_in_feedbacks(word):

    count = 0

    word = word.lower()

    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        if word in words:
            count += 1

    return count


# Print word count insights

print("\n========== WORD COUNT INSIGHTS ==========")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))

print("\n========== FINAL CLEANED DATA ==========")

print(feedback_data)

total_rating = sum(feedback_data['Rating'])

number_of_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / number_of_feedbacks

print("\nAverage Rating:", round(average_rating, 2))

longest_feedback = ""
longest_word_count = 0
longest_name = ""

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    word_count = len(feedback.split())

    if word_count > longest_word_count:

        longest_word_count = word_count
        longest_feedback = feedback
        longest_name = feedback_data['Name'][i]

print("Name:", longest_name)
print("Feedback:", longest_feedback)
print("Word Count:", longest_word_count)


unique_words = []

for feedback in feedback_data['Feedback']:
    words = feedback.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

print(unique_words)

combined_data = list(zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
))

sorted_data = sorted(
    combined_data,
    key=lambda x: x[3],
    reverse=True
)

for item in sorted_data:

    print(
        "S_No:", item[0],
        "| Name:", item[1],
        "| Feedback:", item[2],
        "| Rating:", item[3]
    )