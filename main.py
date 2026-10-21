
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
DATA_FILE = DATA_DIR / "data_mahasiswa.csv"


def buat_dataset():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if DATA_FILE.exists():
        return

    data = {
        "jam_belajar": [
            1, 2, 2, 3, 3, 4, 4, 5, 5, 6,
            1, 2, 3, 4, 5, 6, 7, 7, 8, 8,
            2, 3, 4, 5, 6, 7, 8, 9, 9, 10
        ],
        "kehadiran": [
            50, 55, 60, 60, 65, 70, 75, 75, 80, 85,
            45, 50, 65, 70, 80, 85, 90, 85, 95, 90,
            55, 65, 70, 80, 85, 90, 95, 95, 90, 100
        ],
        "nilai_tugas": [
            40, 45, 50, 55, 60, 65, 70, 70, 75, 80,
            35, 40, 55, 60, 75, 80, 85, 80, 95, 90,
            45, 55, 65, 75, 80, 85, 95, 95, 90, 100
        ],
        "status": [
            "Perlu Evaluasi", "Perlu Evaluasi",
            "Perlu Evaluasi", "Perlu Evaluasi",
            "Perlu Evaluasi", "Lulus", "Lulus",
            "Lulus", "Lulus", "Lulus",
            "Perlu Evaluasi", "Perlu Evaluasi",
            "Perlu Evaluasi", "Perlu Evaluasi",
            "Lulus", "Lulus", "Lulus", "Lulus",
            "Lulus", "Lulus",
            "Perlu Evaluasi", "Perlu Evaluasi",
            "Perlu Evaluasi", "Lulus", "Lulus",
            "Lulus", "Lulus", "Lulus", "Lulus", "Lulus"
        ]
    }

    pd.DataFrame(data).to_csv(DATA_FILE, index=False)
    print("Dataset contoh berhasil dibuat.")


def main():
    print("=" * 50)
    print("PREDIKSI KELULUSAN MAHASISWA")
    print("MENGGUNAKAN MACHINE LEARNING")
    print("=" * 50)

    buat_dataset()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_FILE)

    fitur = ["jam_belajar", "kehadiran", "nilai_tugas"]
    X = df[fitur]
    y = df["status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(
        max_depth=3, random_state=42
    )
    model.fit(X_train, y_train)

    prediksi = model.predict(X_test)
    akurasi = accuracy_score(y_test, prediksi)

    print("\nJumlah seluruh data:", len(df))
    print("Data untuk pelatihan:", len(X_train))
    print("Data untuk pengujian:", len(X_test))
    print(f"Akurasi model: {akurasi:.2%}")

    print("\nLaporan evaluasi model:")
    print(classification_report(y_test, prediksi, zero_division=0))

    hasil = X_test.copy()
    hasil["status_sebenarnya"] = y_test
    hasil["hasil_prediksi"] = prediksi

    hasil.to_csv(
        OUTPUT_DIR / "hasil_prediksi.csv", index=False
    )

    plt.figure(figsize=(12, 7))
    plot_tree(
        model,
        feature_names=fitur,
        class_names=model.classes_,
        filled=True,
        rounded=True
    )
    plt.title("Decision Tree - Prediksi Status Mahasiswa")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "pohon_keputusan.png",
        dpi=160,
        bbox_inches="tight"
    )
    plt.show()

    contoh = pd.DataFrame([{
        "jam_belajar": 6,
        "kehadiran": 85,
        "nilai_tugas": 80
    }])

    hasil_baru = model.predict(contoh)[0]

    print("\nContoh prediksi mahasiswa baru:")
    print(contoh.to_string(index=False))
    print("Prediksi status:", hasil_baru)

    print("\nHasil disimpan di folder output.")


if __name__ == "__main__":
    main()
