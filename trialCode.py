from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time, sys, subprocess


# driver = Chrome()
# driver.maximize_window()
# driver.get("https://testing.suis-setiawan.my.id/")
# data = testRunner.dir_report
# print(data)
# time.sleep(2)

# def read_sys():
#     if len(sys.argv) < 2:
#         print("Usage: python test.py <argument>")
#         return

#     argument = sys.argv[1]
#     long = len(sys.argv)
#     if argument == "chrome":
#         print("You provided the argument:", argument)
#     else:
#         print(f"Unknown argument: {argument}")
#     print("panjang argument : ", long)
#     print(sys.argv)

# Data yang ingin Anda kirim ke TestTrial
data_to_send = "Hello from TestRunner!"

# Menjalankan TestTrial.py dengan mengirimkan data melalui argumen
process = subprocess.run(["python", "Tools/file_reader.py", data_to_send], stdout=subprocess.PIPE, text=True)
subprocess.run(["behave", "--tags=LG0001"], check=True, shell=True)

# Membaca output dari TestTrial
output = process.stdout
print("TestRunner received:", output)