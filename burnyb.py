import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TOKEN")  # Il token lo salviamo come variabile su Render

# Messaggio di benvenuto
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍️ Catalogo", callback_data="catalogo")],
        [InlineKeyboardButton("🛒 Carrello", callback_data="carrello")],
        [InlineKeyboardButton("📦 Mio ordine", callback_data="mioordine")],
        [InlineKeyboardButton("ℹ️ Aiuto", callback_data="aiuto")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🔥 Yo! Sono BurnyB, il tuo amico per lo shopping 🔥\n"
        "È l’ora di sfornare insieme un drip bollente 👟👕✨\n\n"
        "Con me puoi:\n"
        "🛍️ Sfogliare il catalogo\n"
        "🛒 Gestire il carrello\n"
        "📦 Seguire lo stato del tuo ordine\n"
        "💳 Info su pagamenti e spedizioni\n\n"
        "Usa i bottoni qui sotto per iniziare!",
        reply_markup=reply_markup
    )

# Callback dei bottoni
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "catalogo":
        await query.edit_message_text("🛍️ Catalogo in arrivo 🔥 (qui metteremo i prodotti)")
    elif query.data == "carrello":
        await query.edit_message_text("🛒 Il tuo carrello è ancora vuoto 🔥")
    elif query.data == "mioordine":
        await query.edit_message_text("📦 Nessun ordine attivo al momento 😎")
    elif query.data == "aiuto":
        await query.edit_message_text(
            "ℹ️ Sono qui per aiutarti! 🔥\n\n"
            "🛍️ /catalogo – Sfoglia i prodotti\n"
            "🛒 /carrello – Controlla il carrello\n"
            "📦 /mioordine – Stato dell’ordine\n"
            "💳 Info su pagamenti e spedizioni"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🔥 BurnyB è online su Render!")
    app.run_polling()

if __name__ == "__main__":
    main()
