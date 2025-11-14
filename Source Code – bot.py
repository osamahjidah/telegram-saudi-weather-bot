import os
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TELEGRAM_TOKEN = os.environ.get("BOT_TOKEN")
OPENWEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

SAUDI_CITIES = [
    "الرياض", "جدة", "الدمام", "مكة", "المدينة المنورة", "الخبر",
    "تبوك", "بريدة", "خميس مشيط", "حائل", "نجران",
    "الهفوف", "الجبيل", "الطائف", "أبها", "جيزان"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = (
        "مرحبًا بك! الرجاء اختيار اسم مدينة سعودية للحصول على حالة الطقس الحالية.\n"
        "المدن المتاحة:"
    )
    keyboard = [[city] for city in SAUDI_CITIES]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(welcome_msg, reply_markup=reply_markup)

async def get_weather(city):
    city_map = {
        "الرياض": "Riyadh", "جدة": "Jeddah", "الدمام": "Dammam", "مكة": "Mecca",
        "المدينة المنورة": "Medina", "الخبر": "Khobar", "تبوك": "Tabuk", "بريدة": "Buraidah",
        "خميس مشيط": "Khamis Mushait", "حائل": "Hail", "نجران": "Najran",
        "الهفوف": "Al Hofuf", "الجبيل": "Al Jubail", "الطائف": "Taif",
        "أبها": "Abha", "جيزان": "Jizan"
    }

    if city not in city_map:
        return "المدينة غير معروفة أو غير مدرجة. الرجاء اختيار مدينة سعودية من القائمة."

    city_en = city_map[city]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_en},SA&appid={OPENWEATHER_API_KEY}&units=metric&lang=ar"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return "تعذر الحصول على بيانات الطقس لهذه المدينة."

    name = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].capitalize()
    return f"الطقس في {city}:\nدرجة الحرارة: {temp}°C\nالحالة: {desc}"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text.strip()
    weather = await get_weather(city)
    await update.message.reply_text(weather)

if __name__ == "__main__":
    if not TELEGRAM_TOKEN or not OPENWEATHER_API_KEY:
        raise ValueError("BOT_TOKEN أو WEATHER_API_KEY غير موجود. تأكد من إضافتهما في إعدادات Heroku (config vars).")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
