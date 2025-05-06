import sys
import os
import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineView
from ui.envo_ui import Ui_MainWindow
from mapping.geocoding import adresi_koordinata_cevir
from features.feature_extract import extract_all_features
from model.model_predict import predict

# QtWebEngine hatalarını önlemek için
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"

class EnvoAIApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lat = None
        self.lon = None

        # İlk yüklemede genel harita göster
        self.create_map_html(39.0, 35.0, zoom=6)
        self.load_map()

        # Placeholder ve ikonlar
        self.ui.combo_il.addItem("Şehir seçiniz")
        self.ui.combo_ilce.addItem("İlçe seçiniz")
        self.ui.combo_mahalle.addItem("Mahalle seçiniz")
        self.ui.textBrowser_skor.setPlaceholderText("Skor burada gösterilecek")
        self.ui.textBrowser_note.setPlaceholderText("Analiz bilgileri burada yer alacak")
        self.ui.pushButton_ara.setIcon(QtGui.QIcon("ui/icons/search.png"))
        self.ui.pushButton_analiz.setIcon(QtGui.QIcon("ui/icons/analyze.png"))

        self.il_ilce_mahalle = {
            "İstanbul": {
                "Kadıköy": ["Acıbadem", "Moda", "Kozyatağı"],
                "Beşiktaş": ["Levent", "Etiler"]
            },
            "Ankara": {
                "Çankaya": ["Kızılay", "Bahçelievler"],
                "Keçiören": ["Etlik", "Yayla"]
            },
            "İzmir": {
                "Karşıyaka": ["Bostanlı", "Alaybey"],
                "Bornova": ["Kazımdirik", "Evka 3"]
            }
        }

        self.load_combobox_data()
        self.ui.pushButton_ara.clicked.connect(self.search_location)
        self.ui.pushButton_analiz.clicked.connect(self.analyze_location)

    def load_combobox_data(self):
        self.ui.combo_il.addItems(self.il_ilce_mahalle.keys())
        self.ui.combo_il.currentTextChanged.connect(self.update_ilce)
        self.ui.combo_ilce.currentTextChanged.connect(self.update_mahalle)

    def update_ilce(self):
        il = self.ui.combo_il.currentText()
        self.ui.combo_ilce.clear()
        self.ui.combo_ilce.addItem("İlçe seçiniz")
        if il in self.il_ilce_mahalle:
            self.ui.combo_ilce.addItems(self.il_ilce_mahalle[il].keys())
        self.update_mahalle()

    def update_mahalle(self):
        il = self.ui.combo_il.currentText()
        ilce = self.ui.combo_ilce.currentText()
        self.ui.combo_mahalle.clear()
        self.ui.combo_mahalle.addItem("Mahalle seçiniz")
        if il in self.il_ilce_mahalle and ilce in self.il_ilce_mahalle[il]:
            self.ui.combo_mahalle.addItems(self.il_ilce_mahalle[il][ilce])

    def create_map_html(self, lat, lon, zoom=16):
        print(f"Yeni harita HTML dosyası yazılıyor: ({lat}, {lon})")
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <title>Harita</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
            <style>
                html, body, #map {{
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }}
            </style>
        </head>
        <body>
            <div id="map"></div>

            <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
            <script>
                var map = L.map('map').setView([{lat}, {lon}], {zoom});
                L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                    maxZoom: 19,
                }}).addTo(map);
                L.marker([{lat}, {lon}]).addTo(map)
                    .bindPopup('Seçilen Konum')
                    .openPopup();
            </script>
        </body>
        </html>
        """
        os.makedirs("templates", exist_ok=True)
        with open("templates/map.html", "w", encoding="utf-8") as f:
            f.write(html)

    def load_map(self):
        html_path = os.path.abspath("templates/map.html").replace("\\", "/")
        self.ui.widget_harita.setUrl(QtCore.QUrl.fromLocalFile(html_path))
        self.ui.widget_harita.setVisible(True)
        self.ui.widget_harita.setEnabled(True)
        self.ui.widget_harita.reload()

    def search_location(self):
        il = self.ui.combo_il.currentText()
        ilce = self.ui.combo_ilce.currentText()
        mahalle = self.ui.combo_mahalle.currentText()

        if "seçiniz" in [il, ilce, mahalle]:
            self.ui.textBrowser_note.setText("Lütfen geçerli bir şehir, ilçe ve mahalle seçin.")
            return

        adres = f"{mahalle}, {ilce}, {il}"
        lat, lon = adresi_koordinata_cevir(adres)

        if lat and lon:
            self.lat = lat
            self.lon = lon
            self.create_map_html(lat, lon)
            QtCore.QTimer.singleShot(500, self.load_map)
            self.ui.textBrowser_note.setText("Konum başarıyla yüklendi.")
        else:
            self.lat = None
            self.lon = None
            self.ui.textBrowser_note.setText("Adres bulunamadı.")

    def analyze_location(self):
        if self.lat is None or self.lon is None:
            self.ui.textBrowser_note.setText("Lütfen önce bir konum arayın.")
            return

        try:
            features = extract_all_features([self.lon, self.lat], radius=1000)
            score = predict(features.iloc[0].to_dict())
            self.ui.textBrowser_skor.setText(f"%{int(score)}")
            note = "\n".join([f"• {k.replace('_', ' ').title()}: {round(v, 2) if isinstance(v, float) else v}" for k, v in features.iloc[0].items()])
            self.ui.textBrowser_note.setText(note)
        except Exception as e:
            self.ui.textBrowser_note.setText(f"Analiz sırasında hata oluştu:\n{str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = EnvoAIApp()
    window.show()
    sys.exit(app.exec_())
