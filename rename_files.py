import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Projetos\Pessoal\python\prank\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Projetos\Pessoal\python\prank\prank")
    
    #(2) for each file, rename filename
    for file_name in file_list:
        try
            new_name = file_name.translate(str.maketrans('', '', '1234567890')) 
            print("Old Name - " + file_name)
            os.rename(file_name, new_name)
        except Exception:
            print("Error rename file - " + file_name)
        finally
            print("New Name - " + new_name)
    os.chdir(saved_path)
    
rename_files()

