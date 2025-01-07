# Gas Oil Emissions Data Assessor (GOEDA)

## Previous name: Canadian Oilfield Envrionmental Assessor (COEA)

Repository for the Gas Oil Emissions Data Assessor (GOEDA) tool.  
This version is created by: Kareem Youssef  
With contributions and guidance from: Dr. Joule Bergerson and Julia Yuan

## Acknowledgment

This version of the GOEDA tool is created based on the original tool created by Alex Bradley in 2020. If you would like to learn more about this tool and it's use cases, please refer to resource below:  
Alex Bradley's Research Paper - http://hdl.handle.net/1880/111763

## Overview

GOEDA (previously named COEA) originally required python 2.7, it is now updated to run on Python 3 (tested on Python 3.12). The environment is best setup using a package management tool such as conda. The `coea_gui.py` is the main script to run the tool. This will run the tool's Graphical User Interface (GUI) were you can provide your inputs, then click on the _submit_ button. The tool will then call various functions from the runfiles folder, ultimately exporting results to a version of the OPGEE tool where emissions intensities can be estimated. The analysis is completed based on the selection of a set of wells. The following image shows some default parameters that can be used for testing.

![Example Inputs for Search](COEA_py3/images/example2.png)

## Datasets

The GOEDA tool relies on several datasets describing several activities of the upstream Canadian O&G industry.

The Project Data can be downloaded and unzipped from here - https://drive.google.com/file/d/17g927s3yLod_ujxeNGZtKvLEfnrX6hYj/view?usp=sharing

Additonal project data and reports that may be of use can be found here - https://drive.google.com/drive/folders/1-kXnw8VZBgOziqi7pjq4OuPjRuDqKCF-?usp=sharing

## Setup

### Folder Structure

To ensure that GOEDA connects properly with OPGEE Python, it is important that your folder structure is as follows:

1. Create a folder anywhere on your machine, name it "LCA" for example. This folder is where the GOEDA and OPGEEv4 repositories will be cloned.
2. Open a terminal page, navigate to this folder and then clone the GOEDA tool using the `git clone` command followed by the HTTPS of this repository: https://github.com/kareim-y/COEAv2.git
3. Once this is complete ensure that you have the following folder structure:  
   LCA/  
   └── COEAv2/
4. Using the links available in the _Datasets_ section, install the datasets and move them into the `Project Data` Folder which is located inside the `COEAv2/COEA_py3` folder.
5. This should be your folder structre now:  
   LCA/  
   └── COEAv2/  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── COEA*py3/  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Project Data/\_dataset folders*/

### GOEDA Installation

Once the repository cloning is comepleted, follow the steps below:

1. Install conda miniforge on local machine (https://github.com/conda-forge/miniforge). Existing conda install should also work.
2. Using terminal, navigate into the `COEAv2/COEA_py3` folder then create the enviornment `conda create --name coea` (This command will make `coea` the name of the environment, you can pick another name by using `conda create --name <chosen name>`)
3. Once the conda environment is created, activate it using `conda activate coea` (or `conda activate <chosen name>`)
4. Install the following required libraries while the conda environemnt is active, `pip install pandas numpy matplotlib scipy chardet shapely openpyxl`
<!-- 4. Edit the file _runfiles/map_to_drive.py_ to point to the folder containing the unzipped 'Project Data' file downloaded from the above link. -->
5. Test installation by running the script `python coea_gui.py`, then clicking on the `Check Installation of Required Libraries` button at the bottom of the GUI.

### OPGEEv4 Installation

1. Open a new terminal and use this link to navigate to the OPGEE documentation, specifically to the _Install opgee in an Anaconda virtual environment_ page. https://opgee.readthedocs.io/en/latest/install.html
2. If the link above doesn't work, navigate to the README.md file in the OPGEEv4 repository (https://github.com/msmasnadi/OPGEEv4) and a link to the OPGEEv4 documentation should be linked there.
3. In the _Install opgee in an Anaconda virtual environment_ tab, follow steps 1 to 3.
4. now navigate to the LCA/ folder in terminal, then run the command in step 4 in _Install opgee in an Anaconda virtual environment_, this command will clone the OPGEEv4 repository.
5. This should be your folder structre now:  
   LCA/  
   ├── COEAv2/  
   &nbsp;│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── COEA*py3/  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Project Data/\_dataset folders*/  
   └── OPGEEv4/
6. Your OPGEE package should be ready for use now

## Using GOEDA and OPGEE

### Using GOEDA

1. When the folder structuring and installation is compeleted, run the GOEDA GUI by executing the `coea_gui.py` file.
2. Provide the inputs required in by filling up textboxes and selecting/deselecting checkboxes.
3. Once your inputs are compeleted, click on _submit_ at the bottom of the page (scrolling using your mouse does not work on the GUI, use the slide bar on the right of the screen)
4. You should be greeted with a pop-up message that shows all your inputs and once you click _ok_ the GOEDA tool will start executing the required files.
5. This pop-up will stay on your screen until the GOEDA tools comepletes its run, you can track the progress of the GOEDA tool by looking at the terminal.
6. Once the GOEDA run is complete, a pop-up message will alert you and then another message will alert you when the results are transferred to OPGEEv4 for further analysis.
7. Keep an eye on terminal to make sure no errors have occured.

#### Using OPGEEv4

1. If GOEDA functions as intended, you will only need to enter 2 terminal commands to run OPGEEv4.
2. Navigate to the `OPGEEv4/opgee` folder using another terminal page, activate the anaconda environment you set-up earlier (by following the _OPGEEv4 Installation_ section of this document), this command should be `conda activate opgee`
3. Then run this command `opg run -o output -a SSE_test -m etc/opgee.xml` (This command works as of version 4.1.0 of OPGEEv4, the command in this step might change as future versions of OPGEEv4 are released, if you run into issues in this step, refer to the OPGEEv4 documentation)
4. Keep an eye on terminal to see the progress of the OPGEEv4 run.
5. Once the run is complete, the results will be saved in `carbon_intensity.csv` file, in the folder `OPGEEv4/output`.

### Contact

Reach out to kareim.youssef@ucalgary.ca or alexbradley60@gmail.com
