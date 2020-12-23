#!/user/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class BaseBy(By):
    IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
    IOS_PREDICATE = MobileBy.IOS_PREDICATE
    IOS_CLASS_CHAIN = MobileBy.IOS_CLASS_CHAIN
    ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
    ANDROID_VIEWTAG = MobileBy.ANDROID_VIEWTAG
    WINDOWS_UI_AUTOMATION = MobileBy.WINDOWS_UI_AUTOMATION
    ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
    IMAGE = MobileBy.IMAGE
    CUSTOM = MobileBy.CUSTOM
