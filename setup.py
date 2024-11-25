from setuptools import setup, find_packages

setup(
    name="MT",  # اسم المكتبة
    version="0.2",  # الإصدار
    packages=find_packages(),
    install_requires=[  # المكتبات التي تعتمد عليها المكتبة
        "requests",
        "amino.py",
        "amino",
        "numpy",
        "pillow",
        "samino",
        "pyfiglet",
        "gamino",
        "sys",
        "aminofix",
        "aminofixfix",
        "Thread",
        "threading",
        "os",
        "system",
        "websocket",
        "ZAminofix",
        "json",
        "time",
        "hashlib",
        "hmac",
        "base64",
        "uuid4",
        "uuid",
        "rainbowtext",
        "amino",
        "amino.py",
        "pymino",
        "edamino",
        "AminoLightPy",
        "bs",
        "bs4",
    ],
    author="MUSTAFA",
    author_email="your_email@example.com",
    description="Amino Client Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/MT",  # رابط لمستودع GitHub الخاص بك
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # الحد الأدنى من نسخة بايثون المطلوبة
)