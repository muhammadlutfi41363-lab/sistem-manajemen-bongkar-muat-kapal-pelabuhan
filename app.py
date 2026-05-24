from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

antrian = []
riwayat = []

@app.route("/")
def index():

    total_muatan = sum(
        float(kapal["berat"])
        for kapal in antrian
    ) if antrian else 0

    return render_template(
        "index.html",
        antrian=antrian,
        riwayat=riwayat,
        total_antrean=len(antrian),
        total_selesai=len(riwayat),
        total_muatan=total_muatan
    )

@app.route("/tambah", methods=["POST"])
def tambah():

    kapal = {
        "nomor": request.form["nomor"],
        "nama": request.form["nama"],
        "nahkoda": request.form["nahkoda"],
        "dermaga": request.form["dermaga"],
        "muatan": request.form["muatan"],
        "berat": request.form["berat"],
        "waktu": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    }

    antrian.append(kapal)

    return redirect("/")

@app.route("/proses")
def proses():

    if antrian:

        kapal = antrian.pop(0)

        kapal["selesai"] = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        riwayat.append(kapal)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
