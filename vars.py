import os
from os import environ

# API Configuration
API_ID = int(os.environ.get("API_ID", "21834860"))
API_HASH = os.environ.get("API_HASH", "e4acef545ba34ee3fa5c511b38644647")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8207919935:AAG8261WoodTuUz4ICyE1rmzV0k694HR1lc")

CREDIT = os.environ.get("CREDIT", "💫『 𝒟𝒾𝓋𝓎𝒶𝓃𝓈𝒽 𝓈𝒽𝓊𝓀𝓁𝒶 』💫")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "divyanshshukla5375_db_user")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://divyanshshukla5375_db_user:1kZ2dsVTktdMljpr@cluster0.lo5qk5v.mongodb.net/?appName=Cluster0")
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "8056097370"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]  # Default to owner ID

# Channel Configuration
PREMIUM_CHANNEL = "https://t.me/+Tpbm-cGRcf5mZDY9"
# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://ibb.co/PGBvqbGK").split()))

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin @ItsUGBot to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}

