<div align="center">

# 📧 Gmail Reader Bot with Python
### ربات خواندن ایمیل‌های جیمیل با پایتون

A lightweight, robust Python tool for fetching, reading, and organizing emails from Gmail using the **IMAP** protocol.  
یک ابزار سبک و کاربردی با پایتون برای دریافت، خواندن و مدیریت خودکار ایمیل‌های جیمیل با استفاده از پروتکل **IMAP**.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

</div>

---

## 🌟 Features / ویژگی‌ها

* **Fetch All Emails / دریافت تمام ایمیل‌ها:** Reads all incoming emails or filters specifically for unread messages. (قابلیت خواندن تمام ایمیل‌ها یا فقط ایمیل‌های خوانده‌نشده)
* **Auto-Mark as Read / تغییر وضعیت به Seen:** Automatically updates the email status to `Seen` directly on the Gmail server. (علامت‌گذاری خودکار ایمیل‌ها به عنوان خوانده‌شده روی سرور)
* **Unicode & UTF-8 Support / پشتیبانی کامل از UTF-8:** Properly decodes encoded email headers, Persian text, and emojis. (پشتیبانی کامل از متون فارسی، ایموجی‌ها و کاراکترهای خاص)
* **Zero External Dependencies / بدون نیاز به پکیج جانبی:** Built entirely using Python's standard libraries (`imaplib`, `email`). (ساخته‌شده کاملاً با کتابخانه‌های داخلی پایتون)

---

## ⚙️ Setup & App Password / پیش‌نیازها و دریافت رمز برنامه

Google restricts standard password access for scripts. You must generate a 16-character **App Password**:  
گوگل اجازه ورود مستقیم با رمز اصلی حساب را نمی‌دهد، بنابراین باید یک رمز ۱۶ رقمی اختصاصی (App Password) بسازید:

1. Go to [Google Account Security Settings](https://myaccount.google.com/security) and ensure **2-Step Verification** is turned ON.  
   (وارد تنظیمات امنیت حساب گوگل شوید و تایید دو مرحله‌ای را فعال کنید.)
2. Visit [Google App Passwords](https://myaccount.google.com/apppasswords) or search for "App passwords".  
   (عبارت App passwords را در حساب گوگل جستجو کرده یا وارد لینک شوید.)
3. Enter a name (e.g., `Python Reader`) and click **Create**.  
   (یک نام دلخواه انتخاب کرده و روی Create بزنید.)
4. Copy the generated **16-character password**.  
   (رمز ۱۶ رقمی داده‌شده را کپی کنید.)

---

## 🚀 Usage / نحوه اجرا

### 1. Clone the Repository / کلون کردن پروژه
```bash
git clone [https://github.com/shervinaitechwebdeveloper-boop/gmailreader.git](https://github.com/shervinaitechwebdeveloper-boop/gmailreader.git)
cd gmailreader
