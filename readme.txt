Stepik Selenium course project: https://stepik.org/course/575/syllabus
Certificate: https://stepik.org/cert/2148209

ЕСЛИ ПРИ ЗАПУСКЕ ТЕСТА В КОНСОЛЬ ПАДАЕТ ОШИБКА Message: unknown error: cannot find Chrome binary
ТО МОЖНО ПОПРОБОВАТЬ В def browser УДАЛИТЬ СТРОКУ options.binary_location = \
            '/Users/user/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
ИЛИ ПОДСТАВИТЬ СВОЙ ПУТЬ, ТАК КАК РАСПОЛОЖЕНИЕ ФАЙЛА В СИСТЕМЕ И ЕГО ВЕРСИИ МОГУТ ОТЛИЧАТЬСЯ ОТ ВАШИХ
