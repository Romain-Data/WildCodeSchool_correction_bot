from helium import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import google.generativeai as genai


class Correction_bot():
    '''
    AI assistant to help you correct exercises on Wild Code School's Odyssey platform

    Args:
        api_key (str): Google api key for Gemini
        id (str): your id on Odyssey
        pw (str): your password on Odyssey
    '''

    def __init__(self, api_key:str, id:str, pw:str, model="gemini-1.5-flash", ):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
        self.id = id
        self.pw = pw
        self.connect_url = "https://login.wildcodeschool.com/?domain=odyssey.wildcodeschool.com"
        self.base_url = "https://odyssey.wildcodeschool.com/"

    def start_browser(self):
        chrome_options = Options()
        prefs = {
            "profile.default_content_setting_values.notifications": 2 # Avoid Chrome pop-up
        }
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = start_chrome(self.connect_url, options=chrome_options)  


    def connect(self):
        self.driver.get("https://login.wildcodeschool.com/?domain=odyssey.wildcodeschool.com")
        sleep(2)
        write(self.id, into='prenom.nom@example.com')
        write(self.pw, into='your_secret_password')
        click('SE CONNECTER')
        sleep(5)
        if self.driver.current_url == self.base_url:
            sleep(2)
        else:
            print("Error on connection")


    def go_correction_page(self):
        side_bar = self.driver.find_element(By.CLASS_NAME, "mui-1t1zmtf-sidebar")
        actions = ActionChains(self.driver)
        actions.move_to_element(side_bar).perform()
        sleep(0.5)
        click('Corrections')
        sleep(0.5)
        body = self.driver.find_element(By.CLASS_NAME, "mui-ju3tx8-resultsContainer")
        actions.move_to_element(body).perform()
        sleep(2)


    def filter_exercice(self, category:str, promo:str):
        if promo:
            click('FILTRER PAR PROMO')
            sleep(0.5)
            click(promo)
            click('FILTRER PAR PROMO')
            sleep(0.5)
        if category:
            click('Filtrer par catégories')
            sleep(0.5)
            click(category)
            sleep(0.5)
            click('Filtrer par catégories')
            sleep(0.5)
        click('AFFICHER SEULEMENT...')
        sleep(0.5)
        click("Les solutions que je n'ai pas corrigées")
        click('AFFICHER SEULEMENT...')
        

    def select_first_exercice(self):
        card = self.driver.find_elements(By.CLASS_NAME, "mui-1ee1bi6-card")[0]
        actions = ActionChains(self.driver)
        actions.move_to_element(card).perform()
        click('COMMENTER LA SOLUTION')

    
    def get_student_name(self)->str:
        self.name = self.driver.find_element(By.CLASS_NAME, "userCardName").text.split()[0]
        
    

    def get_exercice_theme(self)->str:
        self.exercice = self.driver.find_element(By.CLASS_NAME, "mui-94-title-ref").text
      
    

    def get_insctruction_and_code(self, name)->str:
        # Instruction
        source = self.driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        instruction_html = str(soup).split('Challenge')[-1]
        soup_consigne = BeautifulSoup(instruction_html, "html.parser")
        self.instruction = soup_consigne.text.split(name)[0]

        # Code
        exercise_link = soup.find('a', class_='MuiPaper-root MuiPaper-outlined MuiPaper-rounded css-1q6lxo6 mui-1uljey4')['href']
        self.driver.get(exercise_link)
        sleep(2)
        source_exercise = self.driver.page_source
        source_exercise = BeautifulSoup(source_exercise, "html.parser")
        source_exercise.text
        code_element = self.driver.find_elements(By.CSS_SELECTOR, "[class*='editor flex lazy-editor']")
        self.code = '\n'.join([code.text for code in code_element])
        self.driver.back()
        
    
    def generate_comment(self)-> str:
        prompt = f"""Tu es un élève de la Wild Code School. Ton but est de mettre un commentaire sur les exercices des autres élèves.
        L'élève que tu corriges s'appelle {self.name}. Le thème de l'exercice est {self.exercice}. La consigne est : {self.instruction}. Le code de l'élève pour répondre à cette consigne est : {self.code}.
        Vérifie si le code de l'élève répond à la consigne. 
        Si le code répond correctement à la consigne, félicite l'étudiant, sinon, décris de manière très synthétique et encourageante un seul point à améliorer.
        Utilise un langage naturel, tu es l'égal de cet élève. Sois très concis, 2 phrases maximum. Ne parle pas en détail de l'exercice.
        Termine ton commentaire par 2 sauts de lignes puis «Exercice corrigé avec Selenium et Gemini» en italique"""
        response = self.model.generate_content(prompt)
        self.response = response.text
        return response.text
    

    def check_exercices(self):
        source = self.driver.page_source
        soup = BeautifulSoup(source, 'html.parser')
        result = soup.find('div', class_='mui-ju3tx8-resultsContainer') #div containing results of filters
        return bool(result)

    
    def start_engine(self):
        self.start_browser()
        sleep(0.5)
        self.connect()
        sleep(0.5)


    def correct_exercice(self, category, promo='Ma promo'):
        if not self.base_url in self.driver.current_url:
            self.start_engine()

        if not self.driver.current_url == "https://odyssey.wildcodeschool.com/reviews":
            self.go_correction_page()
            sleep(0.5)

        self.filter_exercice(category=category, promo=promo)
        sleep(0.5)
        self.select_first_exercice()
        sleep(1)
        self.get_student_name()
        self.get_exercice_theme()
        self.get_insctruction_and_code(self.name)
        comment = self.generate_comment()
        text_box = self.driver.find_element(By.CLASS_NAME, "MuiInputBase-input")
        text_box.send_keys(comment)
        approve_button = self.driver.find_element(By.CLASS_NAME, "MuiSwitch-input")
        click(approve_button)
        sleep(1)
        click('Envoyer le commentaire & Approuver')
        sleep(1)
        click('OUI, APPROUVER')
        sleep(2)
        self.driver.back()
        sleep(1)


    def correct_all_exercices(self, category, promo='Ma promo'):
        while self.check_exercices():
            self.correct_exercice(category, promo)