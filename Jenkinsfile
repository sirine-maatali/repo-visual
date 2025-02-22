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

        stage('Exécuter le script Python') {
            steps {
                script {
                    if (params.FILE_NAME == '') {
                        error("❌ Paramètre FILE_NAME requis.")
                    }
                    bat "C:\\Users\\SIRINE\\AppData\\Local\\Programs\\Python\\Python312\\python.ex app.py ${params.FILE_NAME}"
                }
            }
        }

        stage('Générer et publier les graphiques') {
            steps {
                script {
                    writeFile file: 'echarts.html', text: """
                    <html>
                    <head><script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script></head>
                    <body><div id="chart" style="width:600px;height:400px;"></div>
                    <script>
                        fetch('output2.json').then(res => res.json()).then(data => {
                            var chart = echarts.init(document.getElementById('chart'));
                            chart.setOption({ series: [{ type: 'pie', data: Object.keys(data).map(key => ({ name: key, value: data[key].length })) }] });
                        });
                    </script></body></html>
                    """
                }
            }
        }

        stage('Publier le rapport') {
            steps {
                publishHTML(target: [reportDir: '', reportFiles: 'echarts.html', reportName: 'Visualisation des Features'])
            }
        }

        stage('Générer un PDF') {
            steps {
                bat 'wkhtmltopdf echarts.html report.pdf'
                archiveArtifacts artifacts: 'report.pdf', fingerprint: true
            }
        }
    }
}
