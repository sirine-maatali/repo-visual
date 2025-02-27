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


//  hedha yaffichi *******************************




// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX")')
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
//                     bat "python app.py ${params.FILE_NAME} output.json"

//                     if (!fileExists('output.json')) {
//                         error "Le fichier output.json n'a pas été généré !"
//                     }

//                     def jsonOutput = readFile('output.json').trim()
//                     if (!jsonOutput) {
//                         error "Le fichier JSON est vide !"
//                     }

//                     def jsonData = readJSON text: jsonOutput
                    
//                     def statusCounts = [:]
//                     def defectsData = []
//                     jsonData.each { entry ->
//                         def feature = entry.feature.toString().trim()
//                         def status = entry.status.toString().trim()
                        
//                         if (!statusCounts[feature]) {
//                             statusCounts[feature] = [:]
//                         }
//                         statusCounts[feature][status] = (statusCounts[feature][status] ?: 0) + 1
                        
//                         if (status == 'FAIL' || status == 'BLOCKED') {
//                             entry.defects.each { defect ->
//                                 defectsData.add("<tr><td>${defect.id}</td><td>${defect.summary}</td><td>${defect.priority}</td></tr>")
//                             }
//                         }
//                     }
                    
//                     def featureLabels = statusCounts.keySet().collect { "\"${it}\"" }.join(", ")
//                     def datasets = []
//                     def statusTypes = statusCounts.values().collectMany { it.keySet() }.unique()
                    
//                     statusTypes.each { status ->
//                         def data = statusCounts.collect { it.value[status] ?: 0 }
//                         datasets.add("{label: \"${status}\", backgroundColor: getRandomColor(), data: [${data.join(", ")}]}")
//                     }
                    
//                     def pieData = statusCounts.collectEntries { feature, statuses ->
//                         [(feature): statuses.collect { k, v -> v }.sum()]
//                     }
//                     def pieLabels = pieData.keySet().collect { "\"${it}\"" }.join(", ")
//                     def pieValues = pieData.values().join(", ")
                    
//                     def htmlContent = """
//                         <html>
//                         <head>
//                             <title>Test Execution - ${params.FILE_NAME}</title>
//                             <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
//                             <script>
//                                 function getRandomColor() {
//                                     return '#' + Math.floor(Math.random()*16777215).toString(16);
//                                 }
//                             </script>
//                         </head>
//                         <body>
//                             <h1>Test Execution</h1>
//                             <h2>Nom du fichier : ${params.FILE_NAME}</h2>
//                             <canvas id="barChart"></canvas>
//                             <canvas id="pieChart"></canvas>
//                             <h2>Defects (FAIL & BLOCKED)</h2>
//                             <table border="1">
//                                 <tr><th>ID</th><th>Summary</th><th>Priority</th></tr>
//                                 ${defectsData.join("\n")}
//                             </table>
//                             <script>
//                                 var ctxBar = document.getElementById('barChart').getContext('2d');
//                                 new Chart(ctxBar, {
//                                     type: 'bar',
//                                     data: {
//                                         labels: [${featureLabels}],
//                                         datasets: [${datasets.join(", ")}]
//                                     },
//                                     options: {
//                                         responsive: true,
//                                         plugins: {
//                                             legend: { position: 'top' }
//                                         },
//                                         scales: {
//                                             x: { stacked: true },
//                                             y: { stacked: true, beginAtZero: true }
//                                         }
//                                     }
//                                 });
                                
//                                 var ctxPie = document.getElementById('pieChart').getContext('2d');
//                                 new Chart(ctxPie, {
//                                     type: 'pie',
//                                     data: {
//                                         labels: [${pieLabels}],
//                                         datasets: [{
//                                             data: [${pieValues}],
//                                             backgroundColor: [getRandomColor(), getRandomColor(), getRandomColor()]
//                                         }]
//                                     }
//                                 });
//                             </script>
//                         </body>
//                         </html>
//                     """

//                     writeFile file: 'report.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
//             }
//         }
//     }
// }


// ***********



// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX")')
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
//                     bat "python app.py ${params.FILE_NAME} output.json"

//                     if (!fileExists('output.json')) {
//                         error "Le fichier output.json n'a pas été généré !"
//                     }

//                     def jsonOutput = readFile('output.json').trim()
//                     if (!jsonOutput) {
//                         error "Le fichier JSON est vide !"
//                     }

//                     def jsonData = readJSON text: jsonOutput
                    
//                     def statusCounts = [:]
//                     def defectsData = []
//                     jsonData.each { entry ->
//                         def feature = entry.feature.toString().trim()
//                         def status = entry.status.toString().trim()
                        
//                         if (!statusCounts[feature]) {
//                             statusCounts[feature] = [:]
//                         }
//                         statusCounts[feature][status] = (statusCounts[feature][status] ?: 0) + 1
                        
//                         if (status == 'FAIL' || status == 'BLOCKED') {
//                             entry.defects.each { defect ->
//                                 defectsData.add("<tr><td>${defect.id}</td><td>${defect.summary}</td><td>${defect.priority}</td></tr>")
//                             }
//                         }
//                     }
                    
//                     def featureLabels = statusCounts.keySet().collect { "\"${it}\"" }.join(", ")
//                     def datasets = []
//                     def statusTypes = statusCounts.values().collectMany { it.keySet() }.unique()
                    
//                     // Couleurs fixes pour les barres (nuances de vert)
//                     def greenShades = ['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9', '#66BB6A', '#388E3C']
                    
//                     statusTypes.eachWithIndex { status, index ->
//                         def data = statusCounts.collect { it.value[status] ?: 0 }
//                         datasets.add("""
//                             {
//                                 label: "${status}",
//                                 backgroundColor: "${greenShades[index % greenShades.size()]}",
//                                 data: [${data.join(", ")}]
//                             }
//                         """)
//                     }
                    
//                     def pieData = statusCounts.collectEntries { feature, statuses ->
//                         [(feature): statuses.collect { k, v -> v }.sum()]
//                     }
//                     def pieLabels = pieData.keySet().collect { "\"${it}\"" }.join(", ")
//                     def pieValues = pieData.values().join(", ")
                    
