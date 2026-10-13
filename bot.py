from keep_alive import keep_alive
keep_alive()

import os
from io import BytesIO
from PIL import Image
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN", "8710865748:AAGyaCVN5kN8e83lQg2_m0xMb05JDaP7-rY")

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "📁 *File Converter Bot*\n\n"
        "Mujhe koi bhi **Photo / Image** bhejo, main use convert kar dunga:\n"
        "• Image ➔ **PDF Document**\n"
        "• Image ➔ **PNG Format**\n"
        "• Image ➔ **JPG Format**\n\n"
        "_Bas koi bhi photo send karo aur option choose karo!_"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

# Handle Photo / Document
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1] if update.message.photo else None
    
    if not photo and update.message.document:
        if update.message.document.mime_type.startswith("image/"):
            photo = update.message.document
        else:
            await update.message.reply_text("❌ Kripya sirf image/photo bhejein.")
            return

    # File download karke context mein save karna
    file = await context.bot.get_file(photo.file_id)
    file_bytes = await file.download_as_bytearray()
    
    # User data mein temporarily save
    context.user_data['image_bytes'] = file_bytes

    keyboard = [
        [InlineKeyboardButton("📄 Convert to PDF", callback_data="conv_pdf")],
        [
            InlineKeyboardButton("🖼️ Convert to PNG", callback_data="conv_png"),
            InlineKeyboardButton("🌄 Convert to JPG", callback_data="conv_jpg")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Photo receive ho gayi! Kis format mein convert karna hai?", reply_markup=reply_markup)

# Conversion Handler
async def convert_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if 'image_bytes' not in context.user_data:
        await query.edit_message_text("❌ File expire ho chuki hai, kripya dobara photo bhejein.")
        return

    action = query.data
    raw_data = context.user_data['image_bytes']
    img = Image.open(BytesIO(raw_data)).convert('RGB')
    output_io = BytesIO()

    await query.edit_message_text("⏳ Processing... File convert ho rahi hai...")

    if action == "conv_pdf":
        img.save(output_io, format='PDF')
        output_io.seek(0)
        await context.bot.send_document(
            chat_id=query.message.chat_id,
            document=output_io,
            filename="converted_file.pdf",
            caption="✅ *Aapki PDF File ready hai!*",
            parse_mode="Markdown"
        )

    elif action == "conv_png":
        img.save(output_io, format='PNG')
        output_io.seek(0)
        await context.bot.send_document(
            chat_id=query.message.chat_id,
            document=output_io,
            filename="converted_file.png",
            caption="✅ *PNG format ready hai!*",
            parse_mode="Markdown"
        )

    elif action == "conv_jpg":
        img.save(output_io, format='JPEG')
        output_io.seek(0)
        await context.bot.send_document(
            chat_id=query.message.chat_id,
            document=output_io,
            filename="converted_file.jpg",
            caption="✅ *JPG format ready hai!*",
            parse_mode="Markdown"
        )

    await query.message.delete()

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.IMAGE, handle_photo))
    app.add_handler(CallbackQueryHandler(convert_file, pattern="^conv_"))

    print("Converter bot live...")
    app.run_polling()
