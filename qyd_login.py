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


# desired_caps['automationName'] = 'uiautomator2'
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    driver.implicitly_wait(10)
    driver.find_element_by_id("com.zlqb.qyd:id/welcome_test").click()
    time.sleep(1)
    #点击登录按钮
    #driver.implicitly_wait(10)
    #driver.find_element_by_id("com.zlqb.qyd:id/login").click()
    #time.sleep(1)
    #点击密码登录
    driver.find_element_by_id("com.zlqb.qyd:id/login_pwd_btn").click()
    time.sleep(1)

    # 输入用户名、密码
    #delete = driver.find_element_by_id("com.zlqb.qyd:id/login_phone_ed")
    #delete.click()
    ele = driver.find_element_by_id("com.zlqb.qyd:id/login_phone_ed")
    ele.clear()
    ele.send_keys('18365031085')
    ele = driver.find_element_by_id("com.zlqb.qyd:id/login_psw_ed")
    ele.send_keys('zlqb001')

    driver.find_element_by_id("com.zlqb.qyd:id/login_user_icon").click()

    time.sleep(2)
    # 点击登录
    driver.find_element_by_id('com.zlqb.qyd:id/login_btn').click()

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()


