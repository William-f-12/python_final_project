#! python3
# WordToPdf.py - turn word files into pdf files.

def Usage():
    print("""
Usage:
    #1:
    WordToPdf(word_file: input path of word file,
              pdf_file: output path of pdf file)
        
    ==> recive one word file and turn it into pdf file

    #2:
    WordsToPdfs(word_folder: input folder path, 
                pdf_folder: output folder path)

    ==> walk over a folder and converge all word files to pdf
    """)

import os
from pathlib import Path
from win32com.client import Dispatch

def WordToPdf(word_file: "input path of word file", pdf_file: "output path of pdf file"):
    """recive one word file and turn it into pdf file"""

    # get the abspath and set up
    word_file = os.path.abspath(word_file)
    pdf_file = os.path.abspath(pdf_file)
    wdFormatPDF = 17

    # checking the file path
    if not os.path.isfile(word_file):
        raise FileNotFoundError("Cannot find the word_file.")

    # convert .docx to .pdf
    wordObj = Dispatch("Word.Application")
    docObj = wordObj.Documents.Open(word_file)
    docObj.SaveAs(pdf_file, FileFormat=wdFormatPDF)
    docObj.Close()
    wordObj.Quit()


def WordsToPdfs(word_folder: "input folder path", 
                pdf_folder: "output folder path, default to word_folder" = None):
    """walk over a folder and convert all word files to pdf"""

    if not pdf_folder:
        pdf_folder = word_folder
    
    word_folder = os.path.abspath(word_folder)
    pdf_folder = os.path.abspath(pdf_folder)

    # checking the folder paths
    if not os.path.isdir(word_folder):
        raise FileNotFoundError("Cannot find the word_folder.")
    if not os.path.isdir(pdf_folder):
        raise FileNotFoundError("Cannot find the pdf_folder")
    
    # walk over the folder and convert the files
    for folder, subfolder, files in os.walk(word_folder):
        print(f"Working on {folder}...")
        print(f"{len(subfolder)} more folders...\n")
        for file in files:
            print(f"{file}...")
            if file.endswith(".docx"):
                newname = os.path.join(pdf_folder, file[:-5] + ".pdf")
                WordToPdf(os.path.join(folder, file), newname)
    print("Done.")


if __name__ == "__main__":
    Usage()
