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

        stage('Exécuter le script Python pour générer le graphique et le rapport') {
            steps {
                script {
                    echo "Début de l'exécution du script Python pour générer le graphique et le rapport"

                    // Code Python pour générer le graphique
                    def pythonScript = '''
import matplotlib.pyplot as plt
import json

def generate_chart(data, file_name):
    # Exemple de structure de données
    feature_labels = data.keys()
    status_labels = list(set([status for statuses in data.values() for status in statuses.keys()]))
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for feature, status_map in data.items():
        counts = [status_map.get(status, 0) for status in status_labels]
        ax.bar(feature_labels, counts, label=feature)
    
    ax.set_xlabel('Features')
    ax.set_ylabel('Counts')
    ax.set_title('Feature Status Counts')
    ax.legend(title='Features')

    # Sauvegarder le graphique sous forme d'image
    image_path = 'feature_chart.png'
    plt.savefig(image_path)
    plt.close()

    return image_path

# Exemple de données à traiter
data = {
    'Feature 1': {'Pass': 10, 'Fail': 5},
    'Feature 2': {'Pass': 7, 'Fail': 3},
    'Feature 3': {'Pass': 5, 'Fail': 8}
}

# Générer et sauvegarder l'image
image_file = generate_chart(data, 'feature_chart.png')
print(f"Graphique généré : {image_file}")

# Générer le rapport HTML avec l'image
html_content = f'''
<html>
<head>
    <title>Test Execution - {params.FILE_NAME}</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; }}
        h1 {{ color: #2c3e50; }}
        img {{ max-width: 800px; margin: auto; }}
    </style>
</head>
<body>
    <h1>Test Execution Report</h1>
    <h2>Nom du fichier : {params.FILE_NAME}</h2>
    <img src="feature_chart.png" alt="Feature Status Chart">
</body>
</html>
'''

# Sauvegarder le fichier HTML
with open('report.html', 'w') as f:
    f.write(html_content)

print("Le fichier HTML a été généré avec succès.")
'''

                    // Écrire le script Python dans un fichier
                    writeFile file: 'generate_chart.py', text: pythonScript

                    // Exécuter le script Python pour générer le graphique et le rapport
                    bat 'python generate_chart.py'

                    // Vérifier si l'image et le fichier HTML ont été générés
                    if (!fileExists('feature_chart.png')) {
                        error "Le fichier image feature_chart.png n'a pas été généré !"
                    }
                    if (!fileExists('report.html')) {
                        error "Le fichier report.html n'a pas été généré !"
                    }
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
