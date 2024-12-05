from student import Student
from worker import Worker
quotes = [
    "Every man has his secret sorrows which the world knows not; and often times we call a man cold when he is only sad. – Henry Wadsworth Longfellow",
    "Although the world is full of suffering, it is also full of the overcoming of it. – Helen Keller",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "In the midst of winter, I found there was, within me, an invincible summer. – Albert Camus",
    "Fall seven times, stand up eight. – Japanese Proverb",
    "The human capacity for burden is like bamboo—far more flexible than you'd ever believe at first glance. – Jodi Picoult",
    "The best way to predict the future is to create it. – Peter Drucker",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama",
    "The most wasted of days is one without laughter. – E.E. Cummings"
]

therapy_links = [
    "https://www.betterhelp.com",
    "https://www.talkspace.com",
    "https://www.7cups.com",
    "https://www.online-therapy.com",
    "https://www.regain.us",
    "https://www.cerebral.com",
    "https://www.amwell.com",
    "https://www.therapyforblackgirls.com",
    "https://www.pridecounseling.com",
    "https://www.ginger.com"
]

print("Hello and welcome to my application")
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
status = input("Are you a student or a worker? ")
if status == 'student':
    college = input("Enter your college: ")
    major = input("Enter your major: ")
    person = Student(fname, lname, age, college, major)
else:
    company = input("Enter your company: ")
    position = input("Enter your position: ")
    person = Worker(fname, lname, age, company, position)

feeling = int(input("How are you feeling today? (1-10)"))
person.set_feeling(feeling)
print(quotes[feeling - 1])

if feeling < 6:
    print(therapy_links[feeling-1])
    person.set_link(therapy_links[feeling-1])


if person.feeling:
    feeling = person.feeling

if person.link:
    link = person.link
else:
    link = 'You are feeling great today!'
sentence = f"Quote: {quotes[feeling - 1]}, Link: {link}"

with open("data.txt", "a") as f:
    f.write(f"{person.get_all()} {sentence} \n")