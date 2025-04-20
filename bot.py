# ---- bot.py ----
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN   = "7653889834:AAFO67iaWwtHGPSeyRdnTdu3EozBBq12Zw8"
FORM_URL    = "https://forms.gle/yD77G7ZPn3rXipwk6"

# /start コマンド
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello！We are POP KOL Bot.")

# /signup コマンド
async def signup(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📝 Click here for registration form：\n{FORM_URL}")

# Bot を動かす
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start",  start))
    app.add_handler(CommandHandler("signup", signup))
    print("Bot started... Ctrl+C で停止")
    app.run_polling()       # ← *超* 簡単な“ポーリング”方式

if __name__ == "__main__":
    main()

    # bot.py に追記
FORM_URL = "https://forms.gle/yD77G7ZPn3rXipwk6"  # ← ここだけ差し替え

async def signup(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📝 Creator registration form is here 👇.\n{FORM_URL}"
    )

app.add_handler(CommandHandler("signup", signup))

