[app]
title = LoginApp
package.name = loginapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 1

# الأيقونة (اختياري، احذف إذا لم تكن لديك واحدة)
icon.filename = %(source.dir)s/icon.png

# ملف الواجهة Kivy
kv_files = login.kv

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.build_tools_version = 33.0.2
android.minapi = 21
# لا تضف أي مكتبات NDK إضافية
# إضافة خلفية/صور داخل APK
presplash.filename = %(source.dir)s/bg.jpg
# إرسال الإنترنت
android.permissions = INTERNET
# لفتح روابط Telegram API
android.exported = True
