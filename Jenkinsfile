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

// ****************************** hedha yemshi




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

//         stage('Vérifier Python') {
//             steps {
//                 script {
//                     bat 'where python'
//                     bat 'python --version'
//                 }
//             }
//         }

//         stage('Exécuter le script Python') {
//             steps {
//                 script {
//                     echo "Début de l'exécution du script Python"
                    
//                     // Exécuter et rediriger la sortie vers un fichier
//                     bat "python app.py ${params.FILE_NAME} output.json"
                    
//                     // Vérifier si output.json existe
//                     if (!fileExists('output.json')) {
//                         error "Le fichier output.json n'a pas été généré !"
//                     }

//                     // Lire le fichier JSON
//                     def jsonOutput = readFile('output.json').trim()
//                     echo "Sortie JSON récupérée : ${jsonOutput}"

//                     // Vérification si jsonOutput est vide
//                     if (!jsonOutput) {
//                         error "Le fichier JSON est vide !"
//                     }

//                     // Parsing JSON avec gestion des erreurs
//                     def jsonData
//                     try {
//                         jsonData = readJSON text: jsonOutput
//                         echo "JSON Parsé avec succès"
//                     } catch (Exception e) {
//                         error "Erreur lors du parsing du JSON : ${e.message}"
//                     }

//                     // Vérifier si jsonData est une liste
//                     if (!(jsonData instanceof List)) {
//                         error "Le JSON parsé n'est pas une liste d'objets !"
//                     }

//                     // Extraire les features uniques
//                     def features = jsonData.findAll { it.feature }
//                                           .collect { it.feature.toString().replaceAll("[\\[\\]']", "").trim() }
//                                           .unique()
//                     echo "Liste finale des features uniques : ${features}"

//                     def statuss = jsonData.findAll { it.status}
//                                           .collect { it.status.toString().trim() }
                                          
//                     echo "Liste finale des status uniques : ${statuss}"
//                     // Générer le contenu HTML
//                     def htmlContent = """
//                         <html>
//                         <head>
//                             <title>Test Execution - ${params.FILE_NAME}</title>
//                             <style>
//                                 body { font-family: Arial, sans-serif; margin: 20px; }
//                                 h1 { color: #2c3e50; text-align: center; }
//                                 h2 { color: #34495e; }
//                                 h3 { color: #16a085; }
//                                 pre { background: #f4f4f4; padding: 10px; border-radius: 5px; white-space: pre-wrap; word-wrap: break-word; }
//                                 .container { max-width: 800px; margin: auto; }
//                                 .feature-list { background: #ecf0f1; padding: 10px; border-radius: 5px; }
//                             </style>
//                         </head>
//                         <body>
//                             <div class="container">
//                                 <h1>Test Execution</h1>
//                                 <h2>Nom du fichier : ${params.FILE_NAME}</h2>
//                                 <h3>Features uniques :</h3>
//                                 <pre>${features.join("\n")}</pre>
//                                  <h3>Features uniques :</h3>
//                                 <pre>${statuss.join("\n")}</pre>
//                                 <h3>Résultat JSON :</h3>
//                                 <pre>${jsonOutput}</pre>
//                             </div>
//                         </body>
//                         </html>
//                     """

//                     writeFile file: 'report.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Vérifier génération du fichier HTML') {
//             steps {
//                 script {
//                     if (fileExists('report.html')) {
//                         echo 'Le fichier report.html a été généré avec succès !'
//                     } else {
//                         error 'Le fichier report.html n\'a pas été généré !'
//                     }
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
//             }
//         }

//         stage('Générer un PDF') {
//             steps {
//                 bat 'wkhtmltopdf report.html report.pdf'
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
                    echo "Début de l'exécution du script Python"
                    bat "python app.py ${params.FILE_NAME} output.json"
                    
                    if (!fileExists('output.json')) {
                        error "Le fichier output.json n'a pas été généré !"
                    }
                    
                    def jsonOutput = readFile('output.json').trim()
                    echo "Sortie JSON récupérée : ${jsonOutput}"
                    
                    if (!jsonOutput) {
                        error "Le fichier JSON est vide !"
                    }
                    
                    def jsonData
                    try {
                        jsonData = readJSON text: jsonOutput
                    } catch (Exception e) {
                        error "Erreur lors du parsing du JSON : ${e.message}"
                    }
                    
                    def featureData = [:]
                    jsonData.each { item ->
                        def feature = item.feature.toString().trim()
                        def status = item.status.toString().trim()
                        if (!featureData.containsKey(feature)) {
                            featureData[feature] = [:]
                        }
                        featureData[feature][status] = (featureData[feature][status] ?: 0) + 1
                    }
                    
                    def featureNames = featureData.keySet() as List
                    def statusTypes = featureData.values().collectMany { it.keySet() }.unique()
                    
                    def datasets = statusTypes.collect { status ->
                        [
                            label: status,
                            data: featureNames.collect { feature -> featureData[feature][status] ?: 0 },
                            backgroundColor: "#${Integer.toHexString((Math.random() * 0xFFFFFF).intValue()).padLeft(6, '0')}"
                        ]
                    }
                    
                    def htmlContent = """
                        <html>
                        <head>
                            <title>Test Execution - ${params.FILE_NAME}</title>
                            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
                        </head>
                        <body>
                            <h1>Visualisation des Features</h1>
                            <h2>Nom du fichier : ${params.FILE_NAME}</h2>
                            <canvas id="featureChart" width="800" height="400"></canvas>
                            <script>
                                const ctx = document.getElementById('featureChart').getContext('2d');
                                new Chart(ctx, {
                                    type: 'bar',
                                    data: {
                                        labels: ${featureNames},
                                        datasets: ${datasets}
                                    },
                                    options: {
                                        responsive: true,
                                        plugins: {
                                            legend: { position: 'top' }
                                        },
                                        scales: {
                                            y: { beginAtZero: true }
                                        }
                                    }
                                });
                            </script>
                        </body>
                        </html>
                    """
                    
                    writeFile file: 'report.html', text: htmlContent
                }
            }
        }

        stage('Publier le rapport') {
            steps {
                publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
            }
        }
    }
}