//                     def htmlContent = """
//                         <html>
//                         <head>
//                             <title>Test Execution - ${params.FILE_NAME}</title>
//                             <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
//                             <style>
//                                 body {
//                                     font-family: Arial, sans-serif;
//                                     margin: 20px;
//                                 }
//                                 h1, h2 {
//                                     color: #2E7D32;
//                                 }
//                                 table {
//                                     width: 100%;
//                                     border-collapse: collapse;
//                                     margin-top: 20px;
//                                 }
//                                 table, th, td {
//                                     border: 1px solid #ddd;
//                                 }
//                                 th, td {
//                                     padding: 12px;
//                                     text-align: left;
//                                 }
//                                 th {
//                                     background-color: #4CAF50;
//                                     color: white;
//                                 }
//                                 tr:nth-child(even) {
//                                     background-color: #f2f2f2;
//                                 }
//                                 tr:hover {
//                                     background-color: #ddd;
//                                 }
//                                 canvas {
//                                     margin-top: 20px;
//                                     margin-bottom: 40px;
//                                     max-width: 800px;
//                                 }
//                                 .chart-container {
//                                     width: 50%;
//                                     margin: 0 auto;
//                                 }
//                             </style>
//                         </head>
//                         <body>
//                             <h1>Test Execution</h1>
//                             <h2>Nom du fichier : ${params.FILE_NAME}</h2>
//                             <div class="chart-container">
//                                 <canvas id="barChart"></canvas>
//                             </div>
//                             <div class="chart-container">
//                                 <canvas id="pieChart"></canvas>
//                             </div>
//                             <h2>Defects (FAIL & BLOCKED)</h2>
//                             <table>
//                                 <tr><th>ID</th><th>Summary</th><th>Priority</th></tr>
//                                 ${defectsData.join("\n")}
//                             </table>
//                             <script>
//                                 document.addEventListener('DOMContentLoaded', function() {
//                                     // Bar Chart
//                                     var ctxBar = document.getElementById('barChart').getContext('2d');
//                                     new Chart(ctxBar, {
//                                         type: 'bar',
//                                         data: {
//                                             labels: [${featureLabels}],
//                                             datasets: [${datasets.join(", ")}]
//                                         },
//                                         options: {
//                                             responsive: true,
//                                             plugins: {
//                                                 legend: { position: 'top' }
//                                             },
//                                             scales: {
//                                                 x: { stacked: true },
//                                                 y: { stacked: true, beginAtZero: true }
//                                             }
//                                         }
//                                     });
                                    
//                                     // Pie Chart
//                                     var ctxPie = document.getElementById('pieChart').getContext('2d');
//                                     new Chart(ctxPie, {
//                                         type: 'pie',
//                                         data: {
//                                             labels: [${pieLabels}],
//                                             datasets: [{
//                                                 data: [${pieValues}],
//                                                 backgroundColor: [${greenShades.collect { "\"${it}\"" }.join(", ")}]
//                                             }]
//                                         },
//                                         options: {
//                                             responsive: true,
//                                             plugins: {
//                                                 legend: { position: 'top' }
//                                             }
//                                         }
//                                     });
//                                 });
//                             </script>
//                         </body>
//                         </html>
//                     """

//                     writeFile file: 'report.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
//             }
//         }
//     }
// }



// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX")')
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
//                     bat "python app.py ${params.FILE_NAME} output.json"

//                     if (!fileExists('output.json')) {
//                         error "Le fichier output.json n'a pas été généré !"
//                     }

//                     def jsonOutput = readFile('output.json').trim()
//                     if (!jsonOutput) {
//                         error "Le fichier JSON est vide !"
//                     }

//                     def jsonData = readJSON text: jsonOutput
                    
//                     def statusCounts = [:]
//                     def defectsData = []
//                     jsonData.each { entry ->
//                         def feature = entry.feature.toString().trim()
//                         def status = entry.status.toString().trim()
                        
//                         if (!statusCounts[feature]) {
//                             statusCounts[feature] = [:]
//                         }
//                         statusCounts[feature][status] = (statusCounts[feature][status] ?: 0) + 1
                        
//                         if (status == 'FAIL' || status == 'BLOCKED') {
//                             entry.defects.each { defect ->
//                                 defectsData.add("<tr><td>${defect.id}</td><td>${defect.summary}</td><td>${defect.priority}</td></tr>")
//                             }
//                         }
//                     }
                    
//                     def featureLabels = statusCounts.keySet().collect { it }.join(", ")
//                     def datasets = []
//                     def statusTypes = statusCounts.values().collectMany { it.keySet() }.unique()
                    
//                     // Couleurs fixes pour les barres (nuances de vert)
//                     def greenShades = ['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9']
                    
//                     statusTypes.eachWithIndex { status, index ->
//                         def data = statusCounts.collect { it.value[status] ?: 0 }
//                         datasets.add("""
//                             {
//                                 name: '${status}',
//                                 type: 'bar',
//                                 data: [${data.join(", ")}],
//                                 itemStyle: { color: '${greenShades[index % greenShades.size()]}' }
//                             }
//                         """)
//                     }
                    
//                     def pieData = statusCounts.collectEntries { feature, statuses ->
//                         [(feature): statuses.collect { k, v -> v }.sum()]
//                     }
//                     def pieLabels = pieData.keySet().collect { it }.join(", ")
//                     def pieValues = pieData.values().join(", ")
                    
//                     def htmlContent = """
//                         <html>
//                         <head>
//                             <title>Test Execution - ${params.FILE_NAME}</title>
//                             <script src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js"></script>
//                             <style>
//                                 body {
//                                     font-family: Arial, sans-serif;
//                                     margin: 20px;
//                                 }
//                                 h1, h2 {
//                                     color: #2E7D32;
//                                 }
//                                 table {
//                                     width: 100%;
//                                     border-collapse: collapse;
//                                     margin-top: 20px;
//                                 }
//                                 table, th, td {
//                                     border: 1px solid #ddd;
//                                 }
//                                 th, td {
//                                     padding: 12px;
//                                     text-align: left;
//                                 }
//                                 th {
//                                     background-color: #4CAF50;
//                                     color: white;
//                                 }
//                                 tr:nth-child(even) {
//                                     background-color: #f2f2f2;
//                                 }
//                                 tr:hover {
//                                     background-color: #ddd;
//                                 }
//                                 .chart-container {
//                                     width: 100%;
//                                     height: 400px;
//                                     margin: 20px 0;
//                                 }
//                             </style>
//                         </head>
//                         <body>
//                             <h1>Test Execution</h1>
//                             <h2>Nom du fichier : ${params.FILE_NAME}</h2>
//                             <div id="barChart" class="chart-container"></div>
//                             <div id="pieChart" class="chart-container"></div>
//                             <h2>Defects (FAIL & BLOCKED)</h2>
//                             <table>
//                                 <tr><th>ID</th><th>Summary</th><th>Priority</th></tr>
//                                 ${defectsData.join("\n")}
//                             </table>
//                             <script>
//                                 // Bar Chart
//                                 var barChart = echarts.init(document.getElementById('barChart'));
//                                 var barOption = {
//                                     title: { text: 'Statut des Features' },
//                                     tooltip: { trigger: 'axis' },
//                                     legend: { data: [${statusTypes.collect { "'${it}'" }.join(", ")}] },
//                                     xAxis: { type: 'category', data: [${featureLabels.split(", ").collect { "'${it}'" }.join(", ")}] },
//                                     yAxis: { type: 'value' },
//                                     series: [${datasets.join(", ")}]
//                                 };
//                                 barChart.setOption(barOption);
                                
