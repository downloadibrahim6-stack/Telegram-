from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Apne bot ka token yahan config section mein add karein
BOT_TOKEN = "8677878265:AAFJ2GMXaDerzMzaR6dzgwk-fhDslWvxTa0"

def get_banti_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Buy Now", callback_data="buy_now", style="danger")],
        [InlineKeyboardButton(text="🔄 Check Update", callback_data="check_update", style="success"),
        [InlineKeyboardButton(text="➕ Add Balance", callback_data="add_balance", style="primary")
        [InlineKeyboardButton(text="👤 My Profile + All History", callback_data="profile", style="success")
        [InlineKeyboardButton(text="💸 Refer And Earn", callback_data="refer", style="success"),
        [InlineKeyboardButton(text="💡 How To Use Bot", callback_data="tutorial", style="success")
        [InlineKeyboardButton(text="🛠 Support", callback_data="menu_support", style="danger")] 
        [InlineKeyboardButton(text="🎁 Daily Gift", callback_data="gift", style="success")
    ])
    return keyboard
    @dp.callback_query_handler(text="buy_now")
async def buy_now_callback(call: types.CallbackQuery):
 await call.message.answer("यहाँ आपके प्रोडक्ट का नाम है!")
        @dp.callback_query_handler(text="check_update")
async def check_update_callback(call: types.CallbackQuery):
    await call.message.answer("https://t.me/Sahilbhaiallupdate")
         import qrcode
from io import BytesIO

@dp.callback_query_handler(text="add_balance")
async def add_balance_callback(call: types.CallbackQuery):
    upi_id = "7318748360@fam"
    qr = qrcode.make(f"upi://pay?pa={upi_id}")
    bio = BytesIO()
    qr.save(bio, "PNG")
    bio.seek(0)
    await call.message.answer_photo(bio, caption="7318748360@fam")
         
