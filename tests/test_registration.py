
import random
import locators
from config.urls import BASE_URL

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mock_data import (
    generate_email,
    VALID_PASSWORD,
    INVALID_EMAIL,
    EXISTING_ACC
)


class TestRegistration:

    def test_reg_success(self, driver):
        email = generate_email()
        password = VALID_PASSWORD
        expected_url = f'{BASE_URL}registration'

        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.BTN_NO_ACC).click()

        driver.find_element(*locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.INPUT_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*locators.BTN_CREATE_ACC).click()

        wait = WebDriverWait(driver, 10)

        assert wait.until(EC.url_to_be(expected_url))
        assert wait.until(EC.visibility_of_element_located(locators.USER_AVATAR))
        assert wait.until(EC.visibility_of_element_located(locators.USER_NAME))


    def test_reg_invalid_email_fail(self, driver):
        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.BTN_NO_ACC).click()

        driver.find_element(*locators.INPUT_EMAIL).send_keys(INVALID_EMAIL)
        driver.find_element(*locators.BTN_CREATE_ACC).click()

        wait = WebDriverWait(driver, 10)

        assert 'input_inputError' in wait.until(
            EC.presence_of_element_located(locators.EMAIL_ERROR_WRAP)
        ).get_attribute('class')

        assert 'input_inputError' in wait.until(
            EC.presence_of_element_located(locators.PASSWORD_ERROR_WRAP)
        ).get_attribute('class')

        assert 'input_inputError' in wait.until(
            EC.presence_of_element_located(locators.REPEAT_PASSWORD_ERROR_WRAP)
        ).get_attribute('class')

        assert wait.until(
            EC.visibility_of_element_located(locators.REG_ERROR_TEXT)
        )

    def test_reg_existing_acc_no_account_fail(self, driver):
        driver.find_element(*locators.BTN_ENTER_REG).click()
        driver.find_element(*locators.BTN_NO_ACC).click()

        driver.find_element(*locators.INPUT_EMAIL).send_keys(EXISTING_ACC['email'])
        driver.find_element(*locators.INPUT_PASSWORD).send_keys(EXISTING_ACC['password'])
        driver.find_element(*locators.INPUT_REPEAT_PASSWORD).send_keys(EXISTING_ACC['password'])
        driver.find_element(*locators.BTN_CREATE_ACC).click()

        wait = WebDriverWait(driver, 10)

        assert 'input_inputError' in wait.until(
            EC.presence_of_element_located(locators.EMAIL_ERROR_WRAP)
        ).get_attribute('class')

        assert 'input_inputError' in wait.until(
            EC.presence_of_element_located(locators.PASSWORD_ERROR_WRAP)
        ).get_attribute('class')

        assert 'input_inputError' in wait.until(
            EC.presence_of_element_located(locators.REPEAT_PASSWORD_ERROR_WRAP)
        ).get_attribute('class')

        assert wait.until(
            EC.visibility_of_element_located(locators.REG_ERROR_TEXT)
        )


