from selenium import webdriver
import time

# Ege Universitesi ve Istinye Universitesi crawler edilemiyor.
#   6, 11 sayfa

# Dikkat: Sitedeki id'ler hep degisiyor.
Url = "https://yoksis.yok.gov.tr/websitesiuygulamalari/harita/"
WaitSeconds = 8

AllUniversity = []
switcher = {
    0: "Ad",
    1: "Website",
    2: "Eposta",
    3: "Telefon",
    4: "Fax",
    5: "Adres",
}

# Butun Selector ler
TumUniversitesiListesi_ButtonClass = "btn-danger"
ShadowWindow_DivClass = "z-window-shadow"
Rows_TrClass = "z-listitem"
RowContent_DivClass = "z-listcell-content"
Next_AtagClass = "z-paging-next"

def findTown(university):
    ### Test Cases
    # 123 BOLU
    # Kocasinan-KAYSERI
    # Atasehir ISTANBUL
    # Merkez/AGRI
    university["Sehir"] = university.get("Adres").split(" ")[-1].split("-")[-1].split("/")[-1].split(",")[-1]

def writeUniNameToFile(university):
    with open("universities.txt", "a") as file:
        findTown(university)
        file.write(university.get("Ad") + " (" + university.get("Sehir") + ")"+ "\n")

def getNextPage(secretWindow):
    print("Go to Next Page")
    nextLink = secretWindow.find_element_by_class_name(Next_AtagClass)
    status = nextLink.get_attribute("disabled")
    if status == None:
        nextLink.click()
        time.sleep(WaitSeconds)
        return "Okey"
    return status

def getUniversityInShadowWindow(secretWindow):
    print("Get University Contents")
    trElements = secretWindow.find_elements_by_class_name(Rows_TrClass)
    for trElement in trElements:
        University = {}
        contents = trElement.find_elements_by_class_name(RowContent_DivClass)
        for index, content in enumerate(contents):
            if content.text == '':
                University[switcher.get(index)] = content.get_attribute('innerHTML')
            else:
                University[switcher.get(index)] = content.text
        print(University)
        writeUniNameToFile(University)
        AllUniversity.append(University)

def main():
    print("Started Selenim Code")
    # Site acildi.
    driver = webdriver.Chrome()
    driver.get(Url)
    time.sleep(WaitSeconds)

    # Tum UniversiteListesi buttonuna tiklanildi.
    element = driver.find_element_by_class_name(TumUniversitesiListesi_ButtonClass)
    element.click()
    time.sleep(WaitSeconds)

    # Gizli pencere yakalandi.
    secretWindow = driver.find_element_by_class_name(ShadowWindow_DivClass)

    getUniversityInShadowWindow(secretWindow)
    while "Okey" == getNextPage(secretWindow):
        getUniversityInShadowWindow(secretWindow)

    print(AllUniversity)
    a = input("Exit: ")
    print(a)
    driver.quit()

if __name__ == "__main__":
    main()