//                                 // Pie Chart
//                                 var pieChart = echarts.init(document.getElementById('pieChart'));
//                                 var pieOption = {
//                                     title: { text: 'Répartition des Features' },
//                                     tooltip: { trigger: 'item' },
//                                     series: [{
//                                         type: 'pie',
//                                         data: [${pieLabels.split(", ").collect { label, i -> "{ value: ${pieValues.split(", ")[i]}, name: '${label}' }" }.join(", ")}],
//                                         itemStyle: { color: function(params) { return ['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9'][params.dataIndex]; } }
//                                     }]
//                                 };
//                                 pieChart.setOption(pieOption);
//                             </script>
//                         </body>
//                         </html>
//                     """

//                     writeFile file: 'report.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
//             }
//         }
//     }
// }

// hedhi fiha les visualisations

// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX")')
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
//                     bat "python app.py ${params.FILE_NAME} output.json"

//                     if (!fileExists('output.json')) {
//                         error "Le fichier output.json n'a pas été généré !"
//                     }

//                     def jsonOutput = readFile('output.json').trim()
//                     if (!jsonOutput) {
//                         error "Le fichier JSON est vide !"
//                     }

//                     def jsonData = readJSON text: jsonOutput
                    
//                     def statusCounts = [:]
//                     def featureStatusData = [:]
//                     def defectsData = []
//                     jsonData.each { entry ->
//                         def feature = entry.feature.toString().trim()
//                         def status = entry.status.toString().trim()
//                         def priority = entry.defects?.priority?.toString()?.trim()?.toLowerCase() ?: ""
                        
//                         // Initialisation de la structure de données pour la feature si elle n'existe pas encore
//                         if (!featureStatusData[feature]) {
//                             featureStatusData[feature] = [PASS: 0, NOTEXECUTED: 0, NOKMINOR: 0, NOKMAJOR: 0]
//                         }
                        
//                         // Mise à jour des compteurs en fonction du statut et de la priorité
//                         if (status == 'PASS') {
//                             featureStatusData[feature].PASS++
//                         } else if (status == 'ABORTED' || status == 'TODO') {
//                             featureStatusData[feature].NOTEXECUTED++
//                         } else if (status == 'FAIL' || status == 'BLOCKED') {
//                             if (priority =='[medium]'|| status == '[high]') {
//                                 featureStatusData[feature].NOKMINOR++
//                             } else if (priority == '[very high]' || priority == '[blocker]') {
//                                 featureStatusData[feature].NOKMAJOR++
//                             }
//                         }
                        
//                         if (!statusCounts[feature]) {
//                             statusCounts[feature] = [:]
//                         }
//                         statusCounts[feature][status] = (statusCounts[feature][status] ?: 0) + 1
                        
//                         if (status == 'FAIL' || status == 'BLOCKED') {
//                             entry.defects.each { defect ->
//                                 defectsData.add("<tr><td>${defect.id}</td><td>${defect.summary}</td><td>${defect.priority}</td></tr>")
//                             }
//                         }
//                     }
                    
//                     def featureLabels = statusCounts.keySet().collect { "\"${it}\"" }.join(", ")
//                     def datasets = []
//                     def statusTypes = statusCounts.values().collectMany { it.keySet() }.unique()
                    
//                     // Couleurs fixes pour les barres (nuances de vert)
//                     def greenShades = ['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9', '#66BB6A', '#388E3C']
                    
//                     statusTypes.eachWithIndex { status, index ->
//                         def data = statusCounts.collect { it.value[status] ?: 0 }
//                         datasets.add("""
//                             {
//                                 label: "${status}",
//                                 backgroundColor: "${greenShades[index % greenShades.size()]}",
//                                 data: [${data.join(", ")}]
//                             }
//                         """)
//                     }
                    
//                     def pieData = statusCounts.collectEntries { feature, statuses ->
//                         [(feature): statuses.collect { k, v -> v }.sum()]
//                     }
//                     def pieLabels = pieData.keySet().collect { "\"${it}\"" }.join(", ")
//                     def pieValues = pieData.values().join(", ")
                    
//                     def featureStatusLabels = featureStatusData.keySet().collect { "\"${it}\"" }.join(", ")
//                     def featureStatusDatasets = [
//                         """
//                             {
//                                 label: "PASS",
//                                 backgroundColor: "#4CAF50",
//                                 data: [${featureStatusData.collect { it.value.PASS }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOT EXECUTED",
//                                 backgroundColor: "#FFEB3B",
//                                 data: [${featureStatusData.collect { it.value.NOTEXECUTED }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOK MINOR",
//                                 backgroundColor: "#FF9800",
//                                 data: [${featureStatusData.collect { it.value.NOKMINOR }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOK MAJOR",
//                                 backgroundColor: "#F44336",
//                                 data: [${featureStatusData.collect { it.value.NOKMAJOR }.join(", ")}]
//                             }
//                         """
//                     ]

//                     def htmlContent = """
//                         <html>
//                         <head>
//                             <title>Test Execution - ${params.FILE_NAME}</title>
//                             <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
//                             <style>
//                                 body {
//                                     font-family: Arial, sans-serif;
//                                     margin: 20px;
//                                 }
//                                 h1, h2 {
//                                     color: #2E7D32;
//                                 }
//                                 table {
//                                     width: 100%;
//                                     border-collapse: collapse;
//                                     margin-top: 20px;
//                                 }
//                                 table, th, td {
//                                     border: 1px solid #ddd;
//                                 }
//                                 th, td {
//                                     padding: 12px;
//                                     text-align: left;
//                                 }
//                                 th {
//                                     background-color: #4CAF50;
//                                     color: white;
//                                 }
//                                 tr:nth-child(even) {
//                                     background-color: #f2f2f2;
//                                 }
//                                 tr:hover {
//                                     background-color: #ddd;
//                                 }
//                                 canvas {
//                                     margin-top: 20px;
//                                     margin-bottom: 40px;
//                                     max-width: 800px;
//                                 }
//                                 .chart-container {
//                                     width: 50%;
//                                     margin: 0 auto;
//                                 }
//                             </style>
//                         </head>
//                         <body>
//                             <h1>Test Execution</h1>
//                             <h2>Nom du fichier : ${params.FILE_NAME}</h2>
//                             <div class="chart-container">
//                                 <canvas id="barChart"></canvas>
//                             </div>
//                             <div class="chart-container">
//                                 <canvas id="pieChart"></canvas>
//                             </div>
//                             <div class="chart-container">
//                                 <canvas id="featureStatusChart"></canvas>
//                             </div>
//                             <h2>Defects (FAIL & BLOCKED)</h2>
//                             <table>
//                                 <tr><th>ID</th><th>Summary</th><th>Priority</th></tr>
//                                 ${defectsData.join("\n")}
//                             </table>
//                             <script>
//                                 document.addEventListener('DOMContentLoaded', function() {
//                                     // Bar Chart
//                                     var ctxBar = document.getElementById('barChart').getContext('2d');
//                                     new Chart(ctxBar, {
//                                         type: 'bar',
//                                         data: {
//                                             labels: [${featureLabels}],
//                                             datasets: [${datasets.join(", ")}]
//                                         },
//                                         options: {
//                                             responsive: true,
//                                             plugins: {
//                                                 legend: { position: 'top' }
//                                             },
//                                             scales: {
//                                                 x: { stacked: true },
//                                                 y: { stacked: true, beginAtZero: true }
//                                             }
//                                         }
//                                     });
                                    
