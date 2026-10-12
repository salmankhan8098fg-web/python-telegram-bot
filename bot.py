from keep_alive import keep_alive
keep_alive()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Apna BotFather ka token yahan paste karein
TOKEN = "8710865748:AAGyaCVN5kN8e83lQg2_m0xMb05JDaP7-rY"

# All Brands, Models aur Playstyle ka Data
SENSITIVITY_DATABASE = {
    "apple": {
        "name": "🍎 Apple (iPhone)",
        "models": {
            "iphone_base": {
                "name": "iPhone 11 / 12 / 13 / 14 (60Hz)",
                "gyro": {
                    "code": "7238-4921-8392-1049-201",
                    "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 295%\n• Gyro 4X: 235%\n• ADS Red Dot: 50%"
                },
                "nongyro": {
                    "code": "7238-4921-8392-1049-202",
                    "details": "• ADS Red Dot: 60%\n• ADS 3X: 33%\n• ADS 4X: 24%\n• Gyroscope: OFF"
                }
            },
            "iphone_pro": {
                "name": "iPhone 13 Pro / 14 Pro / 15 Pro (120Hz)",
                "gyro": {
                    "code": "7238-4921-8392-1049-203",
                    "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 280%\n• Gyro 4X: 215%\n• ProMotion smooth response"
                },
                "nongyro": {
                    "code": "7238-4921-8392-1049-204",
                    "details": "• ADS Red Dot: 55%\n• ADS 3X: 30%\n• ADS 4X: 21%\n• Gyroscope: OFF"
                }
            }
        }
    },
    "iqoo": {
        "name": "⚡ iQOO",
        "models": {
            "iqoo_neo": {
                "name": "iQOO Neo 7 / Neo 9 Pro / 12",
                "gyro": {
                    "code": "7190-6211-4820-9102-311",
                    "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 310%\n• Gyro 4X: 230%\n• Instant touch sampling settings"
                },
                "nongyro": {
                    "code": "7190-6211-4820-9102-312",
                    "details": "• ADS Red Dot: 62%\n• ADS 3X: 34%\n• ADS 4X: 23%\n• Gyroscope: OFF"
                }
            },
            "iqoo_z": {
                "name": "iQOO Z7 / Z9 Series",
                "gyro": {
                    "code": "7190-6211-4820-9102-313",
                    "details": "• Gyro 3rd Person: 390%\n• Gyro Red Dot: 390%\n• Gyro 3X: 300%\n• Gyro 4X: 220%"
                },
                "nongyro": {
                    "code": "7190-6211-4820-9102-314",
                    "details": "• ADS Red Dot: 65%\n• ADS 3X: 35%\n• ADS 4X: 25%\n• Gyroscope: OFF"
                }
            }
        }
    },
    "oneplus": {
        "name": "🔴 OnePlus",
        "models": {
            "op_number": {
                "name": "OnePlus 11 / 12 / 12R",
                "gyro": {
                    "code": "7142-6581-9920-3411-501",
                    "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 285%\n• Gyro 4X: 210%"
                },
                "nongyro": {
                    "code": "7142-6581-9920-3411-502",
                    "details": "• ADS Red Dot: 58%\n• ADS 3X: 31%\n• ADS 4X: 22%\n• Gyroscope: OFF"
                }
            },
            "op_nord": {
                "name": "OnePlus Nord Series (CE / 3 / 4)",
                "gyro": {
                    "code": "7142-6581-9920-3411-503",
                    "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 305%\n• Gyro 4X: 225%"
                },
                "nongyro": {
                    "code": "7142-6581-9920-3411-504",
                    "details": "• ADS Red Dot: 63%\n• ADS 3X: 33%\n• ADS 4X: 24%\n• Gyroscope: OFF"
                }
            }
        }
    },
    "redmi": {
        "name": "📱 Redmi / Poco",
        "models": {
            "poco_x_f": {
                "name": "Poco X5 / X6 Pro / F5 / F6",
                "gyro": {
                    "code": "7310-8452-1109-7623-881",
                    "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 300%\n• Gyro 4X: 225%"
                },
                "nongyro": {
                    "code": "7310-8452-1109-7623-882",
                    "details": "• ADS Red Dot: 64%\n• ADS 3X: 35%\n• ADS 4X: 24%\n• Gyroscope: OFF"
                }
            },
            "redmi_note": {
                "name": "Redmi Note 11 / 12 / 13 Series",
                "gyro": {
                    "code": "7310-8452-1109-7623-883",
                    "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 310%\n• Gyro 4X: 235%"
                },
                "nongyro": {
                    "code": "7310-8452-1109-7623-884",
                    "details": "• ADS Red Dot: 66%\n• ADS 3X: 36%\n• ADS 4X: 26%\n• Gyroscope: OFF"
                }
            }
        }
    },
    "realme": {
        "name": "⚡ Realme",
        "models": {
            "realme_gt": {
                "name": "Realme GT Series (GT 2 / 6 / Neo)",
                "gyro": {
                    "code": "7189-3201-4478-9012-631",
                    "details": "• Gyro 3rd Person: 385%\n• Gyro Red Dot: 385%\n• Gyro 3X: 290%\n• Gyro 4X: 215%"
                },
                "nongyro": {
                    "code": "7189-3201-4478-9012-632",
                    "details": "• ADS Red Dot: 60%\n• ADS 3X: 32%\n• ADS 4X: 22%\n• Gyroscope: OFF"
                }
            },
            "realme_number": {
                "name": "Realme 10 / 11 / 12 / Narzo Series",
                "gyro": {
                    "code": "7189-3201-4478-9012-633",
                    "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"
                },
                "nongyro": {
                    "code": "7189-3201-4478-9012-634",
                    "details": "• ADS Red Dot: 65%\n• ADS 3X: 35%\n• ADS 4X: 25%\n• Gyroscope: OFF"
                }
            }
        }
    },
    "samsung": {
        "name": "🌌 Samsung",
        "models": {
            "galaxy_s": {
                "name": "Galaxy S21 / S22 / S23 / S24",
                "gyro": {
                    "code": "7201-9451-2209-1830-441",
                    "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 280%\n• Gyro 4X: 210%"
                },
                "nongyro": {
                    "code": "7201-9451-2209-1830-442",
                    "details": "• ADS Red Dot: 58%\n• ADS 3X: 31%\n• ADS 4X: 22%\n• Gyroscope: OFF"
                }
            },
            "galaxy_m_a": {
                "name": "Galaxy M / A / F Series",
                "gyro": {
                    "code": "7201-9451-2209-1830-443",
                    "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 310%\n• Gyro 4X: 235%"
                },
                "nongyro": {
                    "code": "7201-9451-2209-1830-444",
                    "details": "• ADS Red Dot: 65%\n• ADS 3X: 36%\n• ADS 4X: 26%\n• Gyroscope: OFF"
                }
            }
        }
    }
}

