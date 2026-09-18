import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BufferedInputFile
import qrcode
from io import BytesIO

BOT_TOKEN = "8677878265:..." # अपना बोट टोकन डालें 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_menu_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Product Store", callback_data="menu_shop")],
        [InlineKeyboardButton(text="👤 My Profile", callback_data="profile")],
        [InlineKeyboardButton(text="➕ Add Balance", callback_data="add_balance")],
        [InlineKeyboardButton(text="🛠️ Tutorials", callback_data="menu_how_to")],
        [InlineKeyboardButton(text="🛠️ Support", callback_data="menu_support")]
    ])
    return keyboard

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🏪SAHIL BHAI STORE🔓", reply_markup=main_menu_kb())

@dp.callback_query(F.data == "menu_shop")
async def shop_callback(callback: types.CallbackQuery):
    await callback.message.answer("Here is your product name!")
    await callback.answer()

@dp.callback_query(F.data == "add_balance")
async def add_balance_callback(callback: types.CallbackQuery):
    upi_id = "7318748360@fam"
    qr = qrcode.make(f"upi://pay?pa={upi_id}")
    bio = BytesIO()
    qr.save(bio, "PNG")
    bio.seek(0)
    await callback.message.answer_photo(
        BufferedInputFile(bio, filename="qr_code.png"),
        caption="Here is your QR code for adding balance."
    )
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    
