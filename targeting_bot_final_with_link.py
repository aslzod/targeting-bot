import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7948153588:AAGwfhKSa236q0qklUPGp8m-Rw8JyKsi1QI"
ADMIN_ID = 986867203
PAID_USERS_FILE = "paid_users.txt"

menu_buttons = [["🎬 Demo dars", "🎓 Kurs haqida"], ["💳 To‘lov", "📎 Chek yuborish"], ["🎓 To‘liq darslar"]]
markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)

def add_paid_user(user_id):
    with open(PAID_USERS_FILE, "a") as f:
        f.write(f"{user_id}\n")

def is_paid_user(user_id):
    if not os.path.exists(PAID_USERS_FILE):
        return False
    with open(PAID_USERS_FILE, "r") as f:
        return str(user_id) in f.read()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! 👋\nTargeting 0 dan PROgacha kursiga xush kelibsiz!",
        reply_markup=markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.from_user.id

    if text == "🎬 Demo dars":
        await update.message.reply_text(
            "Salom Snayperlar! 😊 Bugundan boshlab siz reklamani eng aniq nuqtasini nishonga olishni boshlaysiz! 🎯\n"
            "Shuning uchun snaypersiz!\n\n"
            "🎬 1-BEPUL darsni tomosha qiling!\n\n"
            "Ushbu dars orqali siz kurs formatini tushunasiz va o‘rganish qanday bo‘lishini his qilasiz.\n\n"
            "💡 Yoqqan bo‘lsa — 130.000 so‘m evaziga to‘liq 20 darsni oling!\n\n"
            "📺 Video darslar bu yerda: https://t.me/targetingbepul"
        )

    elif text == "🎓 Kurs haqida":
        await update.message.reply_text(
            "🟢 1-MODUL: \nAsosiy tayyorgarlik (Foundation Mode)\n\n"
            "Bu modulda siz raqamli reklama ishlarining asosiy vositalari bilan tanishasiz. Oddiy profilni professional marketing quroliga aylantirishni o‘rganasiz.\n\n"
            "• Facebook'da shaxsiy profil ochish\n"
            "• Instagram akkauntni biznes profilga aylantirish\n"
            "• Facebook sahifasini sozlash\n"
            "• Visa kartani ochish va reklama uchun tayyorlash\n"
            "• Facebook Business Manager va reklama account ochish\n\n"

            "🟠 2-MODUL: \nReklama asoslari va amaliy sozlash\n"
            "Bu yerda siz reklama platformasini 100% sozlab, reklama pulingizni yo‘qqa chiqarmaslikni o‘rganasiz.\n\n"
            "• Reklama accountga Visa cardni ulash\n"
            "• Shaxsiy ma’lumotlarni tasdiqlash — blokdan qochish\n"
            "• Reklama maqsadlari tahlili: Trafikmi? Sotuvmi? Ijtimoiy isbotmi?\n"
            "• ChatGPT yordamida reklama strategiyasini tezda tuzish\n\n"

            "🔵 3-MODUL: Reklama kampaniyalari — amaliyot bo‘yicha masterclass\n"
            "Endi har bir reklama turini misollar bilan, real kampaniya bilan yoqasiz!\n\n"
            "• Traffic maqsadida reklama yoqish (Saytga odam haydash)\n"
            "• Soobsheniya maqsadida reklama (DM portlashi uchun)\n"
            "• Obunachi ko‘paytirish: Profilni ko‘rishli qilish\n"
            "• Lid maqsadida reklama (Kontakt to‘plash)\n"
            "• Ko‘rishlar sonini oshirish — video postlar uchun\n"
            "• Postdan tashqari reklama yoqish (Dark post usuli)\n\n"

            "🔴 4-MODUL: Pro hacklar va kuchli manipulyatsiyalar\n"
            "Bu bo‘lim sizni oddiy foydalanuvchidan sistemani aldov darajasida biladigan reklama xakeriga aylantiradi.\n\n"
            "• Bir summaga ko‘p reklama yoqish (Duplicate bypass usuli)\n"
            "• Reklamaga soliq to‘lamaslik (Qo‘rqmasdan reklama qilish)\n"
            "• Telegram’da reklama yoqish va ulanish sistemasi\n"
            "• Raqobatchilarni tahlil qilish (Spy usullari va yaratish)\n"
            "• ChatGPT yordamida kreativ, text, strategiya, analiz qilish"
        )

    elif text == "💳 To‘lov":
        await update.message.reply_text(
            "💳 TO‘LOV QILISH:\n\n"
            "📌 Kurs narxi: 130 000 so‘m\n\n"
            "To‘lovni quyidagi kartaga amalga oshiring:\n\n"
            "💳 6262 5701 6010 6961\n"
            "👤 Mirsodiqov Bekzod\n\n"
            "✅ To‘lovdan so‘ng “📎 Chek yuborish” bo‘limi orqali chekingizni rasm sifatida yuboring."
        )

    elif text == "📎 Chek yuborish":
        await update.message.reply_text("📎 Iltimos, to‘lov chekini rasm sifatida shu yerga yuboring.")

    elif text == "🎓 To‘liq darslar":
        if is_paid_user(user_id):
            await update.message.reply_text("📚 Marhamat, bu yerda to‘liq kurs darslarini tomosha qilishingiz mumkin.")
        else:
            await update.message.reply_text("❌ Bu bo‘lim faqat to‘lov qilgan foydalanuvchilar uchun. Avval to‘lovni amalga oshiring va chekingizni yuboring.")

    else:
        await update.message.reply_text("❗️ Iltimos, tugmalardan birini tanlang yoki chekni yuboring.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    username = f"@{user.username}" if user.username else "Yo'q"
    full_name = user.full_name or "Noma’lum foydalanuvchi"
    user_id = user.id

    caption = (
        f"🧾 Yangi TO‘LOV CHEKI:\n\n"
        f"👤 Ismi: {full_name}\n"
        f"🔗 Username: {username}\n"
        f"🆔 ID: {user_id}\n\n"
        f"🕒 Yuborilgan vaqt: {update.message.date.strftime('%Y-%m-%d %H:%M')}"
    )

    photo = update.message.photo[-1]
    await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo.file_id, caption=caption)
    await update.message.reply_text("✅ Chekingiz muvaffaqiyatli yuborildi!\nTez orada admin siz bilan bog‘lanadi.")
    add_paid_user(user_id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot ishga tushdi!")
app.run_polling()
