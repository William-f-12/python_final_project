#! python3
# EncryptAndDecrypt.py - to encrypt pdf and decrypt pdf

def Usage():
    print("""
Usage:
    #1
    Encrypt(file: "the input pdf file", 
            password: "the password for the encrypted file", 
            outputPath: "path for output file")

    ==> to encrypt a file use the password

    #2
    Decrypt(encrypted_file: "the input encrypted file", 
            password: "the password for the file", 
            outputPath: "path for output file, defaults to None"=None)

    ==> decrypt the input encrypted file

    #3
    Encrypt_files(input_folder: "folder path of input files", 
                  password: "password", 
                  output_folder: "output path")

    ==> walk over the folder and encrypt all pdf file
    """)

import os
import PyPDF2

def Encrypt(file: "the input pdf file", password: "the password for the encrypted file",
            outputPath: "path for output file"):
    """to encrypt a file use the password"""

    if not str(file).endswith(".pdf"):
        raise TypeError("input file should be a pdf file.")
    if not os.path.isfile(file):
        raise FileNotFoundError("input file does not exist or is not a file, and it needs to be an absolute path")
    if not os.path.isdir(outputPath):
        raise FileNotFoundError("output path need to be the absolute path of an exist folder")
    outputPath = os.path.join(outputPath, os.path.basename(file))
    
    pdfFile = open(file, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()

    if pdfReader.isEncrypted:
        return 0

    for page in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(page))
    pdfWriter.encrypt(str(password))

    resultpdf = open(outputPath, "wb")
    pdfWriter.write(resultpdf)
    pdfFile.close()
    resultpdf.close()

    return 1

# this function has a potential bug:
# it cannot work with some pdf file and will get a PdfReadWarning

def Decrypt(pdfReader: "the input PdfFileReader object", password: "the password for the file",
            outputPath: "path for output file, defaults to None"=None):
    """decrypt the input encrypted file"""

    if outputPath:
        if not os.path.isdir(outputPath):
            raise FileNotFoundError("output path need to be the absolute path of an exist folder")
        outputPath = os.path.join(outputPath, "decrypted_pdf.pdf")

    if pdfReader.isEncrypted:
        if not outputPath:
            result = pdfReader.decrypt(str(password))
            return result
        else:
            if pdfReader.decrypt(str(password)):
                pdfWriter = PyPDF2.PdfFileWriter()
                for page in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(page))
                resultpdf = open(outputPath, "wb")
                pdfWriter.write(resultpdf)
                resultpdf.close()
                return 1
            else:
                return 0

def Encrypt_files(input_folder: "folder path of input files", password: "password", output_folder: "output path"):
    """walk over the folder and encrypt all pdf file"""

    if not os.path.isdir(input_folder):
        raise FileNotFoundError("output path need to be the absolute path of an exist folder")
    if not os.path.isdir(output_folder):
        raise FileNotFoundError("output path need to be the absolute path of an exist folder")

    for folder, subfolder, files in os.walk(input_folder):
        print(f"Working on {folder} \n{len(subfolder)} more folder sneed to work on...")
        for file in files:
            if file.endswith(".pdf"):
                Encrypt(os.path.join(folder, file), str(password), output_folder)
    

if __name__ == "__main__":
    Usage()