//                                     // Pie Chart
//                                     var ctxPie = document.getElementById('pieChart').getContext('2d');
//                                     new Chart(ctxPie, {
//                                         type: 'pie',
//                                         data: {
//                                             labels: [${pieLabels}],
//                                             datasets: [{
//                                                 data: [${pieValues}],
//                                                 backgroundColor: [${greenShades.collect { "\"${it}\"" }.join(", ")}]
//                                             }]
//                                         },
//                                         options: {
//                                             responsive: true,
//                                             plugins: {
//                                                 legend: { position: 'top' }
//                                             }
//                                         }
//                                     });
                                    
//                                     // Feature Status Chart
//                                     var ctxFeatureStatus = document.getElementById('featureStatusChart').getContext('2d');
//                                     new Chart(ctxFeatureStatus, {
//                                         type: 'bar',
//                                         data: {
//                                             labels: [${featureStatusLabels}],
//                                             datasets: [${featureStatusDatasets.join(", ")}]
//                                         },
//                                         options: {
//                                             responsive: true,
//                                             plugins: {
//                                                 legend: { position: 'top' }
//                                             },
//                                             scales: {
//                                                 x: { stacked: true },
//                                                 y: { stacked: true, beginAtZero: true }
//                                             }
//                                         }
//                                     });
//                                 });
//                             </script>
//                         </body>
//                         </html>
//                     """

//                     writeFile file: 'report.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Convertir en PDF') {
//             steps {
//                 script {
//                     // Assurez-vous que wkhtmltopdf est installé sur l'agent Jenkins
//                     bat 'wkhtmltopdf --version'
                    
//                     // Convertir le fichier HTML en PDF
//                     bat 'wkhtmltopdf report.html report.pdf'
                    
//                     // Vérifier que le fichier PDF a été généré
//                     if (!fileExists('report.pdf')) {
//                         error "Le fichier report.pdf n'a pas été généré !"
//                     }
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
                
//                 // Publier le fichier PDF
//                 archiveArtifacts artifacts: 'report.pdf', fingerprint: true
//             }
//         }
//     }
// }



// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX")')
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
//                     bat "python app.py ${params.FILE_NAME} output.json"

//                     if (!fileExists('output.json')) {
//                         error "Le fichier output.json n'a pas été généré !"
//                     }

//                     def jsonOutput = readFile('output.json').trim()
//                     if (!jsonOutput) {
//                         error "Le fichier JSON est vide !"
//                     }

//                     def jsonData = readJSON text: jsonOutput
                    
//                def featureStatusData = [:]
//                     jsonData.each { entry ->
//                         def feature = entry.feature.toString().trim()
//                         def status = entry.status.toString().trim()
//                         def priority = entry.defects?.priority?.toString()?.trim()?.toLowerCase() ?: ""
                        
//                         // Affichage des valeurs initiales
//                         echo "hedhiiiiiiiiiii priority: ${priority}"
//                         echo "hedhiiiiiiiiiii status: ${status}"
//                         echo "hedhiiiiiiiiiii feature: ${feature}"
                        
//                         // Initialisation de la structure de données pour la feature si elle n'existe pas encore
//                         if (!featureStatusData[feature]) {
//                             featureStatusData[feature] = [PASS: 0, NOTEXECUTED: 0, NOKMINOR: 0, NOKMAJOR: 0]
//                             echo "Initialisation de la feature: ${feature} avec les valeurs par défaut: ${featureStatusData[feature]}"
//                         }
                        
//                         // Mise à jour des compteurs en fonction du statut et de la priorité
//                         if (status == 'PASS') {
//                             featureStatusData[feature].PASS++
//                             echo "Statut PASS détecté pour la feature: ${feature}. Nouveau compte PASS: ${featureStatusData[feature].PASS}"
//                         } else if (status == 'ABORTED' || status == 'TODO') {
//                             featureStatusData[feature].NOTEXECUTED++
//                             echo "Statut ABORTED ou TODO détecté pour la feature: ${feature}. Nouveau compte NOTEXECUTED: ${featureStatusData[feature].NOTEXECUTED}"
//                         } else if (status == 'FAIL' || status == 'BLOCKED') {
//                             if (priority =='[medium]'|| status == '[high]') {
//                                 featureStatusData[feature].NOKMINOR++
//                                 echo "Statut FAIL ou BLOCKED avec priorité ${priority} détecté pour la feature: ${feature}. Nouveau compte NOKMINOR: ${featureStatusData[feature].NOKMINOR}"
//                             } else if (priority == '[very high]' || priority == '[blocker]') {
//                                 featureStatusData[feature].NOKMAJOR++
//                                 echo "Statut FAIL ou BLOCKED avec priorité ${priority} détecté pour la feature: ${feature}. Nouveau compte NOKMAJOR: ${featureStatusData[feature].NOKMAJOR}"
//                             }
//                         }
                        
//                         // Affichage de l'état actuel de featureStatusData après chaque itération
//                         echo "État actuel de featureStatusData après traitement de la feature ${feature}: ${featureStatusData}"
//                 }

//                     def featureStatusLabels = featureStatusData.keySet().collect { "\"${it}\"" }.join(", ")
//                     def featureStatusDatasets = [
//                         """
//                             {
//                                 label: "PASS",
//                                 backgroundColor: "#4CAF50",
//                                 data: [${featureStatusData.collect { it.value.PASS }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOT EXECUTED",
//                                 backgroundColor: "#FFEB3B",
//                                 data: [${featureStatusData.collect { it.value.NOTEXECUTED }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOK MINOR",
//                                 backgroundColor: "#FF9800",
//                                 data: [${featureStatusData.collect { it.value.NOKMINOR }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOK MAJOR",
//                                 backgroundColor: "#F44336",
//                                 data: [${featureStatusData.collect { it.value.NOKMAJOR }.join(", ")}]
//                             }
//                         """
//                     ]

