
import pathlib
import shutil
import os
import fileinput
from pathlib import Path

dirfiles = []

# 
# -------------------
    # change this if you need to add another directory of csvs.
csvdir = "./Base_csv_files"
# -------------------

    # This is where they will be held
hostFolder = "Museum_Rakes/"




    #  -----------purpose ------------ iterate of the list of CSV files:
    # note for future use that the entry variable in this(the files) are not the names, they are in a weird format(dirfiles), so use entry.name
for entry in os.scandir(csvdir):
    if entry.is_file():  
            # --------purpose---------- create a directory, CP the template folder content and put it into the directory.
            # ------------------------- then to move CP the csv file from the csvdir 
        dirfiles.append(entry.name)
        fileDir = str(entry.name).replace(".csv","")+"_folder"

            # copying tempfolder content / creating new dir - xxxx_folder
        try:
            # =====change this if we can make a subfolder
            shutil.copytree(os.path.abspath(os.curdir+"/template_folder"), "./"+hostFolder+fileDir)
            # shutil.copytree(os.path.abspath(os.curdir+"/template_folder"), "./"+fileDir)

        except:
            print(fileDir + "------folder already exist or something(cant copy from template folder)---------")

            # moves the csv of the museum to the ^^^^ folder/fetched_items_csvs
        try: 
            shutil.copy(csvdir+"/"+entry.name,"./"+hostFolder+ fileDir+"/fetched_item_csvs")
        except:
            print(fileDir + "------folder already exists/ has been moved there (copy csv file error)---------")
        print("Directory is made and now we are doing namespace etc changes")

            # text to search for:
        c1= "import_master_data"
        c1c = (entry.name).replace(".csv","_data")
        c2 = "change1"
        # =====change this if we can make a subfolder===============
        c2c = hostFolder+(entry.name).replace(".csv", "_folder")
        # c2c = (entry.name).replace(".csv", "_folder")

        c3 = "change2"
        c3c = (entry.name).replace(".csv", "")

        #     # files to change 
        # artDistRake = Path(os.path.abspath(".")+"/"+ fileDir+"/analyze_artist_duplication.rake")
        # impRake = Path(os.path.abspath(".")+"/"+ fileDir+"/import.rake")
        # transArtRake =Path(os.path.abspath(".")+"/"+ fileDir+"/translate_artist_names.rake")

        # =====change this if we can make a subfolder============
        artDistRake = Path("./"+hostFolder+ fileDir+"/analyze_artist_duplication.rake")
        impRake = Path("./"+hostFolder+ fileDir+"/import.rake")
        transArtRake =Path("./"+hostFolder+ fileDir+"/translate_artist_names.rake")

        
            # Replacing text in artDistRake
        fin = open(artDistRake, "rt")
        data = fin.read()
        data = data.replace(c2,c2c).replace(c1,c1c).replace(c3,c3c)
        fin.close()
        fin = open(artDistRake, "wt")
        fin.write(data)
        fin.close()

                # Replacing text in impRake
        fin = open(impRake, "rt")
        data = fin.read()
        data = data.replace(c2,c2c).replace(c1,c1c).replace(c3,c3c)
        fin.close()
        fin = open(impRake, "wt")
        fin.write(data)
        fin.close()

                    # Replacing text in transArtRake
        fin = open(transArtRake, "rt")
        data = fin.read()
        data = data.replace(c2,c2c).replace(c1,c1c).replace(c3,c3c)
        fin.close()
        fin = open(transArtRake, "wt")
        fin.write(data)
        fin.close()



print("this worked")
