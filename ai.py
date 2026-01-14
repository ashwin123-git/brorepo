import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Chat memory
messages = [
    {"role": "system", "content": "You are Jarvis, a friendly and playful AI assistant."}
]

def completion(user_message):
    messages.append({"role": "user", "content": user_message})

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages
    )

    bot_reply = response.output_text

    messages.append({"role": "assistant", "content": bot_reply})
    print("Jarvis:", bot_reply)


if __name__ == "__main__":
    print("🤖 Hi, I am Jarvis. How may I help you?")

    while True:
        user_question = input("You: ")

        if user_question.lower() == "bye":
            print("Jarvis: Goodbye, sir 😌")
            break

        completion(user_question)
