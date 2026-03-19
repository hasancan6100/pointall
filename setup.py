from setuptools import setup, find_packages

setup(
    name="phone-data-collector",
    version="0.1.0",
    description="Pydroid için telefon verisi toplama kütüphanesi",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot>=20.0",
        "aiofiles>=23.0"
    ],
    python_requires=">=3.6",
)
