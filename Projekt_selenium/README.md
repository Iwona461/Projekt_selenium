```
# tworzymy hermetyczne środowisko dla bibliotek aplikacji:
$ python3 -m venv .venv

# aktywowanie hermetycznego środowiska:
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pip install -r test_requirements.txt

# instalacja niezbednych pakietów:

- selenium
$ sudo apt install python3-selenium

- PyCharm
To start the application, open a console, cd into "{installation home}/bin" and type:
$ cd Pobrane/pycharm/bin
$ ./pycharm.sh

- Chrome
from selenium import webdriver

# Uruchamianie zestawu testowego:
if __name__ == "__main__":  
    unittest.main()

# jako zwykły program:
$ python3 test_2.py

# Czyszczenie po teście:
def tearDown(self):
  self.driver.close()
```
