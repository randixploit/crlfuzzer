from setuptools import setup

setup(
    name="crlfuzzer",  # Nama tools Anda
    version="1.1.0",  # Versi tools Anda
    author="randiXploit",  # Nama penulis
    author_email="randixploit@gmail.com",  # Email penulis
    description="CRLF Vulnerability Fuzzer",  # Deskripsi singkat tools Anda
    url="https://github.com/randixploit/crlf-fuzzer",  # URL repositori Anda (jika ada)
    packages=["."],  # Menentukan paket yang ingin disertakan, di sini hanya direktori saat ini
    install_requires=[  # Paket yang diperlukan untuk menjalankan tools
        "requests", 
        "urllib3", 
        "colorama",
    ],
    entry_points={  # Menentukan command line entry point
        'console_scripts': [
            'crlfuzzer=main:main',  # crlf_fuzzer adalah nama file, dan main adalah fungsi utama
        ],
    },
    classifiers=[  # Klasifikasi tools Anda untuk memudahkan pencarian
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
