import matplotlib.pyplot as plt
from collections import defaultdict
import os

def generate_html_report(data, report_path="report.html"):
    # Création du graphique
    fig, ax = plt.subplots(figsize=(8, 6))
    categories = list(data.keys())
    values = list(data.values())
    ax.bar(categories, values, color='skyblue')

    # Ajouter des labels et un titre
    ax.set_xlabel('ID de Défaut')
    ax.set_ylabel('Nombre de Défauts')
    ax.set_title('Histogramme des Défauts par ID')

    # Sauvegarder le graphique en image PNG
    img_path = "chart.png"
    plt.savefig(img_path)
    plt.close()

    # Création du fichier HTML contenant l'image
    with open(report_path, 'w') as file:
        file.write(f"""
        <html>
        <head><title>Rapport de Défauts</title></head>
        <body>
            <h1>Rapport des Défauts</h1>
            <img src="{img_path}" alt="Histogramme des défauts">
        </body>
        </html>
        """)

    print(f"Rapport HTML généré : {report_path}")
    print(f"Image enregistrée : {img_path}")

def main():
    defect_counts = defaultdict(int)
    defect_counts["DEF-001"] = 10
    defect_counts["DEF-002"] = 5
    defect_counts["DEF-003"] = 3
    defect_counts["DEF-004"] = 8

    # Appeler la fonction pour générer un rapport HTML avec l'image
    generate_html_report(defect_counts)

if __name__ == "__main__":
    main()
