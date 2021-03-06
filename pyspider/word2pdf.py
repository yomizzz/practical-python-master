from win32com.client import Dispatch
import os

wdFormatPDF = 17

def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    doc_files = []
    directory = r"C:\Users\yzhai.A123SYSTEMS\Desktop\formation"
    for root, dirs, filenames in os.walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                doc2pdf(str(root + "\\" + file))
                os.remove(str(root + "\\" + file))