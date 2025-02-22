pipeline {
    agent any

    stages {
        stage('Cloner le Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sirine-maatali/repo-visual.git'
            }
        }

        stage('Exécuter le script Python') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Générer et publier les graphiques') {
            steps {
                script {
                    def htmlContent = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
                    </head>
                    <body>
                        <div id="chart" style="width: 600px;height:400px;"></div>
                        <script>
                            fetch('output2.json')
                                .then(response => response.json())
                                .then(data => {
                                    var chart = echarts.init(document.getElementById('chart'));
                                    var seriesData = [];
                                    Object.keys(data).forEach(key => {
                                        seriesData.push({name: key, value: data[key].length});
                                    });
                                    var option = {
                                        title: { text: 'Distribution des Features', left: 'center' },
                                        tooltip: { trigger: 'item' },
                                        series: [{ name: 'Feature', type: 'pie', radius: '50%', data: seriesData }]
                                    };
                                    chart.setOption(option);
                                });
                        </script>
                    </body>
                    </html>
                    """
                    writeFile file: 'echarts.html', text: htmlContent
                }
            }
        }

        stage('Publier la page HTML') {
            steps {
                publishHTML(target: [
                    reportDir: '',
                    reportFiles: 'echarts.html',
                    reportName: 'Visualisation des Features'
                ])
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
