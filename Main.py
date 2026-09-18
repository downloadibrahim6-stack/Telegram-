from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
import qrcode
from io import BytesIO

# Bot token can be added here in the config section
BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot)

def get_banti_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Buy Now", callback_data="buy_now", style="danger")],
        [InlineKeyboardButton(text="🔄 Check Update", callback_data="check_update")],
        [InlineKeyboardButton(text="➕ Add Balance", callback_data="add_balance", style="primary")],
        [InlineKeyboardButton(text="👤 My Profile + All History", callback_data="profile", style="success")],
        [InlineKeyboardButton(text="🗣️ Refer And Earn", callback_data="refer", style="success")],
        [InlineKeyboardButton(text="ℹ️ How To Use Bot", callback_data="tutorial", style="success")],
        [InlineKeyboardButton(text="🛠️ Support", callback_data="menu_support", style="danger")],
        [InlineKeyboardButton(text="🎁 Daily Gift", callback_data="gift", style="success")]
    ])
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: aiogram.types.Message):
    await message.answer("Welcome to the Bot!", reply_markup=get_banti_keyboard())

@dp.callback_query_handler(text="buy_now")
async def buy_now_callback(call: types.CallbackQuery):
    await call.message.answer("Here is your product name!")

@dp.callback_query_handler(text="check_update")
async def check_update_callback(call: types.CallbackQuery):
    await call.message.answer("https://t.me/Sahilbhaiallupdate")

@dp.callback_query_handler(text="add_balance")
async def add_balance_callback(call: types.CallbackQuery):
    upi_id = "7318748360@fam"
    qr = qrcode.make(f"upi://pay?pa={upi_id}")
    bio = BytesIO()
    qr.save(bio, "PNG")
    bio.seek(0)
    await call.message.answer_photo(bio, caption="Here is your QR code for adding balance.")

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
    
