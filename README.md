<div align="center">

# 📧 Gmail Reader Bot with Python

### 🤖 ربات خواندن و مدیریت ایمیل Gmail با Python و IMAP

<p>
  <a href="#-راهنمای-فارسی">
    <img src="https://img.shields.io/badge/🇮🇷_راهنمای_فارسی-Click-blue?style=for-the-badge" alt="راهنمای فارسی">
  </a>


<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gmail-IMAP-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  <img src="https://img.shields.io/badge/Dependencies-Zero-success?style=for-the-badge" alt="Dependencies">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p>
  <b>📥 دریافت ایمیل</b> •
  <b>📖 خواندن ایمیل</b> •
  <b>🔤 پشتیبانی فارسی</b> •
  <b>🔐 IMAP Secure</b>
</p>

</div>

---

<a name="-راهنمای-فارسی"></a>

# 🇮🇷 راهنمای فارسی

## 📌 معرفی پروژه

**Gmail Reader Bot** یک ابزار سبک، سریع و کاربردی ساخته‌شده با Python است که با استفاده از پروتکل **IMAP** به حساب Gmail متصل می‌شود و امکان دریافت، خواندن، پردازش و مدیریت ایمیل‌ها را فراهم می‌کند.

این پروژه برای ساخت ابزارهای اتوماسیون، ربات‌های ایمیلی و پروژه‌های هوش مصنوعی بسیار مناسب است.

یکی از مهم‌ترین ویژگی‌های پروژه این است که برای عملکرد اصلی خود به هیچ کتابخانه خارجی نیاز ندارد و از کتابخانه‌های استاندارد Python استفاده می‌کند.

---

## 🌟 امکانات پروژه

* 📥 دریافت ایمیل‌های Gmail
* 📬 خواندن ایمیل‌های Inbox
* 🔎 امکان جستجوی ایمیل‌ها
* 📖 دریافت ایمیل‌های خوانده‌نشده
* ✅ تغییر وضعیت ایمیل به `Seen`
* 🇮🇷 پشتیبانی از زبان فارسی
* 🌍 پشتیبانی از Unicode و UTF-8
* 😀 پشتیبانی از Emoji
* 📧 دریافت Subject
* 👤 دریافت Sender
* 📅 دریافت Date
* 📝 استخراج متن ایمیل
* 🔐 اتصال امن به Gmail
* ⚡ سبک و سریع
* 🚫 بدون نیاز به نصب Package خارجی
* 🐍 ساخته‌شده کاملاً با Python

---

# 🧠 نحوه کار پروژه

فرآیند کلی پروژه به شکل زیر است:

```text
                ┌─────────────────────┐
                │    Gmail Account    │
                └──────────┬──────────┘
                           │
                           │ IMAP / SSL
                           ▼
                ┌─────────────────────┐
                │    Python Bot       │
                │      imaplib        │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Search Emails     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Fetch Messages    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Decode Content    │
                │       email         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Process Email Data  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Mark as Seen     │
                └─────────────────────┘
```

---

# ⚙️ پیش‌نیازها

برای اجرای پروژه به موارد زیر نیاز دارید:

### Python

نسخه Python:

```text
Python 3.8+
```

بررسی نسخه Python:

```bash
python --version
```

یا:

```bash
python3 --version
```

---

## 📦 کتابخانه‌های استفاده‌شده

پروژه از کتابخانه‌های داخلی Python استفاده می‌کند:

```text
imaplib
email
```

بنابراین برای اجرای نسخه اصلی پروژه نیازی به اجرای:

```bash
pip install
```

ندارید.

---

# 🔐 ساخت Gmail App Password

برای اتصال امن برنامه به Gmail باید از **App Password** استفاده کنید.

> ⚠️ رمز اصلی Gmail خود را داخل برنامه قرار ندهید.

---

## 1️⃣ فعال کردن Two-Step Verification

وارد تنظیمات امنیت حساب Google شوید:

**Google Account → Security**

سپس:

```text
2-Step Verification
```

را فعال کنید.

---

## 2️⃣ ساخت App Password

بعد از فعال کردن تأیید دومرحله‌ای، وارد صفحه App Password شوید.

می‌توانید عبارت زیر را در Google جستجو کنید:

```text
Google App Passwords
```