//                     def htmlContent = """
//                         <html>
//                         <head>
//                             <title>Test Execution - ${params.FILE_NAME}</title>
//                             <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
//                             <style>
//                                 body {
//                                     font-family: Arial, sans-serif;
//                                     margin: 20px;
//                                 }
//                                 h1, h2 {
//                                     color: #2E7D32;
//                                 }
//                                 canvas {
//                                     margin-top: 20px;
//                                     margin-bottom: 40px;
//                                     max-width: 800px;
//                                 }
//                                 .chart-container {
//                                     width: 50%;
//                                     margin: 0 auto;
//                                 }
//                             </style>
//                         </head>
//                         <body>
//                             <h1>Test Execution</h1>
//                             <h2>Nom du fichier : ${params.FILE_NAME}</h2>
//                             <div class="chart-container">
//                                 <canvas id="featureStatusChart"></canvas>
//                             </div>
//                             <script>
//                                 document.addEventListener('DOMContentLoaded', function() {
//                                     var ctxFeatureStatus = document.getElementById('featureStatusChart').getContext('2d');
//                                     new Chart(ctxFeatureStatus, {
//                                         type: 'bar',
//                                         data: {
//                                             labels: [${featureStatusLabels}],
//                                             datasets: [${featureStatusDatasets.join(", ")}]
//                                         },
//                                         options: {
//                                             responsive: true,
//                                             plugins: {
//                                                 legend: { position: 'top' }
//                                             },
//                                             scales: {
//                                                 x: { stacked: true },
//                                                 y: { stacked: true, beginAtZero: true }
//                                             }
//                                         }
//                                     });
//                                 });
//                             </script>
//                         </body>
//                         </html>
//                     """

//                     writeFile file: 'report.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Convertir en PDF') {
//             steps {
//                 script {
//                     bat 'wkhtmltopdf --version'
//                     bat 'wkhtmltopdf report.html report.pdf'

//                     if (!fileExists('report.pdf')) {
//                         error "Le fichier report.pdf n'a pas été généré !"
//                     }
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Test Execution Report'])
//             }
//         }
//     }
// }



// pipeline {
//     agent any

//     parameters {
//         string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX")')
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
//                     bat "python app.py ${params.FILE_NAME} output.json"

//                     if (!fileExists('output.json')) {
//                         error "Le fichier output.json n'a pas été généré !"
//                     }

//                     def jsonOutput = readFile('output.json').trim()
//                     if (!jsonOutput) {
//                         error "Le fichier JSON est vide !"
//                     }

//                     def jsonData = readJSON text: jsonOutput
                    
//                     def statusCounts = [:]
//                     def featureStatusData = [:]
//                     def defectsData = []
//                     jsonData.each { entry ->
//                         def feature = entry.feature.toString().trim()
//                         def status = entry.status.toString().trim()
//                         def priority = entry.defects?.priority?.toString()?.trim()?.toLowerCase() ?: ""
                        
//                         // Initialisation de la structure de données pour la feature si elle n'existe pas encore
//                         if (!featureStatusData[feature]) {
//                             featureStatusData[feature] = [PASS: 0, NOTEXECUTED: 0, NOKMINOR: 0, NOKMAJOR: 0]
//                         }
                        
//                         // Mise à jour des compteurs en fonction du statut et de la priorité
//                         if (status == 'PASS') {
//                             featureStatusData[feature].PASS++
//                         } else if (status == 'ABORTED' || status == 'TODO') {
//                             featureStatusData[feature].NOTEXECUTED++
//                         } else if (status == 'FAIL' || status == 'BLOCKED') {
//                             if (priority =='[medium]'|| status == '[high]') {
//                                 featureStatusData[feature].NOKMINOR++
//                             } else if (priority == '[very high]' || priority == '[blocker]') {
//                                 featureStatusData[feature].NOKMAJOR++
//                             }
//                         }
                        
//                         if (!statusCounts[feature]) {
//                             statusCounts[feature] = [:]
//                         }
//                         statusCounts[feature][status] = (statusCounts[feature][status] ?: 0) + 1
                        
//                         if (status == 'FAIL' || status == 'BLOCKED') {
//                             entry.defects.each { defect ->
//                                 defectsData.add("<tr><td>${defect.id}</td><td>${defect.summary}</td><td>${defect.priority}</td></tr>")
//                             }
//                         }
//                     }
                    
//                     def featureLabels = statusCounts.keySet().collect { "\"${it}\"" }.join(", ")
//                     def datasets = []
//                     def statusTypes = statusCounts.values().collectMany { it.keySet() }.unique()
                    
//                     // Couleurs fixes pour les barres (nuances de vert)
//                     def greenShades = ['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9', '#66BB6A', '#388E3C']
                    
//                     statusTypes.eachWithIndex { status, index ->
//                         def data = statusCounts.collect { it.value[status] ?: 0 }
//                         datasets.add("""
//                             {
//                                 label: "${status}",
//                                 backgroundColor: "${greenShades[index % greenShades.size()]}",
//                                 data: [${data.join(", ")}]
//                             }
//                         """)
//                     }
                    
//                     def pieData = statusCounts.collectEntries { feature, statuses ->
//                         [(feature): statuses.collect { k, v -> v }.sum()]
//                     }
//                     def pieLabels = pieData.keySet().collect { "\"${it}\"" }.join(", ")
//                     def pieValues = pieData.values().join(", ")
                    
//                     // Données pour la deuxième pie chart (basée sur featureStatusData)
//                     def featureStatusPieData = [
//                         featureStatusData.collect { it.value.PASS }.sum(),
//                         featureStatusData.collect { it.value.NOTEXECUTED }.sum(),
//                         featureStatusData.collect { it.value.NOKMINOR }.sum(),
//                         featureStatusData.collect { it.value.NOKMAJOR }.sum()
//                     ]
//                     def featureStatusPieLabels = ['PASS', 'NOT EXECUTED', 'NOK MINOR', 'NOK MAJOR']
//                     def featureStatusPieColors = ['#4CAF50', '#FFEB3B', '#FF9800', '#F44336']
                    
