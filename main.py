import asyncio
import logging
import sys
from aiogram.types import Message, FSInputFile

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import wikipedia
wikipedia.set_lang("uz")
import qrcode
import base64
TOKEN =("8809466266:AAGRfkX8dpRDiu88fqH1zAHmOddJehNcmXA")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text)
async def get_text_all(message: Message):
    matn = message.text
    if "wikipedia: " in matn:
        natija_text = matn[11:]
        wiki_text = wikipedia.summary(natija_text)
        wiki_text_limit = wiki_text[:100]
        await message.answer(wiki_text_limit)
    elif "qrcode: " in matn:
        matn_img = matn[7:]
        img = qrcode.make(matn_img)
        type(img)
        img_text = "qrcode.png"
        img.save(img_text)
        rasm = FSInputFile(img_text)
        await message.answer_photo(photo=rasm)
    elif "qr: " in matn:
        matn_url = matn[3:]
        qrcode.make(matn_url).save('https://i.pinimg.com/736x/bd/ad/98/bdad9876dd5cef97a60ecfcb0a89e960.jpg').save('hostedprcode.png')
        rasm_qr = FSInputFile("hostedqrcode.png")
        await message.answer_photo(photo=rasm_qr)




async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())