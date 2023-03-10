
from decouple import config
import openai

openai.api_key = config("OPENAI_API_KEY")
import asyncio


def get_message(message):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=message.text,
      temperature=0.5,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
    )

    return response['choices'][0]['text']


# async def download_photo(photo_count, limit):
#     while photo_count < limit:
#         await asyncio.sleep(5)
#         photo_count += 1
#         print(f"Photo {photo_count}...")
#
#
# async def download_video(video_count, limit):
#     while video_count < limit:
#         await asyncio.sleep(1)
#         video_count += 1
#         print(f"video {video_count}...")
#
#
# async def main():
#     photo_count = 0
#     video_count = 0
#
#     task_list = [
#         download_photo(photo_count, 10),
#         download_video(video_count, 5)
#     ]
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())

# async def download_photo(photo_count):
#     await asyncio.sleep(1)
#     print(f"Photo {photo_count}...")
#
#
# async def main():
#     limit = int(input("Enter amount: "))
#     current_photo = 0
#     task_list = []
#
#     while current_photo < limit:
#         current_photo += 1
#         task = asyncio.create_task(download_photo(current_photo))
#         task_list.append(task)
#
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())