# Step 1: All Brands Menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    brand_keys = list(SENSITIVITY_DATABASE.keys())
    
    # 2 buttons per row
    for i in range(0, len(brand_keys), 2):
        row = [InlineKeyboardButton(SENSITIVITY_DATABASE[brand_keys[i]]["name"], callback_query_data=f"b_{brand_keys[i]}")]
        if i + 1 < len(brand_keys):
            row.append(InlineKeyboardButton(SENSITIVITY_DATABASE[brand_keys[i+1]]["name"], callback_query_data=f"b_{brand_keys[i+1]}"))
        keyboard.append(row)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "🎮 *BGMI All Device Sensitivity Bot*\n\nApne phone ka **Brand (Company)** select karein:"
    
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")

# Step 2: Selected Brand ke All Models
async def show_models(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    brand_key = query.data.split("_")[1]
    brand_data = SENSITIVITY_DATABASE[brand_key]
    
    keyboard = []
    for model_key, model_info in brand_data["models"].items():
        keyboard.append([InlineKeyboardButton(model_info["name"], callback_query_data=f"m_{brand_key}_{model_key}")])
        
    keyboard.append([InlineKeyboardButton("🔙 Brands Menu", callback_query_data="back_home")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"Selected: *{brand_data['name']}*\n\nAb apna phone **Model** chunein:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Step 3: Playstyle (Gyro vs Non-Gyro)
async def select_playstyle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    _, brand_key, model_key = query.data.split("_")
    model_name = SENSITIVITY_DATABASE[brand_key]["models"][model_key]["name"]
    
    keyboard = [
        [
            InlineKeyboardButton("🎯 Full Gyroscope", callback_query_data=f"res_{brand_key}_{model_key}_gyro"),
            InlineKeyboardButton("👆 Non-Gyro (Thumb)", callback_query_data=f"res_{brand_key}_{model_key}_nongyro")
        ],
        [InlineKeyboardButton("🔙 Change Model", callback_query_data=f"b_{brand_key}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"Device: *{model_name}*\n\nApna **Playstyle** select karein:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Step 4: Final Result (Code + Details)
async def show_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    _, brand_key, model_key, playstyle = query.data.split("_")
    model_data = SENSITIVITY_DATABASE[brand_key]["models"][model_key]
    style_data = model_data[playstyle]
    style_label = "Full Gyroscope" if playstyle == "gyro" else "Non-Gyro (Thumb)"
    
    keyboard = [
        [InlineKeyboardButton("🔙 Change Playstyle", callback_query_data=f"m_{brand_key}_{model_key}")],
        [InlineKeyboardButton("🏠 Main Menu", callback_query_data="back_home")]
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

# Back to Start Handler
async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(back_to_start, pattern="^back_home$"))
    app.add_handler(CallbackQueryHandler(show_models, pattern="^b_"))
    app.add_handler(CallbackQueryHandler(select_playstyle, pattern="^m_"))
    app.add_handler(CallbackQueryHandler(show_result, pattern="^res_"))
    
    print("All Devices Bot live...")
    app.run_polling()
