# ============================================================================
# Soccer Stars Analyzer — Buildozer Spec  (final / production-ready)
# ============================================================================
[app]

# ----------------------------------------------------------------------------
# Identity
# ----------------------------------------------------------------------------
title          = Soccer Stars Analyzer
package.name   = soccerstarsanalyzer
package.domain = com.soccerstars

# ----------------------------------------------------------------------------
# Source
# ----------------------------------------------------------------------------
source.dir          = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf
source.main         = main.py

services = SoccerStarsService:service/main.py:foreground

# ----------------------------------------------------------------------------
# Version
# ----------------------------------------------------------------------------
version          = 1.1.0

# ----------------------------------------------------------------------------
# Orientation & display
# ----------------------------------------------------------------------------
orientation = portrait
fullscreen   = 0

# ----------------------------------------------------------------------------
# Requirements
# ----------------------------------------------------------------------------
requirements = python3==3.11.9,kivy==2.3.0,numpy,opencv,pyjnius,android

# ----------------------------------------------------------------------------
# Android SDK / NDK - تم التعديل هنا ليتوافق مع كودماجيك
# ----------------------------------------------------------------------------
android.api     = 33
android.minapi  = 26
android.ndk_api = 26
android.archs   = arm64-v8a
android.sdk_build_tools_version = 33.0.0

# Gradle / AndroidX
android.gradle_dependencies = androidx.core:core:1.13.1
android.enable_androidx      = True

# ----------------------------------------------------------------------------
# PERMISSIONS
# ----------------------------------------------------------------------------
android.permissions =
    android.permission.SYSTEM_ALERT_WINDOW,
    android.permission.FOREGROUND_SERVICE,
    android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION,
    android.permission.WAKE_LOCK,
    android.permission.INTERNET,
    android.permission.ACCESS_NETWORK_STATE,
    android.permission.VIBRATE

# ----------------------------------------------------------------------------
# AndroidManifest extras
# ----------------------------------------------------------------------------
android.extra_manifest_application_arguments =
    android:usesCleartextTraffic="true"

android.manifest.intent_filters =

# ----------------------------------------------------------------------------
# p4a (python-for-android)
# ----------------------------------------------------------------------------
p4a.branch = develop

# ----------------------------------------------------------------------------
# Build directories
# ----------------------------------------------------------------------------
[buildozer]
build_dir = .buildozer
bin_dir   = ./bin
log_level = 2
