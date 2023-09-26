import subprocess

#------------------------------------- SETUP PARAMS ----------------------------------------------------

need_report = False                                             # Change to true for generate report while running testing
dir_report  = "Documentation\Report\FILE_result"                # directory report
test_tags   = "LG0002"                                          # use comma "," to run multiple tags


#-------------------------------------- RUNNING TERMINAL ------------------------------------------------
try:
    if need_report:
        subprocess.run(["behave", "--tags="+test_tags, "-f", "allure_behave.formatter:AllureFormatter", "-o", dir_report, "./features"], check=True, shell=True)
        subprocess.run(["allure", "generate", dir_report,"--clean", "-o", "Documentation\Report\HTML_result"], check=True, shell=True)
        subprocess.run(["allure", "serve", dir_report], check=True, shell=True)

    else:
        subprocess.run(["behave", "--tags="+test_tags], check=True, shell=True)

        
except subprocess.CalledProcessError as e:
    print("Error running test:", e)