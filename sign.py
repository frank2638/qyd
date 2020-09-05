from appium import webdriver
import time,traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'D:\apk\app-qyd-debug-2.2.0.apk'
desired_caps['appPackage'] = 'com.zlqb.qyd'
desired_caps['appActivity'] = 'com.zlqb.app.act.WelcomeAct'
# desired_caps['unicodeKeyboard']  = True
# desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
desired_caps['chromedriverExecutableDir'] = r'D:\Tools\webdrivers\chromedriver_78'
desired_caps['automationName'] = 'uiautomator2'
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    driver.implicitly_wait(10)
    #点击测试环境
    driver.find_element_by_id("com.zlqb.qyd:id/welcome_test").click()
    time.sleep(1)
    #点击首页
    driver.find_element_by_id("com.zlqb.qyd:id/main_home").click()
    #点击签到
    driver.find_element_by_id("com.zlqb.qyd:id/home_sign").click()
    time.sleep(2)
    print(driver.contexts)
    driver.switch_to.context('WEBVIEW_com.zlqb.qyd')
    print(driver.current_context)
    #print(driver.page_source)
    #点击领金币
    #driver.find_element_by_xpath("//*[@text='领金币']").click()
    target = driver.find_elements_by_android_uiautomator('new UiSelector().text("领金币")')
    target.click()


except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()
