import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Cấu hình ghi log (không bắt buộc, nhưng giúp gỡ lỗi)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Thay thế bằng mã token của bạn
BOT_TOKEN = '7174414575:AAEapQ55TOycYd4UdRQtoa7B603u6ozxOfU'

# Định nghĩa các hàm xử lý lệnh
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Chào bạn! Tôi là bot của bạn.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Xin lỗi, tôi không hiểu lệnh đó.")

# Hàm chính để chạy bot
if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Thêm các trình xử lý
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)

    # Bắt đầu bot
    application.run_polling()
