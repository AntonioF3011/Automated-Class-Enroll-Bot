from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#==============FUNCIONES==========================##
def click_continue_button():
    try:
        # Verificar si el botón de continue está dentro de un iframe
        driver.switch_to.default_content()  # Asegúrate de estar en el contexto principal
        time.sleep(3)  # Esperar un momento después de refrescar
        
        # Vuelve a verificar si hay iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if len(iframes) > 0:
            driver.switch_to.frame(iframes[0])  # Cambia al primer iframe, ajusta si hay más iframes
            
        # Buscar el botón de Continue
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/div/form/div[5]/div[1]/div/ul/li/a")))
        continue_button.click()
        print("Clic en Continue realizado.")
        
        # Volver al contenido principal
        driver.switch_to.default_content()
    except Exception as e:
        print(f"No se pudo hacer clic en el botón Continue: {e}")

# Función para buscar el botón de finish enrolling y hacer clic
def click_finish_enrolling_button():
    try:
        driver.switch_to.default_content()  # Asegúrate de estar en el contexto principal
        time.sleep(3)  # Esperar un momento después de refrescar

        # Vuelve a verificar si hay iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if len(iframes) > 0:
            driver.switch_to.frame(iframes[0])  # Cambia al iframe donde están los botones
        
        # Buscar el botón de Finish Enrolling
        finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/form/div[5]/div[1]/div/ul/li[3]/a/span")))
        finish_button.click()
        print("Clic en Finish Enrolling realizado.")
        
        # Volver al contenido principal
        driver.switch_to.default_content()
    except Exception as e:
        print(f"No se pudo hacer clic en el botón Finish Enrolling: {e}")

# Función para verificar si la clase está cerrada
def is_class_closed():
    try:
        # Asegurarse de que estamos en el iframe correcto
        driver.switch_to.default_content()  # Salimos de cualquier iframe actual
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if len(iframes) > 0:
            driver.switch_to.frame(iframes[0])

        # Verificar si existe el ícono de clase cerrada
        closed_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-gh-replace='CLOSED_ICN']")))
        if closed_icon:
            print("La clase está cerrada.")
            return True
    except Exception as e:
        print(f"No se encontró el ícono de clase cerrada: {e}")
        return False

# Accede al chromedriver
driver_path = 'C:\\Users\\antof\\OneDrive\\Desktop\\chrome\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'  #direccion del chromedriver

# Inicializa el servicio del WebDriver
service = Service(driver_path)

# Inicializa el navegador usando el servicio
driver = webdriver.Chrome(service=service)

# Inicializa WebDriverWait con un tiempo máximo de espera (20 segundos en este caso)
wait = WebDriverWait(driver, 20)

# Enter your FSU username and password here
username = os.getenv("FSU_USERNAME")
password = os.getenv("FSU_PASSWORD")

# Abre la página de inicio de sesión de FSU
driver.get("https://cas.fsu.edu/cas/login?service=https://www.my.fsu.edu/")

# Espera a que el campo "username" sea visible y escribe el nombre de usuario
username_box = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_box.send_keys(username)

# Espera a que el campo "password" sea visible y escribe la contraseña
password_box = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_box.send_keys(password)

# Presiona Enter para enviar el formulario
password_box.send_keys(Keys.RETURN)

# Espera a que el enlace "Otras opciones" sea clickeable y haz clic en él
link_otrasOpciones = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Otras opciones")))
link_otrasOpciones.click()

# Espera a que el enlace "Enviar a iOS" sea visible y haz clic en él
link_enviar_ios = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Enviar a \"iOS\"')]")))
link_enviar_ios.click()

# Dale clic a "sí, este es mi dispositivo"
trust_button = wait.until(EC.element_to_be_clickable((By.ID, "trust-browser-button")))
trust_button.click()

# Entra al enlace de SC
link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'campus.omni.fsu.edu/psc/sprdcs/EMPLOYEE/SA/c/NUI_FRAMEWORK')]")))
link.click()

# Abre una nueva pestaña
driver.execute_script("window.open('');")

# Cambia el enfoque a la nueva pestaña
driver.switch_to.window(driver.window_handles[-1])

# Carga la nueva URL en la nueva pestaña
driver.get("https://cas.fsu.edu/cas/login?service=https%3A%2F%2Fcampus.omni.fsu.edu%2Fpsc%2Fsprdcs%2FEMPLOYEE%2FSA%2Fc%2FNUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL%3FCONTEXTIDPARAMS%3DTEMPLATE_ID%3APTPPNAVCOL%26scname%3DADMN_FSU_SR_ST_MY_CLASSES_CL_N%26PanelCollapsible%3DY%26PTPPB_GROUPLET_ID%3DFSU_SR_ST_MY_CLASSES_CL_TL%26CRefName%3DADMN_NAVCOLL_25%26ICAJAXTrf%3Dtrue%26ptgpid%3DADMN_S201807141525557333111812")

# Verifica si hay iframes
iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(f"Cantidad de iframes: {len(iframes)}")
if len(iframes) > 0:
    driver.switch_to.frame(iframes[0])  # Cambia esto según el número del iframe correcto

# Usa un selector CSS en lugar del XPath para buscar el radio button
try:
    radio_button_2025 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='SSR_DUMMY_RECV1$sels$1$$0']")))
    print("Elemento encontrado")

    # Haz clic en el radio button directamente (sin ejecutar el script JavaScript)
    radio_button_2025.click()

    print("Clic en radio button ejecutado")
except Exception as e:
    print(f"No se pudo encontrar el elemento: {e}")

# Haz clic en el botón "Continue"
continue_button = wait.until(EC.element_to_be_clickable((By.ID, "DERIVED_SSS_SCT_SSR_PB_GO")))
continue_button.click()

# Inicializa una variable para controlar el ciclo
repetir_infinito = True

# Ciclo para refrescar hasta que la clase no esté cerrada
while repetir_infinito:
    try:
        if is_class_closed():
            print("La clase sigue cerrada, refrescando la página...")
            driver.refresh()
            time.sleep(6)  # Espera para dar tiempo a que la página se recargue
        else:
            print("¡La clase ya no está cerrada! Procediendo con la inscripción...")
            # Haz clic en el botón de Continue
            click_continue_button()

            # Haz clic en el botón de Finish Enrolling
            click_finish_enrolling_button()

            repetir_infinito = False
            
    except Exception as e:
        print(f"Error en el ciclo: {e}")
        repetir_infinito = False  # Para detener el ciclo en caso de error


# Tiempo de espera adicional para no cerrar el navegador de inmediato
time.sleep(777)

