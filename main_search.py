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

screenSize = driver.get_window_size()
screenW = screenSize['width']
screenH = screenSize['height']
start_x = screenW/2
start_y = screenH/6*5
distance = screenH/6

try:
    driver.implicitly_wait(10)
    #点击测试环境
    driver.find_element_by_id("com.zlqb.qyd:id/welcome_test").click()
    time.sleep(1)
    #点击贷款大全
    driver.find_element_by_id("com.zlqb.qyd:id/main_search").click()

    screenSize = driver.get_window_size()
    screenW = screenSize['width']
    screenH = screenSize['height']
    start_x = screenW/2
    start_y = screenH/6*5
    distance = screenH/6
    driver.swipe(start_x,start_y-distance,start_x,start_y,3000)





except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()
