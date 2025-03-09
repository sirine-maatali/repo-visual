document.addEventListener('DOMContentLoaded', function() {
    // Données statiques pour les graphiques (à remplacer par des données dynamiques si nécessaire)
    const featureLabels = ["Feature1", "Feature2", "Feature3"];
    const barDatasets = [
        {
            label: "PASS",
            backgroundColor: "#4CAF50",
            data: [10, 20, 30]
        },
        {
            label: "NOT EXECUTED",
            backgroundColor: "#A5D6A7",
            data: [5, 15, 25]
        }
    ];

    // Diagramme à barres horizontales
    var ctxGroupedBar = document.getElementById('groupedBarChart').getContext('2d');
    new Chart(ctxGroupedBar, {
        type: 'bar',
        data: {
            labels: featureLabels,
            datasets: barDatasets
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            plugins: {
                legend: { position: 'top' }
            },
            scales: {
                x: { stacked: false, beginAtZero: true,
                    ticks: {
                        font: {
                            size: 10 
                        }
                    } },
                y: { stacked: false, 
                    ticks: {
                        font: {
                            size: 10
                        }
                    } }
            }
        }
    });

    // ... (autres graphiques et fonctionnalités)
});

// Script pour générer le PDF
document.getElementById('generatePdfButton').addEventListener('click', function () {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF('p', 'mm', 'a4');
    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();
    const padding = 10; // Marge intérieure

    // Afficher temporairement toutes les lignes du tableau
    const table = document.getElementById('defectsTable');
    const rows = table.querySelectorAll('tbody tr');
    rows.forEach(row => (row.style.display = '')); // Afficher toutes les lignes

    // Fonction pour capturer et ajouter le contenu au PDF
    async function generatePdf() {
        let currentPage = 1;
        let positionY = padding;

        // Diviser le contenu en sections
        const sections = document.querySelectorAll('.pdf-section');
        for (let i = 0; i < sections.length; i++) {
            const section = sections[i];

            // Capturer la section avec html2canvas
            const canvas = await html2canvas(section, { scale: 2 });
            const imgData = canvas.toDataURL('image/png');
            const imgWidth = pageWidth - 2 * padding;
            const imgHeight = (canvas.height * imgWidth) / canvas.width;

            // Vérifier si la section dépasse la hauteur de la page
            if (positionY + imgHeight > pageHeight) {
                // Ajouter une nouvelle page si nécessaire
                doc.addPage();
                currentPage++;
                positionY = padding; // Réinitialiser la position Y
            }

            // Ajouter l'image de la section à la page actuelle
            doc.addImage(imgData, 'PNG', padding, positionY, imgWidth, imgHeight);
            positionY += imgHeight + padding; // Mettre à jour la position Y
        }

        // Sauvegarder le PDF
        doc.save('report.pdf');

        // Réappliquer la pagination après la génération du PDF
        showPage(1); // Revenir à la première page
        setActiveButton(paginationDiv.querySelector('button'));
    }

    generatePdf();
});