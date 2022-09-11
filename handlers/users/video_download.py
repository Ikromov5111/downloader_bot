import os

from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from utils.misc.Instagramdownloader import instagramdownloader
from utils.misc.tiktokdownload import tiktokDownload

from pytube import YouTube
video = None

@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def insta_download(message: types.Message):
    try:
        link = message.text
        data = instagramdownloader(link=link)
        if data == 'Bad':
            await message.answer("Bu url manzil orqali hech narsa topolmadik")
        elif data['type'] == 'image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'carousel':
            for media in data['media']:
                await message.answer_document(document=media)

        else:
            await message.answer("Bu url manzil orqali hech narsa topolmadik")

    except:
        await message.answer("Bu url manzil orqali hech narsa topolmadik")



@dp.message_handler(Text(contains='tiktok', ignore_case=True))
async def tiktok_download(message: types.Message):
    link= message.text
    data = tiktokDownload(link=link)

    try:
        if data == "Bad":
            await message.answer('Bu url manzil orqali hech narsa topolmadik')
        else:
            await message.answer_video(video=data['video'])
    except:
        await message.answer('Bu url manzil orqali hech narsa topolmadik')
    # await message.answer('Bu url manzil orqali hech narsa topolmadik')





@dp.message_handler(Text(startswith='http'))
async def download(message: types.Message):
    link = message.text
    url = YouTube(link)

    try:
        if url.check_availability() is None:

            await message.answer('video yuklanmoqda...')
            video_f = url.streams.get_lowest_resolution().download(filename='name.mp4')
            filename = url.title
            await message.answer_video(video=open('name.mp4', 'rb'), supports_streaming=True, caption=f'{url.title}')

            os.remove('name.mp4')

        else:
            await message.answer("xatolik")
    except:
        await message.answer('Bu url manzil orqali hech narsa topolmadik')

# link = 'https://youtu.be/lRfu2vj3l3g'
# url = YouTube(link)
# buffer=BytesIO()
# url.streams.get_lowest_resolution().stream_to_buffer(buffer=buffer)
# print()