سپس یک نام برای برنامه انتخاب کنید، مثلاً:

```text
Gmail Reader Bot
```

و روی:

```text
Create
```

کلیک کنید.

Google یک App Password اختصاصی برای شما ایجاد می‌کند.

---

## 3️⃣ استفاده از App Password

رمز ایجادشده را به عنوان Password برنامه استفاده کنید.

ساختار کلی:

```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
```

---

# 📧 Gmail IMAP Settings

تنظیمات Gmail برای IMAP:

```text
IMAP Server: imap.gmail.com
Port: 993
Security: SSL
```

در Python:

```python
imaplib.IMAP4_SSL("imap.gmail.com", 993)
```

---

# 🚀 نصب و اجرای پروژه

## 1. Clone کردن Repository

```bash
git clone https://github.com/shervinaitechwebdeveloper-boop/gmailreader.git
```

---

## 2. ورود به پوشه پروژه

```bash
cd gmailreader
```

---

## 3. اجرای برنامه

اگر فایل اصلی پروژه `main.py` باشد:

```bash
python main.py
```

در Linux یا macOS:

```bash
python3 main.py
```

> اگر نام فایل اصلی پروژه متفاوت است، نام فایل Python خود را جایگزین `main.py` کنید.

---

# 📂 ساختار پیشنهادی پروژه

```text
gmailreader/
│
├── main.py
├── README.md
├── .gitignore
└── LICENSE
```

---

# 📖 اطلاعاتی که می‌توان از Email دریافت کرد

برنامه می‌تواند اطلاعات مختلفی از ایمیل استخراج کند:

```text
📧 Sender
📝 Subject
📅 Date
📄 Body
📨 Message ID
📎 Attachments
```

همچنین ایمیل‌هایی که دارای متن فارسی باشند نیز قابل پردازش هستند.

مثال:

```text
سلام شروین 👋

این یک ایمیل آزمایشی است.

🚀 Gmail Reader Bot
```

---

# 🌍 پشتیبانی از فارسی و Unicode

یکی از قابلیت‌های مهم پروژه، پشتیبانی از Encodingهای مختلف ایمیل است.

برای مثال:

```text
سلام دنیا 🌍
ربات هوشمند ایمیل 🤖
هوش مصنوعی 🚀
```

همچنین زبان‌های مختلف:

```text
🇮🇷 فارسی
🇬🇧 English
🇩🇪 Deutsch
🇫🇷 Français
🇯🇵 日本語
🇰🇷 한국어
🇸🇦 العربية
```

قابل پردازش هستند.

---

# 📖 Read و Unread

Gmail برای ایمیل‌ها وضعیت‌هایی مانند `Seen` و `Unseen` دارد.

ایمیل خوانده‌نشده:

```text
UNSEEN
```

پس از پردازش:

```text
SEEN
```

ربات می‌تواند پس از دریافت و پردازش ایمیل، وضعیت آن را به `Seen` تغییر دهد.

---

# 🔒 امنیت

اطلاعات ورود Gmail بسیار حساس هستند.

### ❌ هرگز این کار را انجام ندهید:

```python
EMAIL = "example@gmail.com"
PASSWORD = "my-real-password"
```

### ❌ App Password را در GitHub قرار ندهید.

اگر اطلاعات حساس را داخل فایل جداگانه قرار می‌دهید، آن فایل را در `.gitignore` قرار دهید.

مثلاً:

```text
.env
config.py
secrets.py
credentials.json
```

---

# 🛡️ فایل `.gitignore`

نمونه:

```gitignore
__pycache__/
*.pyc

.env
.env.*
config.py
secrets.py
credentials.json
```

---

# ⚠️ اگر App Password لو رفت

اگر App Password را به اشتباه در GitHub منتشر کردید:

1. فوراً آن App Password را حذف کنید.
2. یک App Password جدید بسازید.
3. رمز قبلی را دیگر استفاده نکنید.
4. GitHub Repository و Commit History را بررسی کنید.

---

# 🧪 Workflow

فرآیند اجرای برنامه:

```text
Start
  │
  ▼
Connect to Gmail
  │
  ▼
Login with App Password
  │
  ▼
Open INBOX
  │
  ▼
Search Emails
  │
  ▼
Fetch Email
  │
  ▼
Decode Email
  │
  ▼
Read Subject / Sender / Body
  │
  ▼
Process Email
  │
  ▼
Mark as Seen
  │
  ▼
Logout
  │
  ▼
Finish
```

