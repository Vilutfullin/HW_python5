import os
from selene import browser, have

def test_registration():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Vil')
    browser.element('#lastName').type('Lutfullin')
    browser.element('#userEmail').type('villutfullin@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9874354351')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1995"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--015').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('Toolsqa.jpg'))
    browser.element('#currentAddress').type('Samara Russia')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()

    browser.element('#submit').click()

    browser.element('.table-responsive').all('td').even.should(
            have.exact_texts('Vil Lutfullin', 'villutfullin@gmail.com',
                             'Male','9874354351', '15 July,1995', 'English',
                             'Sports', 'Toolsqa.jpg', 'Samara Russia', 'NCR Noida'))