//                     def featureStatusLabels = featureStatusData.keySet().collect { "\"${it}\"" }.join(", ")
//                     def featureStatusDatasets = [
//                         """
//                             {
//                                 label: "PASS",
//                                 backgroundColor: "#4CAF50",
//                                 data: [${featureStatusData.collect { it.value.PASS }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOT EXECUTED",
//                                 backgroundColor: "#FFEB3B",
//                                 data: [${featureStatusData.collect { it.value.NOTEXECUTED }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOK MINOR",
//                                 backgroundColor: "#FF9800",
//                                 data: [${featureStatusData.collect { it.value.NOKMINOR }.join(", ")}]
//                             }
//                         """,
//                         """
//                             {
//                                 label: "NOK MAJOR",
//                                 backgroundColor: "#F44336",
//                                 data: [${featureStatusData.collect { it.value.NOKMAJOR }.join(", ")}]
//                             }
//                         """
//                     ]

//                  def htmlContent = """
//                     <html>
//                     <head>
//                         <title>Test Execution - ${params.FILE_NAME}</title>
//                         <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
//                         <style>
//                             body {
//                                 font-family: Arial, sans-serif;
//                                 margin: 20px;
//                             }
//                             h1, h2 {
//                                 color: #2E7D32;
//                             }
//                             table {
//                                 width: 100%;
//                                 border-collapse: collapse;
//                                 margin-top: 20px;
//                             }
//                             table, th, td {
//                                 border: 1px solid #ddd;
//                             }
//                             th, td {
//                                 padding: 12px;
//                                 text-align: left;
//                             }
//                             th {
//                                 background-color: #4CAF50;
//                                 color: white;
//                             }
//                             tr:nth-child(even) {
//                                 background-color: #f2f2f2;
//                             }
//                             tr:hover {
//                                 background-color: #ddd;
//                             }
//                             canvas {
//                                 margin-top: 20px;
//                                 margin-bottom: 40px;
//                                 max-width: 800px;
//                             }
//                             .chart-container {
//                                 width: 50%;
//                                 margin: 0 auto;
//                                 text-align: center;
//                             }
//                             .chart-description {
//                                 margin-top: 10px;
//                                 font-style: italic;
//                                 color: #555;
//                             }
//                         </style>
//                     </head>
//                     <body>
//                         <h1>Test Execution</h1>
//                         <h2>Nom du fichier : ${params.FILE_NAME}</h2>

//                         <!-- Bar Chart -->
//                         <div class="chart-container">
//                             <h3>Répartition des statuts par feature</h3>
//                             <p class="chart-description">Ce graphique montre la répartition des statuts (PASS, FAIL, etc.) pour chaque feature.</p>
//                             <canvas id="barChart"></canvas>
//                         </div>

//                         <!-- Pie Chart -->
//                         <div class="chart-container">
//                             <h3>Répartition globale des statuts</h3>
//                             <p class="chart-description">Ce graphique montre la répartition globale des statuts pour toutes les features.</p>
//                             <canvas id="pieChart"></canvas>
//                         </div>

//                         <!-- Feature Status Chart -->
//                         <div class="chart-container">
//                             <h3>Répartition des statuts détaillés par feature</h3>
//                             <p class="chart-description">Ce graphique montre la répartition des statuts détaillés (PASS, NOT EXECUTED, NOK MINOR, NOK MAJOR) pour chaque feature.</p>
//                             <canvas id="featureStatusChart"></canvas>
//                         </div>

//                         <!-- Feature Status Pie Chart -->
//                         <div class="chart-container">
//                             <h3>Répartition globale des statuts détaillés</h3>
//                             <p class="chart-description">Ce graphique montre la répartition globale des statuts détaillés pour toutes les features.</p>
//                             <canvas id="featureStatusPieChart"></canvas>
//                         </div>

//                         <!-- Defects Table -->
//                         <h2>Defects (FAIL & BLOCKED)</h2>
//                         <p class="chart-description">Liste des défauts identifiés avec leur priorité.</p>
//                         <table>
//                             <tr><th>ID</th><th>Summary</th><th>Priority</th></tr>
//                             ${defectsData.join("\n")}
//                         </table>

//                         <script>
//                             document.addEventListener('DOMContentLoaded', function() {
//                                 // Bar Chart
//                                 var ctxBar = document.getElementById('barChart').getContext('2d');
//                                 new Chart(ctxBar, {
//                                     type: 'bar',
//                                     data: {
//                                         labels: [${featureLabels}],
//                                         datasets: [${datasets.join(", ")}]
//                                     },
//                                     options: {
//                                         responsive: true,
//                                         plugins: {
//                                             legend: { position: 'top' }
//                                         },
//                                         scales: {
//                                             x: { stacked: true },
//                                             y: { stacked: true, beginAtZero: true }
//                                         }
//                                     }
//                                 });
                                
//                                 // Pie Chart
//                                 var ctxPie = document.getElementById('pieChart').getContext('2d');
//                                 new Chart(ctxPie, {
//                                     type: 'pie',
//                                     data: {
//                                         labels: [${pieLabels}],
//                                         datasets: [{
//                                             data: [${pieValues}],
//                                             backgroundColor: [${greenShades.collect { "\"${it}\"" }.join(", ")}]
//                                         }]
//                                     },
//                                     options: {
//                                         responsive: true,
//                                         plugins: {
//                                             legend: { position: 'top' }
//                                         }
//                                     }
//                                 });
                                
//                                 // Feature Status Chart
//                                 var ctxFeatureStatus = document.getElementById('featureStatusChart').getContext('2d');
//                                 new Chart(ctxFeatureStatus, {
//                                     type: 'bar',
//                                     data: {
//                                         labels: [${featureStatusLabels}],
//                                         datasets: [${featureStatusDatasets.join(", ")}]
//                                     },
//                                     options: {
//                                         responsive: true,
//                                         plugins: {
//                                             legend: { position: 'top' }
//                                         },
//                                         scales: {
//                                             x: { stacked: true },
//                                             y: { stacked: true, beginAtZero: true }
//                                         }
//                                     }
//                                 });
                                
//                                 // Feature Status Pie Chart
//                                 var ctxFeatureStatusPie = document.getElementById('featureStatusPieChart').getContext('2d');
//                                 new Chart(ctxFeatureStatusPie, {
//                                     type: 'pie',
//                                     data: {
//                                         labels: ${featureStatusPieLabels.collect { "\"${it}\"" }},
//                                         datasets: [{
//                                             data: ${featureStatusPieData},
//                                             backgroundColor: ${featureStatusPieColors.collect { "\"${it}\"" }}
//                                         }]
//                                     },
//                                     options: {
//                                         responsive: true,
//                                         plugins: {
//                                             legend: { position: 'top' }
//                                         }
//                                     }
//                                 });
//                             });
//                         </script>
//                     </body>
//                     </html>
//                 """



//                     writeFile file: 'report.html', text: htmlContent
//                 }
//             }
//         }

