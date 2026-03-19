"""
Pydroid için izin yönetimi modülü
"""
import os
import android  # Pydroid'de android modülü var

class PermissionManager:
    def __init__(self):
        self.droid = android.Android()
        self.permissions_granted = False
    
    def request_storage_permission(self):
        """Depolama izni iste"""
        try:
            # Pydroid için izin iste
            self.droid.activities.startActivityForResult(
                'android.intent.action.ACTION_OPEN_DOCUMENT_TREE',
                None,
                None
            )
            
            # Depolama erişim kontrolü
            result = self.droid.checkSelfPermission(
                'android.permission.READ_EXTERNAL_STORAGE'
            )
            
            if result.result:
                print("Depolama izni verildi")
                return True
            else:
                print("Depolama izni gerekli!")
                return False
                
        except Exception as e:
            print(f"İzin hatası: {e}")
            return False
    
    def check_permissions(self):
        """Tüm izinleri kontrol et"""
        permissions = [
            'android.permission.READ_EXTERNAL_STORAGE',
            'android.permission.WRITE_EXTERNAL_STORAGE',
            'android.permission.INTERNET'
        ]
        
        for perm in permissions:
            result = self.droid.checkSelfPermission(perm)
            if not result.result:
                print(f"İzin gerekli: {perm}")
                return False
        
        return True
