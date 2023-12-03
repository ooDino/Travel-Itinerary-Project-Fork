from openai import OpenAI
import requests
client = OpenAI()
import time
import os

def travel_itinerary_creation(starting_location, destination_location, departing_date, returning_date, min_amt, max_amt):

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content= f"Leaving from {starting_location} on {departing_date}, arriving to {destination_location} on {destination_location}, Staying there until {returning_date}. Minimum I want to spend {min_amt}, maximum I want to spend {max_amt}."    
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_sVJuzKcKffsYYLjauR72zIML"
    )

    while run.status !="completed":
        time.sleep(5)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    return messages.data[0].content[0].text.value
    
# print(travel_itinerary_creation('NYC', 'Seoul, South Korea', '12/21/2023', '1/19/2024', '5000', '10000'))

# sample output:
# in_progress
# in_progress
# in_progress
# in_progress
# in_progress
# in_progress
# completed
# **Day: Thu, 12/21/2023**
# Plan:
# - Arrive at Incheon International Airport.
# - Check in at the hotel, rest and acclimatize.
# - Evening walk around Cheonggyecheon Stream for light sightseeing.
# - Dinner at Myeongdong Kyoja for traditional Korean cuisine.

# **Day: Fri, 12/22/2023**
# Plan:
# - 9:00 AM – Gyeongbokgung Palace and National Folk Museum of Korea.
# - 12:00 PM – Lunch at Tosokchon for their famous samgyetang.
# - 2:00 PM – Bukchon Hanok Village.
# - 5:00 PM – Namsan Seoul Tower before sunset for views of the city.
# - 8:00 PM – Dinner in Itaewon at a restaurant of your choice.

# **Day: Sat, 12/23/2023**
# Plan:
# - 10:00 AM – Shopping and exploring in Hongdae.
# - 1:00 PM – Lunch at any popular street food vendor.
# - 3:00 PM – Trickeye Museum or enjoy local street performances.
# - 6:00 PM – Visit Dongdaemun Design Plaza and nearby shopping centers.
# - 9:00 PM – Dinner at a Dongdaemun eatery.

# **Day: Sun, 12/24/2023**
# Plan:
# - 9:00 AM – Hike Bukhansan National Park.
# - 2:00 PM – Have a picnic lunch in the park with pre-packed food.
# - 6:00 PM – Return and rest.
# - 8:00 PM – Special Christmas Eve Dinner at a high-end restaurant (advance reservation recommended).

# **Day: Mon, 12/25/2023**
# Plan:
# - 10:00 AM – Visit the War Memorial of Korea.
# - 1:00 PM – Lunch in Gangnam at Sutbul Mapo Galbi.
# - 3:00 PM – Explore COEX Mall and the surrounding area.
# - 6:00 PM – SMTOWN for K-pop fans or a relaxing time at Bongeunsa Temple.
# - 8:30 PM – Dinner at Jungsik (advance reservation required) for a modern take on Korean dishes.

# **Day: Tue, 12/26/2023 – Sun, 12/31/2023**
# Plan:
# - Use these days to explore neighborhoods like Insadong, explore the Lotte World Adventure, visit art galleries in Samcheong-dong, and try various Korean BBQ places.
# - Take day trips to places like the DMZ, Suwon's Hwaseong Fortress, and Nami Island. 
# - Enjoy local cafes, bakeries, and take part in any seasonal festivals or events.

# **Day: Mon, 1/1/2024**
# Plan:
# - 11:00 AM – New Year's Day late start; enjoy a leisurely brunch in a Gangnam café.
# - 1:00 PM – Take a leisurely walk in Olympic Park.
# - 4:00 PM – Visit the Seoul National Cemetery.
# - 7:30 PM – Dinner at a local restaurant with traditional New Year's food.

# **Day: Tue, 1/2/2024 – Thu, 1/18/2024**
# Plan:
# - During this extended period, continue to visit museums, palaces, and other cultural sites at your own pace. 
# - Consider taking longer day trips or even overnight trips to cities like Busan, Jeonju, or Gyeongju.
# - Experience Korean spa culture by visiting a jjimjilbang.
# - As you near the end of your stay, revisit favorite neighborhoods or explore new ones like Yeouido or Seongsu-dong.
# - Try to catch performances such as non-verbal shows like NANTA or Korean Traditional Performances at the National Theater of Korea.

# **Day: Fri, 1/19/2024**
# Plan:
# - Pack and check out of the hotel.
# - Depending on flight time, grab a last stroll or meal in Seoul.
# - Departure from Incheon International Airport. 

# **Note:**
# - Reservations for restaurants and attractions are highly recommended where possible.
# - This itinerary intentionally leaves some days less structured for relaxation and impromptu activities.
# - Please adjust activities based on personal interests, seasonal events, and opening times of attractions.