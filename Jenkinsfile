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

        stage('Exécuter le script Python') {
            steps {
                script {
                    // Exécution du script Python et récupération de la sortie JSON
                    def jsonOutput = bat(script: "python app.py ${params.FILE_NAME}", returnStdout: true).trim()

                    // Affichage de la sortie JSON dans les logs
                    echo "Sortie JSON : ${jsonOutput}"

                    // Vérification si la sortie est vide
                    if (!jsonOutput) {
                        error "La sortie JSON est vide !"
                    }

                    // Créer le contenu HTML avec le JSON et le titre
                    def htmlContent = """
                        <html>
                        <head>
                            <title>Test Execution - ${params.FILE_NAME}</title>
                            <style>
                                body { font-family: Arial, sans-serif; margin: 20px; }
                                h1 { color: #2c3e50; text-align: center; }
                                h2 { color: #34495e; }
                                h3 { color: #16a085; }
                                pre { background: #f4f4f4; padding: 10px; border-radius: 5px; white-space: pre-wrap; word-wrap: break-word; }
                                .container { max-width: 800px; margin: auto; }
                            </style>
                        </head>
                        <body>
                            <div class="container">
                                <h1>Test Execution</h1>
                                <h2>Nom du fichier : ${params.FILE_NAME}</h2>
                                <h3>Résultat JSON :</h3>
                                <pre>${jsonOutput}</pre>  <!-- Afficher les données JSON brutes -->
                            </div>
                        </body>
                        </html>
                    """

                    // Sauvegarder ce contenu HTML dans un fichier pour le publier
                    writeFile file: 'report.html', text: htmlContent
                }
            }
        }

        stage('Vérifier génération du fichier HTML') {
            steps {
                script {
                    if (fileExists('report.html')) {
                        echo 'Le fichier report.html a été généré avec succès !'
                    } else {
                        error 'Le fichier report.html n\'a pas été généré !'
                    }
                }
            }
        }

        stage('Publier le rapport') {
            steps {
                publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
            }
        }

        stage('Générer un PDF') {
            steps {
                bat 'wkhtmltopdf report.html report.pdf'
                archiveArtifacts artifacts: 'report.pdf', fingerprint: true
            }
        }
    }
}
