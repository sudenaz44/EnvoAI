import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from envo_ui import Ui_MainWindow
from backend import extract_all_features

class EnvoAI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Harita yükle
        map_path = os.path.abspath("map.html")
        self.ui.widget_harita.load(QUrl.fromLocalFile(map_path))

        # Placeholder ayarları
        self.ui.lineEdit_ada.setPlaceholderText("Ada No")
        self.ui.lineEdit_parsel.setPlaceholderText("Parsel No")

        # Buton sinyalleri
        self.ui.pushButton_ara.clicked.connect(self.arama_yap)
        self.ui.pushButton_analiz.clicked.connect(self.analiz_et)

    def arama_yap(self):
        # Test koordinatları (örnek)
        js_code = "setLocation({}, {});".format(39.92077, 32.85411)
        self.ui.widget_harita.page().runJavaScript(js_code)

    def analiz_et(self):
        point = [32.85411, 39.92077]  # longitude, latitude
        radius = 1000
        result = extract_all_features(point, radius)
        
        # Skor örneği:
        score = round((sum(float(v) for v in result.values() if isinstance(v, (int, float))) / len(result)), 2)
        self.ui.textBrowser_skor.setText(f"Sürdürülebilirlik Skoru: %{score}")

        # Özellikler yazdır
        notlar = "\n".join(f"{key.replace('_', ' ').title()}: {val}" for key, val in result.items())
        self.ui.textBrowser_note.setText(notlar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EnvoAI()
    window.show()
    sys.exit(app.exec_())
