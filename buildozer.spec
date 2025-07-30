[app]
title = LoginApp
package.name = loginapp
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 30
android.minapi = 21
android.ndk = 25b
android.sdk = 30
android.build_tools_version = 30.0.3
android.arch = armeabi-v7a, arm64-v8a
android.permissions = INTERNET