---

# ❗ خطاهای رایج

## Authentication Failed

اگر خطای احراز هویت دریافت کردید:

* ایمیل را بررسی کنید.
* App Password را بررسی کنید.
* Two-Step Verification را بررسی کنید.
* از Password اصلی Gmail استفاده نکنید.
* مطمئن شوید App Password حذف نشده باشد.

---

## IMAP Connection Failed

تنظیمات زیر را بررسی کنید:

```text
Server: imap.gmail.com
Port: 993
SSL: Enabled
```

---

## App Password وجود ندارد

اگر گزینه App Password را مشاهده نمی‌کنید، ابتدا فعال بودن Two-Step Verification را بررسی کنید.

همچنین ممکن است بعضی حساب‌های سازمانی Google محدودیت‌های متفاوتی داشته باشند.

---

# 💡 ایده‌های توسعه آینده

این پروژه می‌تواند در آینده قابلیت‌های جذابی داشته باشد:

* 🤖 خلاصه‌سازی ایمیل با هوش مصنوعی
* 🧠 تشخیص ایمیل‌های مهم با AI
* 📊 تحلیل ایمیل‌ها
* 📎 دانلود خودکار Attachment
* 🔔 ارسال ایمیل جدید به Telegram
* 🎙️ خواندن ایمیل با Text-to-Speech
* 🗂️ دسته‌بندی خودکار ایمیل‌ها
* 🔎 جستجوی پیشرفته
* ⏰ اجرای خودکار در زمان مشخص
* 📬 اتصال همزمان چند Gmail
* 🚨 تشخیص Spam
* 🤖 اتصال به JARVIS
* 🔗 اتصال به n8n
* 📡 ساخت Webhook برای ایمیل‌های جدید

---

# 🔗 استفاده در پروژه‌های دیگر

Gmail Reader Bot می‌تواند بخشی از پروژه‌های بزرگ‌تر باشد.

برای مثال:

```text
Gmail
   │
   ▼
Gmail Reader Bot
   │
   ▼
Python
   │
   ├──────────────► Telegram
   │
   ├──────────────► AI
   │
   ├──────────────► n8n
   │
   └──────────────► JARVIS
```

به این ترتیب می‌توان یک سیستم اتوماسیون کامل برای ایمیل ساخت.

---

# 🤝 مشارکت در پروژه

اگر ایده‌ای برای توسعه پروژه دارید، می‌توانید Repository را Fork کرده و Pull Request ارسال کنید.

```bash
git checkout -b feature/new-feature
```

سپس:

```bash
git add .
```

و:

```bash
git commit -m "Add new feature"
```

در نهایت:

```bash
git push origin feature/new-feature
```

و یک Pull Request ایجاد کنید.

---

# 📜 License

این پروژه تحت **MIT License** منتشر شده است.

استفاده، تغییر و توسعه پروژه مطابق شرایط لایسنس MIT آزاد است.

---

# ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بود، خوشحال می‌شوم:

⭐ به Repository ستاره بدهید.

🍴 پروژه را Fork کنید.

📢 آن را با دوستان و برنامه‌نویسان دیگر به اشتراک بگذارید.

---

# 👨‍💻 ساخته شده توسط

<div align="center">

## 💙 شروین موسوی

### Shervin Moosavi

ساخته‌شده با ❤️ و 🐍 Python

<br>

### 🎥 YouTube

**YouTube ID: `shervinaitech`**

<br>

<a href="https://www.youtube.com/@shervinaitech">
  <img src="https://img.shields.io/badge/YouTube-shervinaitech-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube">
</a>

<br><br>

<a href="https://github.com/shervinaitechwebdeveloper-boop">
  <img src="https://img.shields.io/badge/GitHub-Shervin_Moosavi-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

</div>

---

<div align="center">

### 📧 Gmail Reader Bot

**Built with Python 🐍 | Created by Shervin Moosavi**ا
**توجه دوستان من اینو با هوش مصنوعی نوشتم برای سریع تر کردن کار**

⭐ If you like this project, don't forget to star the repository!

</div>
