import sys
import main
from datetime import datetime
import pdfquery
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
import os
class PDFToExcelApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF to Excel Converter")
        self.setGeometry(100, 100, 400, 200)

        self.pdf_file_label = QLabel("Select PDF File:", self)
        self.pdf_file_label.move(20, 20)

        self.pdf_file_entry = QLabel(self)
        self.pdf_file_entry.setGeometry(20, 50, 260, 30)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setGeometry(290, 50, 80, 30)
        self.browse_button.clicked.connect(self.browse_pdf_file)

        self.convert_button = QPushButton("Convert to Excel", self)
        self.convert_button.setGeometry(20, 100, 350, 30)
        self.convert_button.clicked.connect(self.convert_to_excel)

        self.status_label = QLabel("", self)
        self.status_label.setGeometry(20, 150, 350, 30)

    def browse_pdf_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)")

        if file_path:
            self.pdf_file_entry.setText(file_path)

    def convert_to_excel(self):
        pdf_file_path = self.pdf_file_entry.text()
        if not pdf_file_path:
            self.status_label.config(text="Please select a PDF file.", fg="red")
            return

        try:
        # Read PDF data using tabula-py
            pdf = pdfquery.PDFQuery(pdf_file_path)
            pdf.load()
            extracted_data = main.pdfscrape(pdf)
            periode_str = extracted_data['Periode de stage du'].values[0]
            periode_date = datetime.strptime(periode_str, '%d-%m-%Y').date()
            # Update the DataFrame with the converted date
            extracted_data['Periode de stage du'] = periode_date
            periode_str = extracted_data['Au'].values[0]
            periode_date = datetime.strptime(periode_str, '%d-%m-%Y').date()

        # Update the DataFrame with the converted date
            extracted_data['Au'] = periode_date
            name = pdf_file_path.split('/')[-1]
            name=name[:-4]
        # Save the extracted data to an Excel file
            output_file = f"{name}.xlsx"
            extracted_data.to_excel(output_file, index=False)
            self.status_label.setText("Conversion completed successfully.")
            self.status_label.setStyleSheet("color: green;")
        except Exception as e:
            self.status_label.setText("Error occurred during conversion: " + str(e))
            self.status_label.setStyleSheet("color: red;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFToExcelApp()
    window.show()
    sys.exit(app.exec_())