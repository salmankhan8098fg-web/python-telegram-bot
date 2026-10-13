from keep_alive import keep_alive
keep_alive()

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN", "8710865748:AAGyaCVN5kN8e83lQg2_m0xMb05JDaP7-rY")

SENSITIVITY_DATABASE = {
    "apple": {
        "name": "🍎 Apple (iPhone)",
        "models": {
            "ip11_12": {
                "name": "iPhone 11 / 12",
                "gyro": {"code": "7238-4921-8392-1049-201", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 295%\n• Gyro 4X: 235%\n• ADS Red Dot: 50%"},
                "nongyro": {"code": "7238-4921-8392-1049-202", "details": "• ADS Red Dot: 60%\n• ADS 3X: 33%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            },
            "ip13_14": {
                "name": "iPhone 13 / 14 / 15",
                "gyro": {"code": "7238-4921-8392-1049-203", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 395%\n• Gyro 3X: 290%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7238-4921-8392-1049-204", "details": "• ADS Red Dot: 58%\n• ADS 3X: 32%\n• ADS 4X: 23%\n• Gyroscope: OFF"}
            },
            "ip_pro": {
                "name": "iPhone Pro / Pro Max",
                "gyro": {"code": "7238-4921-8392-1049-205", "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 275%\n• Gyro 4X: 215%"},
                "nongyro": {"code": "7238-4921-8392-1049-206", "details": "• ADS Red Dot: 54%\n• ADS 3X: 29%\n• ADS 4X: 20%\n• Gyroscope: OFF"}
            }
        }
    },
    "iqoo": {
        "name": "⚡ iQOO",
        "models": {
            "iqoo11_12": {
                "name": "iQOO 11 / 12",
                "gyro": {"code": "7190-6211-4820-9102-301", "details": "• Gyro 3rd Person: 390%\n• Gyro Red Dot: 390%\n• Gyro 3X: 290%\n• Gyro 4X: 215%"},
                "nongyro": {"code": "7190-6211-4820-9102-302", "details": "• ADS Red Dot: 59%\n• ADS 3X: 32%\n• ADS 4X: 22%\n• Gyroscope: OFF"}
            },
            "iqoo_neo": {
                "name": "iQOO Neo 6 / 7 / 9 Pro",
                "gyro": {"code": "7190-6211-4820-9102-303", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 310%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7190-6211-4820-9102-304", "details": "• ADS Red Dot: 62%\n• ADS 3X: 34%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            },
            "iqoo_z": {
                "name": "iQOO Z6 / Z7 / Z9 Series",
                "gyro": {"code": "7190-6211-4820-9102-305", "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 300%\n• Gyro 4X: 225%"},
                "nongyro": {"code": "7190-6211-4820-9102-306", "details": "• ADS Red Dot: 65%\n• ADS 3X: 35%\n• ADS 4X: 25%\n• Gyroscope: OFF"}
            }
        }
    },
    "oneplus": {
        "name": "🔴 OnePlus",
        "models": {
            "op_flagship": {
                "name": "OnePlus 10 / 11 / 12 / 12R",
                "gyro": {"code": "7142-6581-9920-3411-501", "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 285%\n• Gyro 4X: 210%"},
                "nongyro": {"code": "7142-6581-9920-3411-502", "details": "• ADS Red Dot: 58%\n• ADS 3X: 31%\n• ADS 4X: 22%\n• Gyroscope: OFF"}
            },
            "op_nord": {
                "name": "OnePlus Nord Series",
                "gyro": {"code": "7142-6581-9920-3411-503", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 305%\n• Gyro 4X: 225%"},
                "nongyro": {"code": "7142-6581-9920-3411-504", "details": "• ADS Red Dot: 63%\n• ADS 3X: 33%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            }
        }
    },
    "poco": {
        "name": "🟡 Poco",
        "models": {
            "poco_f": {
                "name": "Poco F4 / F5 / F6",
                "gyro": {"code": "7310-8452-1109-7623-881", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 295%\n• Gyro 4X: 220%"},
                "nongyro": {"code": "7310-8452-1109-7623-882", "details": "• ADS Red Dot: 61%\n• ADS 3X: 33%\n• ADS 4X: 23%\n• Gyroscope: OFF"}
            },
            "poco_x": {
                "name": "Poco X4 / X5 / X6 Pro",
                "gyro": {"code": "7310-8452-1109-7623-883", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 310%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7310-8452-1109-7623-884", "details": "• ADS Red Dot: 64%\n• ADS 3X: 35%\n• ADS 4X: 25%\n• Gyroscope: OFF"}
            }
        }
    },
    "redmi": {
        "name": "📱 Redmi",
        "models": {
            "redmi_notepro": {
                "name": "Redmi Note 12 / 13 Pro",
                "gyro": {"code": "7310-8452-1109-7623-891", "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7310-8452-1109-7623-892", "details": "• ADS Red Dot: 63%\n• ADS 3X: 34%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            },
            "redmi_note": {
                "name": "Redmi Note 11 / 12 Base",
                "gyro": {"code": "7310-8452-1109-7623-893", "details": "• Gyro 3rd Person: 390%\n• Gyro Red Dot: 390%\n• Gyro 3X: 300%\n• Gyro 4X: 225%"},
                "nongyro": {"code": "7310-8452-1109-7623-894", "details": "• ADS Red Dot: 66%\n• ADS 3X: 36%\n• ADS 4X: 26%\n• Gyroscope: OFF"}
            }
        }
    },
    "realme": {
        "name": "⚡ Realme",
        "models": {
            "realme_gt": {
                "name": "Realme GT Series",
                "gyro": {"code": "7189-3201-4478-9012-631", "details": "• Gyro 3rd Person: 385%\n• Gyro Red Dot: 385%\n• Gyro 3X: 290%\n• Gyro 4X: 215%"},
                "nongyro": {"code": "7189-3201-4478-9012-632", "details": "• ADS Red Dot: 60%\n• ADS 3X: 32%\n• ADS 4X: 22%\n• Gyroscope: OFF"}
            },
            "realme_num": {
                "name": "Realme 11 / 12 / Narzo",
                "gyro": {"code": "7189-3201-4478-9012-633", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7189-3201-4478-9012-634", "details": "• ADS Red Dot: 64%\n• ADS 3X: 34%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            }
        }
    },
    "samsung": {
        "name": "🌌 Samsung",
        "models": {
            "galaxy_s": {
                "name": "Galaxy S21 / S22 / S23 / S24",
                "gyro": {"code": "7201-9451-2209-1830-441", "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 280%\n• Gyro 4X: 210%"},
                "nongyro": {"code": "7201-9451-2209-1830-442", "details": "• ADS Red Dot: 58%\n• ADS 3X: 31%\n• ADS 4X: 22%\n• Gyroscope: OFF"}
            },
            "galaxy_a_m": {
                "name": "Galaxy A / M Series",
                "gyro": {"code": "7201-9451-2209-1830-443", "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7201-9451-2209-1830-444", "details": "• ADS Red Dot: 64%\n• ADS 3X: 35%\n• ADS 4X: 25%\n• Gyroscope: OFF"}
            }
        }
    },
    "vivo": {
        "name": "💎 Vivo",
        "models": {
            "vivo_x": {
                "name": "Vivo X Series (Flagship)",
                "gyro": {"code": "7150-1092-8823-3401-711", "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 285%\n• Gyro 4X: 215%"},
                "nongyro": {"code": "7150-1092-8823-3401-712", "details": "• ADS Red Dot: 59%\n• ADS 3X: 32%\n• ADS 4X: 23%\n• Gyroscope: OFF"}
            },
            "vivo_t_v": {
                "name": "Vivo T / V Series",
                "gyro": {"code": "7150-1092-8823-3401-713", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7150-1092-8823-3401-714", "details": "• ADS Red Dot: 64%\n• ADS 3X: 35%\n• ADS 4X: 25%\n• Gyroscope: OFF"}
            }
        }
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    brand_keys = list(SENSITIVITY_DATABASE.keys())
    
    for i in range(0, len(brand_keys), 2):
        row = [InlineKeyboardButton(SENSITIVITY_DATABASE[brand_keys[i]]["name"], callback_data=f"b:{brand_keys[i]}")]
        if i + 1 < len(brand_keys):
            row.append(InlineKeyboardButton(SENSITIVITY_DATABASE[brand_keys[i+1]]["name"], callback_data=f"b:{brand_keys[i+1]}"))
        keyboard.append(row)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "🎮 *BGMI All Device Sensitivity Bot*\n\nApne phone ka **Brand (Company)** chunein:"
    
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def show_models(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    brand_key = query.data.split(":")[1]
    brand_data = SENSITIVITY_DATABASE[brand_key]
    
    keyboard = []
    for model_key, model_info in brand_data["models"].items():
        keyboard.append([InlineKeyboardButton(model_info["name"], callback_data=f"m:{brand_key}:{model_key}")])
        
    keyboard.append([InlineKeyboardButton("🔙 Brands Menu", callback_data="back_home")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"Selected: *{brand_data['name']}*\n\nAb apna phone **Model** chunein:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def select_playstyle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    _, brand_key, model_key = query.data.split(":")
    model_name = SENSITIVITY_DATABASE[brand_key]["models"][model_key]["name"]
    
    keyboard = [
        [
            InlineKeyboardButton("🎯 Full Gyroscope", callback_data=f"res:{brand_key}:{model_key}:gyro"),
            InlineKeyboardButton("👆 Non-Gyro (Thumb)", callback_data=f"res:{brand_key}:{model_key}:nongyro")
        ],
        [InlineKeyboardButton("🔙 Change Model", callback_data=f"b:{brand_key}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"Device: *{model_name}*\n\nApna **Playstyle** chunein:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def show_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    _, brand_key, model_key, playstyle = query.data.split(":")
    model_data = SENSITIVITY_DATABASE[brand_key]["models"][model_key]
    style_data = model_data[playstyle]
    style_label = "Full Gyroscope" if playstyle == "gyro" else "Non-Gyro (Thumb)"
    
    keyboard = [
        [InlineKeyboardButton("🔙 Change Playstyle", callback_data=f"m:{brand_key}:{model_key}")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="back_home")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    response = (
        f"📱 *{model_data['name']}*\n"
        f"🎯 *Style:* {style_label}\n\n"
        f"📋 *Share Code:*\n`{style_data['code']}`\n\n"
        f"⚙️ *Key Settings:*\n{style_data['details']}\n\n"
        "_(Code copy karne ke liye uspar tap karein aur BGMI > Cloud Layout mein paste karein)_"
    )
    
    await query.edit_message_text(response, reply_markup=reply_markup, parse_mode="Markdown")

async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(back_to_start, pattern="^back_home$"))
    app.add_handler(CallbackQueryHandler(show_models, pattern="^b:"))
    app.add_handler(CallbackQueryHandler(select_playstyle, pattern="^m:"))
    app.add_handler(CallbackQueryHandler(show_result, pattern="^res:"))
    
    print("All Devices Bot live...")
    app.run_polling()
