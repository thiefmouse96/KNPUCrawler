import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome('C:/Users/thief/AppData/Local/Programs/Python/Python38/chromedriver.exe')
driver.implicitly_wait(3)
# url 로딩
driver.get('https://www.police.ac.kr/police/police/master/44/boardList.do?mdex=police17')
# 해당 사이트 제목 경찰대학인지 확인
assert "경찰대학" in driver.title


elem = driver.find_element_by_name("searchKeyword")
elem.send_keys("수의계약")

elem = driver.find_element_by_id("btnSearch") 
elem.click()

i = 0

try:
    while True: 
        lawData = driver.find_elements_by_css_selector(".file-download")
        for i in range(len(lawData)):
            lawData[i].click()
            # print(lawData)

            time.sleep(3.0)
            i += 1

        driver.find_element_by_xpath("//*[@id=\"cont\"]/div[3]/div[2]/span[2]/a[1]").click()
except: 
    # 검색 완료 후 크롬 창 최대화
    driver.maximize_window()
    # 새로고침
    driver.refresh()
    # 3초 후 드라이버 종료(크롬 창 닫힘)
    time.sleep(3)
    print('Process Completed')
    driver.quit()


# pages = 0
# while True:
#     # driver.find_element_by_css_selector("paging_btn m_right15").click()
#     driver.find_element_by_xpath("//*[@id=\"cont\"]/div[3]/div[2]/span[2]/a[1]").click()
    
#     pages += 1


# # 검색 완료 후 크롬 창 최대화
# driver.maximize_window()
# # 새로고침
# driver.refresh()
# # 3초 후 드라이버 종료(크롬 창 닫힘)
# time.sleep(3)
# print('Process Completed')
# driver.quit()