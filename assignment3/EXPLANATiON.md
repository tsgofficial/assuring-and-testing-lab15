# Selenium UI Өөрчлөлт болон Self-Healing Зарчим

## Оршил

Selenium-тэй ажиллах үед UI (Хэрэглэгчийн интерфэйс) өөрчлөгдөхөд тестүүд эвдэрч болох бөгөөд энэ нь тестийн үр дүнг хянахад хүндрэл учруулдаг. UI өөрчлөлтүүдийн үед тестийг засах автомат системийг **Self-healing** гэж нэрлэдэг. Энэ нь тестийн алдааг олж илрүүлж, өөрчлөлтийг автоматаар засах боломжийг олгодог.

Энэ гарын авлагад **Selenium** тестийн UI өөрчлөлтийн дараах эвдрэл үүсэхийг хэрхэн засах, **Self-healing** зарчмыг хэрхэн хэрэгжүүлэх талаар тайлбарлах болно.

## 1. UI Өөрчлөлт болон Эвдэрэл

### Тестийн код:

```html
<button id="loginBtn">Login</button>
```

Selenium тест:

```
driver.find_element(By.ID, "loginBtn").click()
```

Хэрвээ дээрх DOM ийм байна гэж үзвэл, loginBtn гэж тодорхойлогдсон id-тай элемент дээр дарж Login товчийг дарна. Гэхдээ, хэрвээ HTML код өөрчлөгдсөн бол:

```
<button id="signinButton">Login</button>
```

Тэгвэл дээрх Selenium тест эвдэрнэ. Тиймээс locator (байршил) хэт нухацтай тодорхойлогдсон байвал UI өөрчлөгдсөний дараа эвдрэл үүсэх магадлалтай.

### 2. Шинэ Locator

UI өөрчлөгдсөн үед locator-ийг шинэчлэх хэрэгтэй. Доор шинэ locator-ийг хэрхэн ашиглах талаар үзье.

```
driver.find_element(By.ID, "signinButton").click()
```

Харин илүү бат бөх, өөрчлөлтөд тэсвэртэй locator-ийг ашиглах нь зөв шийдэл болно.

Илүү Бат Бөх Locator:

By Name:

```
driver.find_element(By.NAME, "signinButton").click()
```

By XPath:

```
driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
```

By CSS Selector:

```
driver.find_element(By.CSS_SELECTOR, "button[id^='sign']").click()
```

Эдгээр locators нь илүү өргөн хүрээтэй бөгөөд UI өөрчлөгдсөн ч ажиллах боломжтой.

### 3. Self-Healing Зарчим

Self-healing зарчим нь Selenium тестийн үйл явцад гарч болох UI өөрчлөлтүүдийг илрүүлж, автомат засвар хийх боломжийг олгодог.

### 3.1. Retry Mechanism (Дахин Орж Оролдох Механизм)

Тестийн байршил эхний удаад олдсонгүй бол өөр өөр locator ашиглан дахин оролдож болно. Энэ нь UI өөрчлөлт үүсэхэд ашиглах хамгийн энгийн self-healing аргачлал юм.

```
def find_element_with_retry(driver, locators, max_retries=3):
    for i in range(max_retries):
        for locator in locators:
            try:
                element = driver.find_element(*locator)
                return element
            except:
                continue
    raise Exception("Unable to locate element after retries")
```

### 3.2. AI-Powered Tools (AI Ашигласан Тестийн Хэрэгслүүд)

AI-driven testing tools нь UI өөрчлөлтүүдийг илрүүлж, автомат засвар хийхэд тусалдаг. Тухайлбал, Testim.io болон Mabl гэх мэт хэрэгслүүд нь self-healing-ийн боломжуудыг агуулдаг.

### 3.3. Visual Testing (Визуал Тест)

Визуал тестийг хэрэгжүүлснээр бид UI өөрчлөлтийг зураг авах замаар илрүүлж, автоматаар засах боломжтой. Applitools гэх мэт хэрэгслүүдийг ашиглан зураг авах боломжтой.

### 4. Жишээ Код (Self-Healing)

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def find_element_with_retry(driver, locators, max_retries=3):
    for i in range(max_retries):
        for locator in locators:
            try:
                element = driver.find_element(*locator)
                return element
            except:
                continue
    raise Exception("Unable to locate element after retries")

# Browser setup
driver = webdriver.Chrome()
driver.get("https://yourwebsite.com")

# Locators list
locators = [
    (By.ID, "signinButton"),
    (By.XPATH, "//button[contains(text(), 'Login')]"),
    (By.NAME, "signinButton"),
    (By.CSS_SELECTOR, "button[id^='sign']")
]

# Try finding and clicking the element
try:
    login_button = find_element_with_retry(driver, locators)
    login_button.click()
except Exception as e:
    print(f"Test failed: {e}")
```

### 4.1. Тестийн Алдааг Дахин Оролдох

Энэхүү код нь өгөгдсөн locators-ыг ашиглан элементийг олон удаа хайж, олдсон тохиолдолд дарах болно. Хэрвээ эхний оролдлого амжилтгүй бол дахин оролдох болно.

### 5. Дүгнэлт

Self-healing зарчим нь Selenium тестийн UI өөрчлөлтүүдэд тэсвэртэй байлгахад чухал үүрэг гүйцэтгэдэг. Элементүүдийн байршлыг олон төрлийн locator ашиглан тодорхойлох нь тестийн бат бөх байдлыг сайжруулдаг. Мөн self-healing хэрэгслүүдийг ашиглан UI өөрчлөлтүүдийг автоматаар илрүүлж засах боломжтой. Хэрэв танд self-healing хэрэгсэл болон автомат засвар хийх шаардлага үүсвэл, retry mechanism болон AI-powered tools-ийг ашиглах нь үр дүнтэй арга байх болно.