//         stage('Convertir en PDF') {
//             steps {
//                 script {
//                     // Assurez-vous que wkhtmltopdf est installé sur l'agent Jenkins
//                     bat 'wkhtmltopdf --version'
                    
//                     // Convertir le fichier HTML en PDF
//                     bat 'wkhtmltopdf report.html report.pdf'
                    
//                     // Vérifier que le fichier PDF a été généré
//                     if (!fileExists('report.pdf')) {
//                         error "Le fichier report.pdf n'a pas été généré !"
//                     }
//                 }
//             }
//         }

//         stage('Publier le rapport') {
//             steps {
//                 publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
                
//                 // Publier le fichier PDF
//                 archiveArtifacts artifacts: 'report.pdf', fingerprint: true
//             }
//         }
//     }
// }


pipeline {
    agent any

    parameters {
        string(name: 'FILE_NAME', defaultValue: '', description: 'Nom du fichier (format "HGWXRAY-XXXXX")')
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
                    if (!jsonOutput) {
                        error "Le fichier JSON est vide !"
                    }

                    def jsonData = readJSON text: jsonOutput
                    
                    def statusCounts = [:]
                    def featureStatusData = [:]
                    def defectsData = []
                    jsonData.each { entry ->
                        def feature = entry.feature.toString().trim()
                        def status = entry.status.toString().trim()
                        def priority = entry.defects?.priority?.toString()?.trim()?.toLowerCase() ?: ""
                        
                        // Initialisation de la structure de données pour la feature si elle n'existe pas encore
                        if (!featureStatusData[feature]) {
                            featureStatusData[feature] = [PASS: 0, NOTEXECUTED: 0, NOKMINOR: 0, NOKMAJOR: 0]
                        }
                        
                        // Mise à jour des compteurs en fonction du statut et de la priorité
                        if (status == 'PASS') {
                            featureStatusData[feature].PASS++
                        } else if (status == 'ABORTED' || status == 'TODO') {
                            featureStatusData[feature].NOTEXECUTED++
                        } else if (status == 'FAIL' || status == 'BLOCKED') {
                            if (priority =='[medium]'|| status == '[high]') {
                                featureStatusData[feature].NOKMINOR++
                            } else if (priority == '[very high]' || priority == '[blocker]') {
                                featureStatusData[feature].NOKMAJOR++
                            }
                        }
                        
                        if (!statusCounts[feature]) {
                            statusCounts[feature] = [:]
                        }
                        statusCounts[feature][status] = (statusCounts[feature][status] ?: 0) + 1
                        
                        if (status == 'FAIL' || status == 'BLOCKED') {
                            entry.defects.each { defect ->
                                defectsData.add("<tr><td>${defect.id}</td><td>${defect.summary}</td><td>${defect.priority}</td></tr>")
                            }
                        }
                    }
                    
                    def featureLabels = statusCounts.keySet().collect { "\"${it}\"" }.join(", ")
                    def datasets = []
                    def statusTypes = statusCounts.values().collectMany { it.keySet() }.unique()
                    
                    // Couleurs fixes pour les barres (nuances de vert)
                    def greenShades = ['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9', '#66BB6A', '#388E3C']
                    
                    statusTypes.eachWithIndex { status, index ->
                        def data = statusCounts.collect { it.value[status] ?: 0 }
                        datasets.add("""
                            {
                                label: "${status}",
                                backgroundColor: "${greenShades[index % greenShades.size()]}",
                                data: [${data.join(", ")}]
                            }
                        """)
                    }
                    
                    def pieData = statusCounts.collectEntries { feature, statuses ->
                        [(feature): statuses.collect { k, v -> v }.sum()]
                    }
                    def pieLabels = pieData.keySet().collect { "\"${it}\"" }.join(", ")
                    def pieValues = pieData.values().join(", ")
                    
                    // Données pour la deuxième pie chart (basée sur featureStatusData)
                    def featureStatusPieData = [
                        featureStatusData.collect { it.value.PASS }.sum(),
                        featureStatusData.collect { it.value.NOTEXECUTED }.sum(),
                        featureStatusData.collect { it.value.NOKMINOR }.sum(),
                        featureStatusData.collect { it.value.NOKMAJOR }.sum()
                    ]
                    def featureStatusPieLabels = ['PASS', 'NOT EXECUTED', 'NOK MINOR', 'NOK MAJOR']
                    def featureStatusPieColors = ['#4CAF50', '#FFEB3B', '#FF9800', '#F44336']
                    
                    def featureStatusLabels = featureStatusData.keySet().collect { "\"${it}\"" }.join(", ")
                    def featureStatusDatasets = [
                        """
                            {
                                label: "PASS",
                                backgroundColor: "#4CAF50",
                                data: [${featureStatusData.collect { it.value.PASS }.join(", ")}]
                            }
                        """,
                        """
                            {
                                label: "NOT EXECUTED",
                                backgroundColor: "#FFEB3B",
                                data: [${featureStatusData.collect { it.value.NOTEXECUTED }.join(", ")}]
                            }
                        """,
                        """
                            {
                                label: "NOK MINOR",
                                backgroundColor: "#FF9800",
                                data: [${featureStatusData.collect { it.value.NOKMINOR }.join(", ")}]
                            }
                        """,
                        """
                            {
                                label: "NOK MAJOR",
                                backgroundColor: "#F44336",
                                data: [${featureStatusData.collect { it.value.NOKMAJOR }.join(", ")}]
                            }
                        """
                    ]


                    // données cards 
                    def totalTests = 0
                    def totalPass = 0
                    def totalNotExecuted = 0
                    def totalNokMinor = 0
                    def totalNokMajor = 0

                    jsonData.each { entry ->
                        def status = entry.status.toString().trim()
                        totalTests++
                        
                        if (status == 'PASS') {
                            totalPass++
                        } else if (status == 'ABORTED' || status == 'TODO') {
                            totalNotExecuted++
                        } else if (status == 'FAIL' || status == 'BLOCKED') {
                            def priority = entry.defects?.priority?.toString()?.trim()?.toLowerCase() ?: ""
                            if (priority == '[medium]' || priority == '[high]') {
                                totalNokMinor++
                            } else if (priority == '[very high]' || priority == '[blocker]') {
                                totalNokMajor++
                            }
                        }
                    }

             def htmlContent = """
<html>
<head>
    <title>Test Execution - ${params.FILE_NAME}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Plugin pour les étiquettes de données -->
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels"></script>
    <!-- Plugin pour l'effet 3D -->
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-3d"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        h1, h2 {
            color: #2E7D32;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #ddd;
        }
        canvas {
            margin-top: 20px;
            margin-bottom: 20px;
            max-width: 100%;
        }
        .chart-container {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 40px;
            gap: 20px;
        }
        .chart-wrapper {
            width: 48%;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .chart-wrapper.pie {
            width: 30%;
        }
        .chart-wrapper.bar {
            width: 68%;
        }
        .chart-description {
            margin-top: 10px;
            font-style: italic;
            color: #555;
            text-align: center;
        }
        .card {
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            border-radius: 10px;
            width: 18%;
            text-align: center;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        .card-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 40px;
        }
        .card h3 {
            margin: 0;
            font-size: 18px;
        }
        .card p {
            margin: 10px 0 0;
            font-size: 24px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Test Execution</h1>
    <h2>Nom du fichier : ${params.FILE_NAME}</h2>

    <!-- Cards Section -->
    <div class="card-container">
        <div class="card" style="background-color: #4CAF50;">
            <h3>Total Tests</h3>
            <p>${totalTests}</p>
        </div>
        <div class="card" style="background-color: #81C784;">
            <h3>PASS</h3>
            <p>${totalPass}</p>
        </div>
        <div class="card" style="background-color: #A5D6A7; color: black;">
            <h3>NOT EXECUTED</h3>
            <p>${totalNotExecuted}</p>
        </div>
        <div class="card" style="background-color: #FF9800;">
            <h3>NOK MINOR</h3>
            <p>${totalNokMinor}</p>
        </div>
        <div class="card" style="background-color: #F44336;">
            <h3>NOK MAJOR</h3>
            <p>${totalNokMajor}</p>
        </div>
    </div>

    <!-- Bar Chart 1 and Pie Chart 1 -->
    <div class="chart-container">
        <div class="chart-wrapper bar">
            <h3>Répartition des statuts par feature</h3>
            <p class="chart-description">Ce graphique montre la répartition des statuts (PASS, FAIL, etc.) pour chaque feature.</p>
            <canvas id="barChart"></canvas>
        </div>
        <div class="chart-wrapper pie">
            <h3>Répartition globale des statuts</h3>
            <p class="chart-description">Ce graphique montre la répartition globale des statuts pour toutes les features.</p>
            <canvas id="pieChart"></canvas>
        </div>
    </div>

    <!-- Bar Chart 2 and Pie Chart 2 -->
    <div class="chart-container">
        <div class="chart-wrapper bar">
            <h3>Répartition des statuts détaillés par feature</h3>
            <p class="chart-description">Ce graphique montre la répartition des statuts détaillés (PASS, NOT EXECUTED, NOK MINOR, NOK MAJOR) pour chaque feature.</p>
            <canvas id="featureStatusChart"></canvas>
        </div>
        <div class="chart-wrapper pie">
            <h3>Répartition globale des statuts détaillés</h3>
            <p class="chart-description">Ce graphique montre la répartition globale des statuts détaillés pour toutes les features.</p>
            <canvas id="featureStatusPieChart"></canvas>
        </div>
    </div>

    <!-- Defects Table -->
    <h2>Defects (FAIL & BLOCKED)</h2>
    <p class="chart-description">Liste des défauts identifiés avec leur priorité.</p>
    <table>
        <tr><th>ID</th><th>Summary</th><th>Priority</th></tr>
        ${defectsData.join("\n")}
    </table>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Bar Chart
            var ctxBar = document.getElementById('barChart').getContext('2d');
            new Chart(ctxBar, {
                type: 'bar',
                data: {
                    labels: [${featureLabels}],
                    datasets: [${datasets.join(", ")}]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'top' }
                    },
                    scales: {
                        x: { stacked: true },
                        y: { stacked: true, beginAtZero: true }
                    }
                }
            });
            
            // Pie Chart (3D)
            var ctxPie = document.getElementById('pieChart').getContext('2d');
            new Chart(ctxPie, {
                type: 'pie',
                data: {
                    labels: [${pieLabels}],
                    datasets: [{
                        data: [${pieValues}],
                        backgroundColor: [${greenShades.collect { "\"${it}\"" }.join(", ")}]
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'top' },
                        datalabels: {
                            color: '#fff',
                            font: { size: 14 },
                            formatter: (value) => value > 0 ? value : ''
                        },
                        'chartjs-plugin-3d': {
                            enabled: true,
                            alpha: 45, // Angle de rotation
                            depth: 50 // Profondeur de l'effet 3D
                        }
                    }
                },
                plugins: [ChartDataLabels, Chart3D] // Activer les plugins
            });
            
            // Feature Status Chart
            var ctxFeatureStatus = document.getElementById('featureStatusChart').getContext('2d');
            new Chart(ctxFeatureStatus, {
                type: 'bar',
                data: {
                    labels: [${featureStatusLabels}],
                    datasets: [${featureStatusDatasets.join(", ")}]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'top' }
                    },
                    scales: {
                        x: { stacked: true },
                        y: { stacked: true, beginAtZero: true }
                    }
                }
            });
            
            // Feature Status Pie Chart (3D)
            var ctxFeatureStatusPie = document.getElementById('featureStatusPieChart').getContext('2d');
            new Chart(ctxFeatureStatusPie, {
                type: 'pie',
                data: {
                    labels: ${featureStatusPieLabels.collect { "\"${it}\"" }},
                    datasets: [{
                        data: ${featureStatusPieData},
                        backgroundColor: ${featureStatusPieColors.collect { "\"${it}\"" }}
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'top' },
                        datalabels: {
                            color: '#fff',
                            font: { size: 14 },
                            formatter: (value) => value > 0 ? value : ''
                        },
                        'chartjs-plugin-3d': {
                            enabled: true,
                            alpha: 45, // Angle de rotation
                            depth: 50 // Profondeur de l'effet 3D
                        }
                    }
                },
                plugins: [ChartDataLabels, Chart3D] // Activer les plugins
            });
        });
    </script>
</body>
</html>"""


                    writeFile file: 'report.html', text: htmlContent
                }
            }
        }

        stage('Convertir en PDF') {
            steps {
                script {
                    // Assurez-vous que wkhtmltopdf est installé sur l'agent Jenkins
                    bat 'wkhtmltopdf --version'
                    
                    // Convertir le fichier HTML en PDF
                    bat 'wkhtmltopdf report.html report.pdf'
                    
                    // Vérifier que le fichier PDF a été généré
                    if (!fileExists('report.pdf')) {
                        error "Le fichier report.pdf n'a pas été généré !"
                    }
                }
            }
        }

        stage('Publier le rapport') {
            steps {
                publishHTML(target: [reportDir: '', reportFiles: 'report.html', reportName: 'Visualisation des Features'])
                
                // Publier le fichier PDF
                archiveArtifacts artifacts: 'report.pdf', fingerprint: true
            }
        }
    }
}

