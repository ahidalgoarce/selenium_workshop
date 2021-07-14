
# bnk
import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ViewProductDetails(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url="https://www.amazon.com"

    # declare variable to store search term
    search_term="WD My Passport 4TB"

    # --- Pre - Condition ---
    def setUp(self):
        # declare and initialize driver variable
        self.driver=webdriver.Chrome(executable_path="D:/DEV/drivers/chromedriver.exe")       
        # browser should be loaded in maximized window
        self.driver.maximize_window()
        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        self.driver.implicitly_wait(10)  #10 is in seconds

    # --- Steps for AMZN_Search_TC_001 ---
    def test_AMZN_Search_TC_001_load_home_page(self):
        """User should be able to load Amazon’s Home Page"""
        # to initialize a variable to hold reference of webdriver instance being passed to the function as a reference.
        driver=self.driver
        # to load a given URL in browser window
        driver.get(self.base_url)
        
        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("Amazon",driver.title)

    # --- Steps for AMZN_Search_TC_002 ---
    def test_AMZN_Search_TC_002_search_for_a_term(self):
        """User should be able to search products."""
        # to load a given URL in browser window
        self.driver.get(self.base_url)         
        # to enter search term, we need to locate the search textbox
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(self.search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to verify if the search results page loaded
        self.assertIn(self.search_term,self.driver.title)
        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)    
        
    # --- Steps for AMZN_Search_TC_003 ---
    def test_AMZN_Search_TC_003_add_item_to_cart(self):    
        """User should be able to add product to cart."""
        # to load a given URL in browser window
        self.driver.get(self.base_url)        
        # to enter search term, we need to locate the search textbox
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(self.search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to click on the first search result's link
        self.driver.find_element_by_xpath("(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        # since the clicked product opens in a new tab, we need to switch to that tab.
        # to do so we will use window_handles()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # to add the product to cart by clicking the add to cart button        
        self.driver.find_element_by_id("add-to-cart-button").click()
        # to verify that sub cart page has loaded
        self.assertTrue(self.driver.find_element_by_id("hlb-subcart").is_enabled())
        # to verify that the product was added to the cart successfully
        self.assertTrue(self.driver.find_element_by_id("hlb-ptc-btn-native").is_displayed())

    # --- Steps for AMZN_Search_TC_004 ---
    def test_AMZN_Search_TC_004_delete_item_from_cart(self):
        """User should be able to delete an item from cart"""  
        # to load a given URL in browser window
        self.driver.get(self.base_url)        
        # to enter search term, we need to locate the search textbox
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(self.search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to click on the first search result's link
        self.driver.find_element_by_xpath("(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        # since the clicked product opens in a new tab, we need to switch to that tab.
        # to do so we will use window_handles()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # to add the product to cart by clicking the add to cart button        
        self.driver.find_element_by_id("add-to-cart-button").click()
        # to confirm if the cart is empty
        #  print (self.driver.find_element_by_id('nav-cart-count').text)
        cartCount=int(self.driver.find_element_by_id('nav-cart-count').text)        
        if(cartCount<1):
            print("Cart is empty")
            exit()
        # to click on the Cart link
        self.driver.find_element_by_id("nav-cart").click()
        # to confirm Cart page has loaded and if yes then delete item              
        if(self.driver.title.startswith("Amazon.in Shopping Cart")):
            # to delete an item from the Cart
            self.driver.find_element_by_xpath("//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]").click()
            time.sleep(2)        
        # to confirm the item was delete successfully
        self.assertTrue(int(self.driver.find_element_by_id('nav-cart-count').text) < cartCount)        

    # --- Steps for AMZN_Search_TC_005 
    def test_AMZN_Search_TC_005_test_signin_to_checkout(self):
        """User must sign in to checkout"""
        # to load a given URL in browser window
        self.driver.get(self.base_url)        
        # to enter search term, we need to locate the search textbox
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(self.search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to click on the first search result's link
        self.driver.find_element_by_xpath("(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        # since the clicked product opens in a new tab, we need to switch to that tab.
        # to do so we will use window_handles()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # to add the product to cart by clicking the add to cart button        
        self.driver.find_element_by_id("add-to-cart-button").click()
        # to click on the 'Proceed to Buy' button
        self.driver.find_element_by_id('hlb-ptc-btn-native').click()
        # to confirm if SignIn page has loaded
        self.assertTrue(self.driver.title.startswith("Amazon Sign In"))
        # to confirm if the email or mobile number textbox is visible or not
        self.assertTrue(self.driver.find_element_by_id('ap_email').is_displayed())   
    
    # --- post - condition ---
    def tearDown(self):
        # to close the browser
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/DEV/amazond/Reports'))