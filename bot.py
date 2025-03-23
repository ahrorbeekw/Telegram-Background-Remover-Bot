import asyncio

from aiogram import Bot, Dispatcher, html, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from rembg import remove
import asyncio
import requests
import time
from PIL import Image
TOKEN = "bot tokeni"

Bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Rasm kiriting orqa fonini olib tashlayman")

@dp.message(F.photo)
async def comman(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    size = photo.file_size
    width = photo.width
    h = photo.height
    
    file = await Bot.get_file(file_id=file_id)
    file_path = file.file_path
    url = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'
    
    vaqt = time.time()
    name = f'{message.from_user.id}_{vaqt}.png'
    input_path = requests.get(url=url , stream=True).raw
    output_path = name
    input1 = Image.open(input_path)
    output = remove(input1)
    output.save(output_path)
    rasm = types.input_file.FSInputFile(name)
    await message.answer_photo(photo=rasm)

async def main() -> None:
    await dp.start_polling(Bot)
if __name__ == '__main__':
    asyncio.run(main())

#pip install  rembg
