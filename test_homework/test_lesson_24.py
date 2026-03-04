# Найти элементы обозначенные стрелочками на картинке с помощью:
# - CSS
# - XPath

# 1 найти элемент Search
# input[placeholder="Search"]  - CSS
# //input[@placeholder="Search"]  - XPath

# 2 найти элемент Dashboard
# [href*="dashboard"]  - CSS
# //*[contains(@href,"dashboard")] - XPath

# 3 найти элемент свернуть
# .oxd-main-menu-button[type="button"]  - CSS
# //*[@role="none"]  - XPath

# 4 найти блок "My Actions"
#  не нашел варанта поиска через css - CSS
#  //*[text()="My Actions"]/../../.. - XPath

# 5 найти кнопку "Upgrade"
# [size="large"]  - CSS
# //button[text()=" Upgrade"]   - XPath

# 6 найти кнопку "Профиль"
# [src="/web/index.php/pim/viewPhoto/empNumber/7"]  - CSS
# //*[@src="/web/index.php/pim/viewPhoto/empNumber/7"]  - XPath

# 7 найти кнопку "Настройки"
#  .bi-gear-fill - CSS
#  //*[contains(@class, "bi-gear-fill")] - XPath

# 8 найти элемент "Engineering"
#  [title="Engineering"]  - CSS
#  //*[@title="Engineering"] - XPath
