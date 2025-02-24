// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX" ou "HGWXRAY-XXXX")')
//     }

//     stages {
//         stage('Cloner le Repo') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/sirine-maatali/repo-visual.git'
//             }
//         }

//         stage('Exécuter le script Python') {
//             steps {
//                script {
//                     // Utilise la valeur du paramètre FILE_NAME
//                     bat "C:\\Users\\SIRINE\\AppData\\Local\\Programs\\Python\\Python312\\python.exe app.py ${params.FILE_NAME}"
//                 }
//             }
//         }

//         stage('Générer et publier les graphiques') {
//             steps {
//                 script {
//                     def htmlContent = """
//                     <!DOCTYPE html>
//                     <html>
//                     <head>
//                         <script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
//                     </head>
//                     <body>
//                         <div id="chart" style="width: 600px;height:400px;"></div>
//                         <script>
//                             fetch('output2.json')
//                                 .then(response => response.json())
//                                 .then(data => {
//                                     var chart = echarts.init(document.getElementById('chart'));
//                                     var seriesData = [];
//                                     Object.keys(data).forEach(key => {
//                                         seriesData.push({name: key, value: data[key].length});
//                                     });
//                                     var option = {
//                                         title: { text: 'Distribution des Features', left: 'center' },
//                                         tooltip: { trigger: 'item' },
//                                         series: [{ name: 'Feature', type: 'pie', radius: '50%', data: seriesData }]
//                                     };
//                                     chart.setOption(option);
//                                 });
//                         </script>
//                     </body>
//                     </html>
//                     """
//                     writeFile file: 'echarts.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Publier la page HTML') {
//             steps {
//                 publishHTML(target: [
//                     reportDir: '',
//                     reportFiles: 'echarts.html',
//                     reportName: 'Visualisation des Features'
//                 ])
//             }
//         }

//         stage('Générer un PDF') {
//             steps {
//                 bat 'wkhtmltopdf echarts.html report.pdf'
//                 archiveArtifacts artifacts: 'report.pdf', fingerprint: true
//             }
//         }
//     }
// }
// hedhi temshiiiiiiii ***************

// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX" ou "HGWXRAY-XXXX")')
//     }

//     stages {
//         stage('Cloner le Repo') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/sirine-maatali/repo-visual.git'
//             }
//         }
//     stage('Vérifier Python') {
//         steps {
//             script {
//                 bat 'where python'
//                 bat 'python --version'
//             }
//         }
//     }
//         stage('Exécuter le script Python') {
//             steps {
//                 script {
//                     if (params.FILE_NAME == '') {
//                         error(" Paramètre FILE_NAME requis.")
//                     }
//                     bat "python app.py ${params.FILE_NAME}"
//                 }
//             }
//         }

//         stage('Générer et publier les graphiques') {
//             steps {
//                 script {
//                     writeFile file: 'echarts.html', text: """
//                     <html>
//                     <head><script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script></head>
//                     <body><div id="chart" style="width:600px;height:400px;"></div>
//                     <script>
//                         fetch('output2.json').then(res => res.json()).then(data => {
//                             var chart = echarts.init(document.getElementById('chart'));
//                             chart.setOption({ series: [{ type: 'pie', data: Object.keys(data).map(key => ({ name: key, value: data[key].length })) }] });
//                         });
//                     </script></body></html>
//                     """
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'echarts.html', reportName: 'Visualisation des Features'])
//             }
//         }

//         stage('Générer un PDF') {
//             steps {
//                 bat 'wkhtmltopdf echarts.html report.pdf'
//                 archiveArtifacts artifacts: 'report.pdf', fingerprint: true
//             }
//         }
//     }
// }



// ********************************

// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX" ou "HGWXRAY-XXXX")')
//     }

//     stages {
//         stage('Cloner le Repo') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/sirine-maatali/repo-visual.git'
//             }
//         }
//     stage('Vérifier Python') {
//         steps {
//             script {
//                 bat 'where python'
//                 bat 'python --version'
//             }
//         }
//     }
//         stage('Exécuter le script Python') {
//             steps {
//                 script {
//                     if (params.FILE_NAME == '') {
//                         error(" Paramètre FILE_NAME requis.")
//                     }
//                     bat "python app.py ${params.FILE_NAME}"
//                 }
//             }
//         }

//         stage('Générer et publier les graphiques') {
//             steps {
//                 script {
//                     writeFile file: 'echarts.html', text: """
//                     <html>
//                     <head><script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script></head>
//                     <body><div id="chart" style="width:600px;height:400px;"></div>
//                     <script>
//                         fetch('output2.json').then(res => res.json()).then(data => {
//                             var chart = echarts.init(document.getElementById('chart'));
//                             chart.setOption({ series: [{ type: 'pie', data: Object.keys(data).map(key => ({ name: key, value: data[key].length })) }] });
//                         });
//                     </script></body></html>
//                     """
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'echarts.html', reportName: 'Visualisation des Features'])
//             }
//         }

