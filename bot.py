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
                "name": "iPhone 13/14/15 Pro Max (120Hz)",
                "gyro": {"code": "7238-4921-8392-1049-205", "details": "• Gyro 3rd Person: 380%\n• Gyro Red Dot: 380%\n• Gyro 3X: 275%\n• Gyro 4X: 215%\n• ProMotion smooth tracking"},
                "nongyro": {"code": "7238-4921-8392-1049-206", "details": "• ADS Red Dot: 54%\n• ADS 3X: 29%\n• ADS 4X: 20%\n• Gyroscope: OFF"}
            }
        }
    },
    "iqoo": {
        "name": "⚡ iQOO",
        "models": {
            "iqoo11_12": {
                "name": "iQOO 11 / 12 (Flagship)",
                "gyro": {"code": "7190-6211-4820-9102-301", "details": "• Gyro 3rd Person: 390%\n• Gyro Red Dot: 390%\n• Gyro 3X: 290%\n• Gyro 4X: 215%"},
                "nongyro": {"code": "7190-6211-4820-9102-302", "details": "• ADS Red Dot: 59%\n• ADS 3X: 32%\n• ADS 4X: 22%\n• Gyroscope: OFF"}
            },
            "iqoo_neo": {
                "name": "iQOO Neo 6 / 7 / 7 Pro / 9 Pro",
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
                "name": "OnePlus Nord CE 3 / 4 / Nord 3",
                "gyro": {"code": "7142-6581-9920-3411-503", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 305%\n• Gyro 4X: 225%"},
                "nongyro": {"code": "7142-6581-9920-3411-504", "details": "• ADS Red Dot: 63%\n• ADS 3X: 33%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            },
            "op_old": {
                "name": "OnePlus 7 / 8 / 9 Series",
                "gyro": {"code": "7142-6581-9920-3411-505", "details": "• Gyro 3rd Person: 390%\n• Gyro Red Dot: 390%\n• Gyro 3X: 295%\n• Gyro 4X: 220%"},
                "nongyro": {"code": "7142-6581-9920-3411-506", "details": "• ADS Red Dot: 60%\n• ADS 3X: 32%\n• ADS 4X: 23%\n• Gyroscope: OFF"}
            }
        }
    },
    "poco": {
        "name": "🟡 Poco",
        "models": {
            "poco_f": {
                "name": "Poco F4 / F5 / F6 Series",
                "gyro": {"code": "7310-8452-1109-7623-881", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 295%\n• Gyro 4X: 220%"},
                "nongyro": {"code": "7310-8452-1109-7623-882", "details": "• ADS Red Dot: 61%\n• ADS 3X: 33%\n• ADS 4X: 23%\n• Gyroscope: OFF"}
            },
            "poco_x": {
                "name": "Poco X3 / X4 / X5 / X6 Pro",
                "gyro": {"code": "7310-8452-1109-7623-883", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 310%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7310-8452-1109-7623-884", "details": "• ADS Red Dot: 64%\n• ADS 3X: 35%\n• ADS 4X: 25%\n• Gyroscope: OFF"}
            },
            "poco_m": {
                "name": "Poco M4 / M5 / M6 Series",
                "gyro": {"code": "7310-8452-1109-7623-885", "details": "• Gyro 3rd Person: 390%\n• Gyro Red Dot: 390%\n• Gyro 3X: 295%\n• Gyro 4X: 225%"},
                "nongyro": {"code": "7310-8452-1109-7623-886", "details": "• ADS Red Dot: 67%\n• ADS 3X: 37%\n• ADS 4X: 27%\n• Gyroscope: OFF"}
            }
        }
    },
    "redmi": {
        "name": "📱 Redmi",
        "models": {
            "redmi_notepro": {
                "name": "Redmi Note 12 / 13 Pro / Pro+",
                "gyro": {"code": "7310-8452-1109-7623-891", "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7310-8452-1109-7623-892", "details": "• ADS Red Dot: 63%\n• ADS 3X: 34%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            },
            "redmi_note": {
                "name": "Redmi Note 10 / 11 / 12 Base",
                "gyro": {"code": "7310-8452-1109-7623-893", "details": "• Gyro 3rd Person: 390%\n• Gyro Red Dot: 390%\n• Gyro 3X: 300%\n• Gyro 4X: 225%"},
                "nongyro": {"code": "7310-8452-1109-7623-894", "details": "• ADS Red Dot: 66%\n• ADS 3X: 36%\n• ADS 4X: 26%\n• Gyroscope: OFF"}
            },
            "redmi_k": {
                "name": "Redmi K50i / K20 Pro",
                "gyro": {"code": "7310-8452-1109-7623-895", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 290%\n• Gyro 4X: 215%"},
                "nongyro": {"code": "7310-8452-1109-7623-896", "details": "• ADS Red Dot: 60%\n• ADS 3X: 32%\n• ADS 4X: 22%\n• Gyroscope: OFF"}
            }
        }
    },
    "realme": {
        "name": "⚡ Realme",
        "models": {
            "realme_gt": {
                "name": "Realme GT 2 / GT 6 / Neo",
                "gyro": {"code": "7189-3201-4478-9012-631", "details": "• Gyro 3rd Person: 385%\n• Gyro Red Dot: 385%\n• Gyro 3X: 290%\n• Gyro 4X: 215%"},
                "nongyro": {"code": "7189-3201-4478-9012-632", "details": "• ADS Red Dot: 60%\n• ADS 3X: 32%\n• ADS 4X: 22%\n• Gyroscope: OFF"}
            },
            "realme_num": {
                "name": "Realme 11 / 12 / 13 Pro Series",
                "gyro": {"code": "7189-3201-4478-9012-633", "details": "• Gyro 3rd Person: 400%\n• Gyro Red Dot: 400%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7189-3201-4478-9012-634", "details": "• ADS Red Dot: 64%\n• ADS 3X: 34%\n• ADS 4X: 24%\n• Gyroscope: OFF"}
            },
            "realme_narzo": {
                "name": "Realme Narzo 60 / 70 Series",
                "gyro": {"code": "7189-3201-4478-9012-635", "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 300%\n• Gyro 4X: 225%"},
                "nongyro": {"code": "7189-3201-4478-9012-636", "details": "• ADS Red Dot: 66%\n• ADS 3X: 36%\n• ADS 4X: 26%\n• Gyroscope: OFF"}
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
            "galaxy_a": {
                "name": "Galaxy A34 / A35 / A54 / A55",
                "gyro": {"code": "7201-9451-2209-1830-443", "details": "• Gyro 3rd Person: 395%\n• Gyro Red Dot: 395%\n• Gyro 3X: 305%\n• Gyro 4X: 230%"},
                "nongyro": {"code": "7201-9451
