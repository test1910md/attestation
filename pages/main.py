import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main import MainPageLocators

logger = logging.getLogger()


class MainPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 60)

    def deposit_button(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(MainPageLocators.DEPOSIT))
        except NoSuchElementException:
            return self.wait.until(EC.element_to_be_clickable(MainPageLocators.DEPOSIT))

    def deposit_button_click(self):
        logger.info("Open deposit page")
        self.deposit_button().click()

    def cards_button(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(MainPageLocators.CARD))
        except NoSuchElementException:
            return self.wait.until(EC.element_to_be_clickable(MainPageLocators.CARD))

    def cards_button_click(self):
        logger.info("Open card page")
        self.cards_button().click()

    def logout_button(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.LOGOUT_BUTTON)
            )
        except NoSuchElementException:
            self.wait.until(
                EC.visibility_of_element_located(MainPageLocators.LOGOUT_BUTTON)
            )

    def logout_button_click(self):
        logger.info("Logout")
        self.logout_button().click()

    def payment_button(self):
        return self.app.wd.find_element(*MainPageLocators.PAYMENT)

    def payment_button_click(self):
        logger.info("Open payment page")
        self.payment_button().click()
