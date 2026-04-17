import logging
import re
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from sqlalchemy import create_engine, Column, Integer, String, BigInteger, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# --- SETUP & DATABASE ---
Base = declarative_base()
engine = create_engine('sqlite:///bot.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"
    chat_id = Column(BigInteger, primary_key=True)
    username = Column(String)
    message_count = Column(Integer, default=0)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, ForeignKey("users.chat_id"))
    text = Column(String)
    is_from_bot = Column(Boolean, default=False)

Base.metadata.create_all(engine)
logging.basicConfig(level=logging.INFO)

# --- KEYWORD LOGIC ---
KEYWORDS = {
    r"hello|hi|hey": "👋 Hello there! How can I help you today?",
    r"help|support": "📖 You can use /start to see commands or just chat with me!",
    r"python|backend": "🐍 Python is the best! You're doing great in this bootcamp."
}

# --- HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Database: Save or Update User
    db_user = session.query(User).filter_by(chat_id=user.id).first()
    if not db_user:
        db_user = User(chat_id=user.id, username=user.username)
        session.add(db_user)
        session.commit()

    # Bonus: Inline Keyboard
    keyboard = [[InlineKeyboardButton("Visit Bootcamp", url="https://github.com/AmSmart")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"Welcome {user.first_name}! I'm your Bootcamp Bot(Camphelperbot1). I'm tracking our chat in my database.",
        reply_markup=reply_markup
    )

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.message.chat_id
    
    # Track stats
    db_user = session.query(User).filter_by(chat_id=chat_id).first()
    if db_user:
        db_user.message_count += 1
        session.commit()

    # Keyword Detection
    response = "I'm listening! (No keyword detected)"
    for pattern, reply in KEYWORDS.items():
        if re.search(pattern, text, re.IGNORECASE):
            response = reply
            break
            
    # Save Message to DB
    msg = Message(chat_id=chat_id, text=text, is_from_bot=False)
    session.add(msg)
    session.commit()

    await update.message.reply_text(response)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db_user = session.query(User).filter_by(chat_id=update.message.chat_id).first()
    count = db_user.message_count if db_user else 0
    await update.message.reply_text(f"📊 Your Stats:\nMessages sent: {count}")

if __name__ == '__main__':
    # Replace with your actual token
    TOKEN = "8604814138:AAFu0shAA9Yc2Lp1O5-hIo5pCTkifBI7UXA"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('stats', stats))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_msg))
    
    print("Bot is alive...")
    app.run_polling()