//         stage('Générer un PDF') {
//             steps {
//                 bat 'wkhtmltopdf echarts.html report.pdf'
//                 archiveArtifacts artifacts: 'report.pdf', fingerprint: true
//             }
//         }
//     }
// }


pipeline {
    agent any

    parameters {
        string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX" ou "HGWXRAY-XXXX")')
    }

stages {
    stage('Cloner le Repo') {
        steps {
            git branch: 'main', url: 'https://github.com/sirine-maatali/repo-visual.git'
        }
    }

    stage('Vérifier Python') {
        steps {
            script {
                bat 'where python'
                bat 'python --version'
            }
        }
    }

    // stage('Exécuter le script Python') {
    //     steps {
    //         script {
    //             if (params.FILE_NAME == '') {
    //                 error("Paramètre FILE_NAME requis.")
    //             }
    //             try {
    //                 def jsonData = bat(script: "python app.py ${params.FILE_NAME}", returnStdout: true).trim()
    //                 if (!jsonData || jsonData.startsWith("{\"error\":")) {
    //                     error("Erreur lors de l'exécution du script Python : ${jsonData}")
    //                 }
    //                 writeFile file: 'output.json', text: jsonData
    //             } catch (Exception e) {
    //                 error("Échec de l'exécution Python : ${e.getMessage()}")
    //             }
    //         }
    //     }
    // }


stage('Exécuter le script Python') {
    steps {
        script {
            // Exécution du script Python et récupération de la sortie
            def jsonOutput = bat(script: "python app.py ${params.FILE_NAME}", returnStdout: true).trim()
            echo "Sortie JSON : ${jsonOutput}"

            // Générer le fichier HTML avec les données
            writeFile file: 'echarts.html', text: """
            <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
                <style>
                    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                </style>
            </head>
            <body>
                <h2>Visualisation des Données</h2>
                <div id="chart" style="width:600px;height:400px;"></div>

                <h3>Données brutes :</h3>
                <table id="dataTable">
                    <thead>
                        <tr>
                            <th>Test Key</th>
                            <th>Feature</th>
                            <th>Status</th>
                            <th>Defects</th>
                        </tr>
                    </thead>
                    <tbody></tbody>
                </table>

                <script>
                    // Injection des données JSON dynamiquement
                    let data = ${jsonOutput};

                    if (!Array.isArray(data)) {
                        document.body.innerHTML = "<h3>Erreur : Données JSON invalides</h3>";
                        throw new Error("Données JSON invalides");
                    }

                    // Graphique
                    var chart = echarts.init(document.getElementById('chart'));
                    chart.setOption({ 
                        title: { text: 'Répartition des Features' },
                        tooltip: { trigger: 'item' },
                        legend: { top: '5%' },
                        series: [{
                            type: 'pie',
                            data: data.map(item => ({ name: item.feature, value: 1 })),
                        }]
                    });

                    // Tableau des données
                    let tableBody = document.querySelector("#dataTable tbody");
                    data.forEach(item => {
                        let row = `<tr>
                            <td>${item.testKey}</td>
                            <td>${item.feature}</td>
                            <td>${item.status}</td>
                            <td>${item.defects.length > 0 ? item.defects.collect { it.id }.join(", ") : "Aucun"}</td>
                        </tr>`;
                        tableBody.innerHTML += row;
                    });
                </script>
            </body>
            </html>
            """
            echo "Fichier echarts.html généré avec succès !"
        }
    }
}

stage('Vérifier génération du fichier HTML') {
    steps {
        script {
            // Vérifier si le fichier echarts.html existe
            if (fileExists('echarts.html')) {
                echo 'Le fichier echarts.html a été généré avec succès !'
            } else {
                error 'Le fichier echarts.html n\'a pas été généré !'
            }
        }
    }
}

stage('Publier le rapport') {
    steps {
        // Publier le fichier HTML généré comme rapport Jenkins
        publishHTML(target: [reportDir: '', reportFiles: 'echarts.html', reportName: 'Visualisation des Features'])
    }
}

stage('Générer un PDF') {
    steps {
        // Convertir le fichier HTML en PDF
        bat 'wkhtmltopdf echarts.html report.pdf'
        // Archiver le PDF généré
        archiveArtifacts artifacts: 'report.pdf', fingerprint: true
    }
}
