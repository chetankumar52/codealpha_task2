```python
# FAQ Chatbot

def chatbot():

    print("🤖 Welcome to FAQ Chatbot!")
    print("Type 'bye' to exit.\n")

    faq = {
        "college timing": "College timing is 9 AM to 4 PM.",
        "admission": "Admission is based on the eligibility criteria.",
        "courses": "We offer B.Tech, BCA and MCA courses.",
        "fees": "Please contact the college office for the latest fee details.",
        "library": "The library is open from 9 AM to 5 PM.",
        "contact": "You can contact the college office for more information."
    }

    while True:

        question = input("You: ").lower().strip()

        if question == "bye":
            print("Bot: Goodbye! 👋")
            break

        found = False

        for keyword in faq:

            if keyword in question:
                print("Bot:", faq[keyword])
                found = True
                break

        if not found:
            print("Bot: Sorry, I don't know the answer to that question.")


chatbot()
```
