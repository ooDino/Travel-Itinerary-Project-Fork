from openai import OpenAI
client = OpenAI()
import time

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Leaving from NYC on December 21th, 2023, arriving to Seoul, South Korea on December 23rd. Staying there until January 19th, 2024. Minimum I want to spend 5k, maximum I want to spend 10k."
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id="asst_sVJuzKcKffsYYLjauR72zIML"
)

time.sleep(60)

run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

print(thread.id)

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

print(messages)
