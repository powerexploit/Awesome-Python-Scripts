# Binod Detector ( 2020 Trend )

import os




def isbinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
        # Detect all forms of Binod like bInoD

    if "binod" in fileContent.lower():
        return True
    else:
        return False


if __name__ == "__main__":
    # Listing the content of this folder
    dir_contents = os.listdir()

    nBinod = 0
    # For each text file, detect Binod in them

    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag = isbinod(item)
            if(flag):
                print(f"Binod found in {item}")
                nBinod +=1
            else:
                print(f"!!!!! Binod not found in {item} !!!!!")

    print("******* Binod Ditector Summary *******")
    print(f"{nBinod} files found with Binod hidden into them")
