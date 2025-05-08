from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# 옵션 객체 생성
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "172.30.1.61:5555"
options.app_package = "com.ss.android.ugc.tiktok.lite"
options.app_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
options.no_reset = True

try:
    driver = webdriver.Remote(
        command_executor='http://localhost:4723/wd/hub',
        options=options
    )
    print("실행 성공!")

    # 앱이 실행된 후 5초 대기
    driver.implicitly_wait(5)

    # Xpath로 '포인트' 버튼 선택
    driver.find_element(
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@content-desc="포인트"]/android.widget.ImageView').click()
    print("Footer 포인트 버튼 클릭")

    for i in range(40):
        # 시청 버튼 선택
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("시청"))').click()
        print(f"시청 버튼 ({i+1}번째) 클릭")
        time.sleep(17) # 17초 대기

        # 시청에서 닫기 버튼 선택
        driver.find_element(
            AppiumBy.ID,
            'com.ss.android.ugc.tiktok.lite:id/obw').click()
        print(f"닫기 버튼 ({i+1}번째) 클릭")
        time.sleep(2)  # 닫기 후 잠시 대기 

except Exception as e:
    print("에러 발생:", e)
