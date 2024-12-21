# @B11_demo_bot
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from keyboards import kb

bot = Bot(token='', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я расскажу тебе о своём любимом фильме.\n'
                         'Набери "/film".')


@dp.message_handler(commands=['film'])
async def process_film(message: types.Message):
    button = types.InlineKeyboardButton(text='Смотреть', url="https://vk.com/video-161546275_456239444")
    kb3 = InlineKeyboardMarkup(row_width=1)
    kb3.add(button)
    await message.answer('Он называется "Телепорт".', reply_markup=kb3)
    await message.answer('Немного о фильме: (Нажимай на кнопки😄)', reply_markup=kb)


@dp.message_handler(text='Аннотация')
async def annotation(message: types.Message):
    await message.answer('Подросток из неблагополучного района Дэвид Райс '
                         'всегда считал себя обычным парнем, пока однажды он не узнал, '
                         'что он может телепортироваться с места на место. Новые способности '
                         'открыли перед ним весь мир. Он может побывать в Нью-Йорке и Токио, '
                         'посетить античные развалины в Риме, увидеть «крышу мира» с горы Эверест, '
                         'увидеть 20 рассветов и 20 закатов. И все - в один день. Теперь ему не нужны '
                         'деньги - он может взять сколько хочет. Однако в один момент он обнаруживает, '
                         'что стал мишенью. На него, как и на других подобных ему, объявлена охота. '
                         'На протяжении тысячи лет тайное общество стремится уничтожить их. '
                         'Вскоре Дэвид узнает истинную ценность его новых способностей.')


@dp.message_handler(text='Обложка')
async def cover(message: types.Message):
    await message.answer_photo(photo='https://www.film.ru/sites/default/files/movies/posters/1626992-2244764.jpeg')


@dp.message_handler(text='Актёры')
async def cast(message: types.Message):
    await message.answer('Хейден Кристенсен\nДжейми Белл\nРэйчел Билсон\nДайан Лэйн\nСэмюэл Л.Джексон')


@dp.message_handler(text='Год выпуска')
async def year(message: types.Message):
    await message.answer('2008')


@dp.message_handler(text='Жанр')
async def genre(message: types.Message):
    await message.answer('Фантастика, боевик, приключения')


@dp.message_handler(text='Не интересует')
async def not_interesting(message: types.Message):
    await message.answer('Очень жаль☹')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
