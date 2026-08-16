import email
from email.header import decode_header
import imaplib

# اطلاعات حساب
EMAIL_USER = "example@gmail.com"  # ایمیل خودت
APP_PASSWORD = "XXXXXXXXXXXXXX"  # رمز ۱۶ رقمی

try:
    # اتصال به سرور
    mail = imaplib.IMAP4_SSL("142.250.102.108", 993)
    mail.login(EMAIL_USER, APP_PASSWORD)
    mail.select("inbox")

    # ۱. جستجوی تمام ایمیل‌ها 
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    print(f"تعداد کل ایمیل‌های پیدا شده: {len(email_ids)}")

    # پردازش تمام ایمیل‌ها
    for e_id in email_ids:
        # دریافت محتوای ایمیل
        _, msg_data = mail.fetch(e_id, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # استخراج موضوع و فرستنده
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")
                from_ = msg.get("From")

                print(f"پردازش شد: {from_} -> {subject}")

                # ۲. علامت زدن به عنوان دیده شده (Seen)
                # این دستور ایمیل را در جیمیل به وضعیت خوانده‌شده تغییر می‌دهد
                mail.store(e_id, '+FLAGS', '\\Seen')

    print("تمام ایمیل‌ها پردازش و علامت‌گذاری شدند.")

    mail.close()
    mail.logout()

except Exception as e:
    print(f"خطایی رخ داد: {e}")
