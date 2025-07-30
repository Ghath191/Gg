[app]
title = KivyLogin
package.name = kivylogin
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

[android]
android.api = 33
android.minapi = 21
android.permissions = INTERNET
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.ndk = 23b
android.sdk = 24.4.1
android.ndk_path = 
android.sdk_path = 
android.extra_args = --accept-licenses
