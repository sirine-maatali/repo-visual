# from flask import Flask, request, jsonify
# import os
# import json
# from collections import defaultdict
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# def read_json_file(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {"error": f"Fichier non trouvé : {file_path}"}
#     except json.JSONDecodeError:
#         return {"error": f"Erreur de lecture du fichier JSON : {file_path}"}

# def extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name):
#     execution_file_path = os.path.join(test_execution_folder, f"{file_name}.json")
#     execution_data = read_json_file(execution_file_path)

#     customfield_data = execution_data.get("fields", {}).get("customfield_12219", [])
#     if not customfield_data:
#         return {"error": f"Le champ 'customfield_12219' est vide ou absent dans {execution_file_path}."}

#     output_data = []
#     defect_to_testkey = defaultdict(set)
#     defect_counts = defaultdict(int)

#     for item in customfield_data:
#         test_key = item.get("testKey")
#         test_run_id = item.get("testRunId")

#         if not test_key:
#             continue

#         test_case_file_path = os.path.join(test_cases_folder, f"{test_key}.json")
#         test_case_data = read_json_file(test_case_file_path)

#         feature = test_case_data.get("fields", {}).get("customfield_13601", "null")

#         defects_file_path = os.path.join(defects_folder, f"{file_name}.json")
#         defects_data = read_json_file(defects_file_path)

#         status = "null"
#         defects_info = []

#         if isinstance(defects_data, list):
#             for defect in defects_data:
#                 if defect.get("key") == test_key:
#                     status = defect.get("status", "null")
#                     if status in ["BLOCKED", "FAIL"]:
#                         defects_list = defect.get("defects", [])
#                         for defect_item in defects_list:
#                             defect_id = defect_item.get("id", "null")

#                             # Ajout des informations de priorité
#                             priority = "null"
#                             issue_links = test_case_data.get("fields", {}).get("issuelinks", [])
#                             for link in issue_links:
#                                 outward_issue = link.get("outwardIssue", {})
#                                 priority_field = outward_issue.get("fields", {}).get("priority", {})
#                                 priority = priority_field.get("name", "null")
#                                 if priority != "null":
#                                     break

#                             defect_to_testkey[defect_id].add(test_key)
#                             defect_counts[defect_id] += 1

#                             defects_info.append({
#                                 "id": defect_id,
#                                 "summary": defect_item.get("summary", "null"),
#                                 "priority": priority
#                             })
#                     break

#         output_data.append({
#             "input_file": file_name,
#             "testKey": test_key,
#             "testRunId": test_run_id,
#             "feature": str(feature),
#             "status": status,
#             "defects": defects_info
#         })

#     return {
#         "output_data": output_data,
#         "defect_to_testkey": dict((k, list(v)) for k, v in defect_to_testkey.items()),
#         "defect_counts": dict(defect_counts)
#     }

# def save_output_to_html(output_data):
#     """ Fonction pour sauvegarder les résultats dans un fichier HTML """
#     html_content = """
#     <html>
#     <head>
#         <title>Visualisation des Données</title>
#     </head>
#     <body>
#         <h1>Résultats du Test</h1>
#         <pre>{}</pre>
#     </body>
#     </html>
#     """.format(json.dumps(output_data, indent=4))

#     with open("output.html", "w", encoding="utf-8") as file:
#         file.write(html_content)

# @app.route("/process-data", methods=["POST"])
# def process_data():
#     data = request.json
#     file_name = data.get("file_name", "")
#     if not file_name or not file_name.startswith("HGWXRAY-"):
#         return jsonify({"error": "Nom de fichier invalide"}), 400

#     test_execution_folder = "test execution"
#     test_cases_folder = "test cases"
#     defects_folder = "testCase Defects"

#     if not all(os.path.exists(folder) for folder in [test_execution_folder, test_cases_folder, defects_folder]):
#         return jsonify({"error": "Un ou plusieurs dossiers requis sont manquants"}), 400

#     result = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name)
    
#     # Sauvegarder les résultats dans un fichier HTML
#     save_output_to_html(result)
    
#     return jsonify(result)

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)
 

# import os
# import json
# from collections import defaultdict

# def get_user_input():
#     while True:
#         user_input = input("Entrez le nom du fichier (format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX') : ")
#         if user_input.startswith("HGWXRAY-") and len(user_input.split("-")[-1]) in [4, 5]:
#             return user_input
#         else:
#             print("Format invalide. Le nom doit être sous le format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX'.")

# def read_json_file(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         print(f"Fichier non trouvé : {file_path}")
#         exit(1)
#     except json.JSONDecodeError:
#         print(f"Erreur de lecture du fichier JSON : {file_path}")
#         exit(1)

# def extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name):
#     execution_file_path = os.path.join(test_execution_folder, f"{file_name}.json")
#     execution_data = read_json_file(execution_file_path)

#     customfield_data = execution_data.get("fields", {}).get("customfield_12219", [])
#     if not customfield_data:
#         print(f"Le champ 'customfield_12219' est vide ou absent dans {execution_file_path}.")
#         exit(1)

#     output_data = []
#     defect_to_testkey = defaultdict(set)
#     defect_counts = defaultdict(int)

#     for item in customfield_data:
#         test_key = item.get("testKey")
#         test_run_id = item.get("testRunId")

#         if not test_key:
#             continue

#         test_case_file_path = os.path.join(test_cases_folder, f"{test_key}.json")
#         test_case_data = read_json_file(test_case_file_path)

#         feature = test_case_data.get("fields", {}).get("customfield_13601", "null")

#         defects_file_path = os.path.join(defects_folder, f"{file_name}.json")
#         defects_data = read_json_file(defects_file_path)

#         status = "null"
#         defects_info = []

#         if isinstance(defects_data, list):
#             for defect in defects_data:
#                 if defect.get("key") == test_key:
#                     status = defect.get("status", "null")
#                     if status in ["BLOCKED", "FAIL"]:
#                         defects_list = defect.get("defects", [])
#                         for defect_item in defects_list:
#                             defect_id = defect_item.get("id", "null")

#                             # Accès à la priorité à partir du fichier test case
#                             priority = "null"  # Valeur par défaut
#                             issue_links = test_case_data.get("fields", {}).get("issuelinks", [])
#                             for link in issue_links:
#                                 outward_issue = link.get("outwardIssue", {})
#                                 priority_field = outward_issue.get("fields", {}).get("priority", {})
#                                 priority = priority_field.get("name", "null")
#                                 if priority != "null":
#                                     break  # Si une priorité est trouvée, on l'ajoute et on arrête la boucle

#                             # Ajout de la correspondance entre defect_id et testKey
#                             defect_to_testkey[defect_id].add(test_key)
#                             defect_counts[defect_id] += 1

#                             defects_info.append({
#                                 "id": defect_id,
#                                 "summary": defect_item.get("summary", "null"),
#                                 "priority": priority
#                             })
#                     break

#         output_data.append({
#             "input_file": file_name,
#             "testKey": test_key,
#             "testRunId": test_run_id,
#             "feature": str(feature),  # Assurez-vous que feature est une chaîne
#             "status": status,
#             "defects": defects_info
#         })

#     return output_data, defect_to_testkey, defect_counts

# def save_output_to_json(output_data, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(output_data, file, ensure_ascii=False, indent=4)
#     print(f"Les données ont été enregistrées dans le fichier {output_file}.")

# def save_output_by_feature(output_data, output_file):
#     feature_grouped = defaultdict(list)
#     for item in output_data:
#         feature = str(item["feature"])  # Assurez-vous que feature est une chaîne
#         feature_grouped[feature].append(item)

#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(feature_grouped, file, ensure_ascii=False, indent=4)
#     print(f"Les données ont été enregistrées dans le fichier {output_file} par fonctionnalité.")

# def display_defect_summary(defect_to_testkey, defect_counts):
#     print("\nRésumé des défauts :")
#     for defect_id, test_keys in defect_to_testkey.items():
#         print(f"ID de défaut : {defect_id}")
#         print(f"TestKeys associés : {', '.join(test_keys)}")
#         print(f"Nombre total de défauts : {defect_counts[defect_id]}\n")

# if __name__ == "__main__":
#     test_execution_folder = "test execution"
#     test_cases_folder = "test cases"
#     defects_folder = "testCase Defects"
#     output_file = "output.json"
#     output_file_by_feature = "output2.json"

#     if not os.path.exists(test_execution_folder):
#         print(f"Le dossier '{test_execution_folder}' n'existe pas.")
#         exit(1)
#     if not os.path.exists(test_cases_folder):
#         print(f"Le dossier '{test_cases_folder}' n'existe pas.")
#         exit(1)
#     if not os.path.exists(defects_folder):
#         print(f"Le dossier '{defects_folder}' n'existe pas.")
#         exit(1)

#     file_name = get_user_input()
#     output_data, defect_to_testkey, defect_counts = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name)
#     save_output_to_json(output_data, output_file)
#     save_output_by_feature(output_data, output_file_by_feature)
#     display_defect_summary(defect_to_testkey, defect_counts)



# import os
# import json
# from collections import defaultdict

# def get_user_input():
#     while True:
#         user_input = input("Entrez le nom du fichier (format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX') : ")
#         if user_input.startswith("HGWXRAY-") and len(user_input.split("-")[-1]) in [4, 5]:
#             return user_input
#         else:
#             print("Format invalide. Le nom doit être sous le format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX'.")

# def read_json_file(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         print(f"Fichier non trouvé : {file_path}")
#         exit(1)
#     except json.JSONDecodeError:
#         print(f"Erreur de lecture du fichier JSON : {file_path}")
#         exit(1)

# def extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name):
#     execution_file_path = os.path.join(test_execution_folder, f"{file_name}.json")
#     execution_data = read_json_file(execution_file_path)

#     customfield_data = execution_data.get("fields", {}).get("customfield_12219", [])
#     if not customfield_data:
#         print(f"Le champ 'customfield_12219' est vide ou absent dans {execution_file_path}.")
#         exit(1)

#     output_data = []
#     defect_to_testkey = defaultdict(set)
#     defect_counts = defaultdict(int)

#     for item in customfield_data:
#         test_key = item.get("testKey")
#         test_run_id = item.get("testRunId")

#         if not test_key:
#             continue

#         test_case_file_path = os.path.join(test_cases_folder, f"{test_key}.json")
#         test_case_data = read_json_file(test_case_file_path)

#         feature = test_case_data.get("fields", {}).get("customfield_13601", "null")

#         defects_file_path = os.path.join(defects_folder, f"{file_name}.json")
#         defects_data = read_json_file(defects_file_path)

#         status = "null"
#         defects_info = []

#         if isinstance(defects_data, list):
#             for defect in defects_data:
#                 if defect.get("key") == test_key:
#                     status = defect.get("status", "null")
#                     if status in ["BLOCKED", "FAIL"]:
#                         defects_list = defect.get("defects", [])
#                         for defect_item in defects_list:
#                             defect_id = defect_item.get("id", "null")

#                             # Accès à la priorité à partir du fichier test case
#                             priority = "null"  # Valeur par défaut
#                             issue_links = test_case_data.get("fields", {}).get("issuelinks", [])
#                             for link in issue_links:
#                                 outward_issue = link.get("outwardIssue", {})
#                                 priority_field = outward_issue.get("fields", {}).get("priority", {})
#                                 priority = priority_field.get("name", "null")
#                                 if priority != "null":
#                                     break  # Si une priorité est trouvée, on l'ajoute et on arrête la boucle

#                             # Ajout de la correspondance entre defect_id et testKey
#                             defect_to_testkey[defect_id].add(test_key)
#                             defect_counts[defect_id] += 1

#                             defects_info.append({
#                                 "id": defect_id,
#                                 "summary": defect_item.get("summary", "null"),
#                                 "priority": priority
#                             })
#                     break

#         output_data.append({
#             "input_file": file_name,
#             "testKey": test_key,
#             "testRunId": test_run_id,
#             "feature": str(feature),  # Assurez-vous que feature est une chaîne
#             "status": status,
#             "defects": defects_info
#         })

#     return output_data, defect_to_testkey, defect_counts

# def save_output_to_json(output_data, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(output_data, file, ensure_ascii=False, indent=4)
#     print(f"Les données ont été enregistrées dans le fichier {output_file}.")

# def save_output_by_feature(output_data, output_file):
#     feature_grouped = defaultdict(list)
#     for item in output_data:
#         feature = str(item["feature"])  # Assurez-vous que feature est une chaîne
#         feature_grouped[feature].append(item)

#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(feature_grouped, file, ensure_ascii=False, indent=4)
#     print(f"Les données ont été enregistrées dans le fichier {output_file} par fonctionnalité.")

# def display_defect_summary(defect_to_testkey, defect_counts):
#     print("\nRésumé des défauts :")
#     for defect_id, test_keys in defect_to_testkey.items():
#         print(f"ID de défaut : {defect_id}")
#         print(f"TestKeys associés : {', '.join(test_keys)}")
#         print(f"Nombre total de défauts : {defect_counts[defect_id]}\n")

# if __name__ == "__main__":
#     test_execution_folder = "test execution"
#     test_cases_folder = "test cases"
#     defects_folder = "testCase Defects"
#     output_file = "output.json"
#     output_file_by_feature = "output2.json"

#     if not os.path.exists(test_execution_folder):
#         print(f"Le dossier '{test_execution_folder}' n'existe pas.")
#         exit(1)
#     if not os.path.exists(test_cases_folder):
#         print(f"Le dossier '{test_cases_folder}' n'existe pas.")
#         exit(1)
#     if not os.path.exists(defects_folder):
#         print(f"Le dossier '{defects_folder}' n'existe pas.")
#         exit(1)

#     file_name = get_user_input()
#     output_data, defect_to_testkey, defect_counts = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name)
#     save_output_to_json(output_data, output_file)
#     save_output_by_feature(output_data, output_file_by_feature)
#     display_defect_summary(defect_to_testkey, defect_counts)


# hedhi temshiiii *****************************************************

# import os
# import json
# import sys
# from collections import defaultdict
# import sys
# sys.stdout.reconfigure(encoding='utf-8')


# def get_user_input():
#     """Demande à l'utilisateur d'entrer le nom du fichier sous le bon format."""
#     while True:
#         user_input = input("Entrez le nom du fichier (format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX') : ")
#         if user_input.startswith("HGWXRAY-") and len(user_input.split("-")[-1]) in [4, 5]:
#             return user_input
#         print("Format invalide. Le nom doit être sous le format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX'.")

# def read_json_file(file_path):
#     """Lit un fichier JSON et retourne son contenu sous forme de dictionnaire."""
#     if not os.path.exists(file_path):
#         print(f" Fichier non trouvé : {file_path}")
#         sys.exit(1)
    
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except json.JSONDecodeError:
#         print(f" Erreur de lecture du fichier JSON : {file_path}")
#         sys.exit(1)

# def extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name):
#     """Extrait les données des tests et des défauts associés."""
#     execution_file_path = os.path.join(test_execution_folder, f"{file_name}.json")
#     execution_data = read_json_file(execution_file_path)

#     customfield_data = execution_data.get("fields", {}).get("customfield_12219", [])
#     if not customfield_data:
#         print(f" Le champ 'customfield_12219' est vide ou absent dans {execution_file_path}.")
#         sys.exit(1)

#     output_data = []
#     defect_to_testkey = defaultdict(set)
#     defect_counts = defaultdict(int)

#     for item in customfield_data:
#         test_key = item.get("testKey")
#         test_run_id = item.get("testRunId")

#         if not test_key:
#             continue

#         test_case_file_path = os.path.join(test_cases_folder, f"{test_key}.json")
#         test_case_data = read_json_file(test_case_file_path)

#         feature = test_case_data.get("fields", {}).get("customfield_13601", "null")

#         defects_file_path = os.path.join(defects_folder, f"{file_name}.json")
#         defects_data = read_json_file(defects_file_path)

#         status = "null"
#         defects_info = []

#         if isinstance(defects_data, list):
#             for defect in defects_data:
#                 if defect.get("key") == test_key:
#                     status = defect.get("status", "null")
#                     if status in ["BLOCKED", "FAIL"]:
#                         for defect_item in defect.get("defects", []):
#                             defect_id = defect_item.get("id", "null")

#                             # Récupération de la priorité
#                             priority = "null"
#                             for link in test_case_data.get("fields", {}).get("issuelinks", []):
#                                 priority = link.get("outwardIssue", {}).get("fields", {}).get("priority", {}).get("name", "null")
#                                 if priority != "null":
#                                     break

#                             defect_to_testkey[defect_id].add(test_key)
#                             defect_counts[defect_id] += 1

#                             defects_info.append({
#                                 "id": defect_id,
#                                 "summary": defect_item.get("summary", "null"),
#                                 "priority": priority
#                             })
#                     break

#         output_data.append({
#             "input_file": file_name,
#             "testKey": test_key,
#             "testRunId": test_run_id,
#             "feature": str(feature),
#             "status": status,
#             "defects": defects_info
#         })

#     return output_data, defect_to_testkey, defect_counts

# def save_output_to_json(output_data, output_file):
#     """Enregistre les résultats au format JSON."""
#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(output_data, file, ensure_ascii=False, indent=4)
#     print(f" Données enregistrées dans {output_file}.")

# def save_output_by_feature(output_data, output_file):
#     """Enregistre les résultats groupés par fonctionnalité."""
#     feature_grouped = defaultdict(list)
#     for item in output_data:
#         feature_grouped[str(item["feature"])].append(item)

#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(feature_grouped, file, ensure_ascii=False, indent=4)
#     print(f" Données enregistrées dans {output_file} (groupées par fonctionnalité).")

# def display_defect_summary(defect_to_testkey, defect_counts):
#     """Affiche un résumé des défauts détectés."""
#     print("\n Résumé des défauts :")
#     for defect_id, test_keys in defect_to_testkey.items():
#         print(f" ID de défaut : {defect_id}")
#         print(f" TestKeys associés : {', '.join(test_keys)}")
#         print(f" Nombre total de défauts : {defect_counts[defect_id]}\n")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print(" Usage : python app.py <NOM_DU_FICHIER>")
#         sys.exit(1)

#     file_name = sys.argv[1]

#     test_execution_folder = "test execution"
#     test_cases_folder = "test cases"
#     defects_folder = "testCase Defects"
#     output_file = "output.json"
#     output_file_by_feature = "output2.json"

#     for folder in [test_execution_folder, test_cases_folder, defects_folder]:
#         if not os.path.exists(folder):
#             print(f" Le dossier '{folder}' n'existe pas.")
#             sys.exit(1)

#     output_data, defect_to_testkey, defect_counts = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name)
#     save_output_to_json(output_data, output_file)
#     save_output_by_feature(output_data, output_file_by_feature)
#     display_defect_summary(defect_to_testkey, defect_counts)



# ***************************

# import os
# import json
# import sys
# from collections import defaultdict

# sys.stdout.reconfigure(encoding='utf-8')

# def get_user_input():
#     """Demande à l'utilisateur d'entrer le nom du fichier sous le bon format."""
#     while True:
#         user_input = input("Entrez le nom du fichier (format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX') : ")
#         if user_input.startswith("HGWXRAY-") and len(user_input.split("-")[-1]) in [4, 5]:
#             return user_input
#         print("Format invalide. Le nom doit être sous le format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX'.")

# def read_json_file(file_path):
#     """Lit un fichier JSON et retourne son contenu sous forme de dictionnaire."""
#     if not os.path.exists(file_path):
#         print(f" Fichier non trouvé : {file_path}")
#         sys.exit(1)
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except json.JSONDecodeError:
#         print(f" Erreur de lecture du fichier JSON : {file_path}")
#         sys.exit(1)

# def extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name):
#     """Extrait les données des tests et des défauts associés."""
#     execution_file_path = os.path.join(test_execution_folder, f"{file_name}.json")
#     execution_data = read_json_file(execution_file_path)

#     customfield_data = execution_data.get("fields", {}).get("customfield_12219", [])
#     if not customfield_data:
#         print(f" Le champ 'customfield_12219' est vide ou absent dans {execution_file_path}.")
#         sys.exit(1)

#     output_data = []
#     defect_to_testkey = defaultdict(set)
#     defect_counts = defaultdict(int)

#     for item in customfield_data:
#         test_key = item.get("testKey")
#         test_run_id = item.get("testRunId")

#         if not test_key:
#             continue

#         test_case_file_path = os.path.join(test_cases_folder, f"{test_key}.json")
#         test_case_data = read_json_file(test_case_file_path)

#         feature = test_case_data.get("fields", {}).get("customfield_13601", "null")

#         defects_file_path = os.path.join(defects_folder, f"{file_name}.json")
#         defects_data = read_json_file(defects_file_path)

#         status = "null"
#         defects_info = []

#         if isinstance(defects_data, list):
#             for defect in defects_data:
#                 if defect.get("key") == test_key:
#                     status = defect.get("status", "null")
#                     if status in ["BLOCKED", "FAIL"]:
#                         for defect_item in defect.get("defects", []):
#                             defect_id = defect_item.get("id", "null")

#                             # Récupération de la priorité
#                             priority = "null"
#                             for link in test_case_data.get("fields", {}).get("issuelinks", []):
#                                 priority = link.get("outwardIssue", {}).get("fields", {}).get("priority", {}).get("name", "null")
#                                 if priority != "null":
#                                     break

#                             defect_to_testkey[defect_id].add(test_key)
#                             defect_counts[defect_id] += 1

#                             defects_info.append({
#                                 "id": defect_id,
#                                 "summary": defect_item.get("summary", "null"),
#                                 "priority": priority
#                             })
#                     break

#         output_data.append({
#             "input_file": file_name,
#             "testKey": test_key,
#             "testRunId": test_run_id,
#             "feature": str(feature),
#             "status": status,
#             "defects": defects_info
#         })

#     return output_data, defect_to_testkey, defect_counts

# def save_output_to_json(output_data, output_file):
#     """Enregistre les résultats au format JSON et les retourne pour affichage."""
#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(output_data, file, ensure_ascii=False, indent=4)
#     print(f" Données enregistrées dans {output_file}.")
#     return output_data  # Retourne les données pour affichage

# def save_output_by_feature(output_data, output_file):
#     """Enregistre les résultats groupés par fonctionnalité."""
#     feature_grouped = defaultdict(list)
#     for item in output_data:
#         feature_grouped[str(item["feature"])].append(item)

#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(feature_grouped, file, ensure_ascii=False, indent=4)
#     print(f" Données enregistrées dans {output_file} (groupées par fonctionnalité).")

# def display_defect_summary(defect_to_testkey, defect_counts):
#     """Affiche un résumé des défauts détectés."""
#     print("\n Résumé des défauts :")
#     for defect_id, test_keys in defect_to_testkey.items():
#         print(f" ID de défaut : {defect_id}")
#         print(f" TestKeys associés : {', '.join(test_keys)}")
#         print(f" Nombre total de défauts : {defect_counts[defect_id]}\n")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print(" Usage : python app.py <NOM_DU_FICHIER>")
#         sys.exit(1)

#     file_name = sys.argv[1]

#     test_execution_folder = "test execution"
#     test_cases_folder = "test cases"
#     defects_folder = "testCase Defects"
#     output_file = "output.json"
#     output_file_by_feature = "output2.json"

#     for folder in [test_execution_folder, test_cases_folder, defects_folder]:
#         if not os.path.exists(folder):
#             print(f" Le dossier '{folder}' n'existe pas.")
#             sys.exit(1)

#     output_data, defect_to_testkey, defect_counts = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name)
#     output_data = save_output_to_json(output_data, output_file)  # Récupère les données ici pour affichage
#     save_output_by_feature(output_data, output_file_by_feature)
#     display_defect_summary(defect_to_testkey, defect_counts)

#     # Affichage des données en console
#     print(json.dumps(output_data, ensure_ascii=False, indent=4))  # Affiche le contenu de output2.json



# *****************************************hedhi shyha

# import os
# import json
# import sys
# from collections import defaultdict

# sys.stdout.reconfigure(encoding='utf-8')

# def read_json_file(file_path):
#     """Lit un fichier JSON et retourne son contenu sous forme de dictionnaire."""
#     if not os.path.exists(file_path):
#         return {"error": f"Fichier non trouvé : {file_path}"}
    
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except json.JSONDecodeError:
#         return {"error": f"Erreur de lecture du fichier JSON : {file_path}"}

# def extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name, output_file):
#     """Extrait les données des tests et des défauts associés."""
#     execution_file_path = os.path.join(test_execution_folder, f"{file_name}.json")
#     execution_data = read_json_file(execution_file_path)

#     if "error" in execution_data:
#         return execution_data

#     customfield_data = execution_data.get("fields", {}).get("customfield_12219", [])
#     if not customfield_data:
#         return {"error": f"Le champ 'customfield_12219' est vide ou absent dans {execution_file_path}"}

#     output_data = []
#     defect_to_testkey = defaultdict(set)
#     defect_counts = defaultdict(int)

#     for item in customfield_data:
#         test_key = item.get("testKey")
#         test_run_id = item.get("testRunId")

#         if not test_key:
#             continue

#         test_case_file_path = os.path.join(test_cases_folder, f"{test_key}.json")
#         test_case_data = read_json_file(test_case_file_path)

#         # Extraction de la feature sans les crochets
#         feature = test_case_data.get("fields", {}).get("customfield_13601", "null")
#         if isinstance(feature, list) and feature:
#             feature = feature[0]  # Prend le premier élément de la liste si c'est une liste

#         defects_file_path = os.path.join(defects_folder, f"{file_name}.json")
#         defects_data = read_json_file(defects_file_path)

#         status = "null"
#         defects_info = []

#         if isinstance(defects_data, list):
#             for defect in defects_data:
#                 if defect.get("key") == test_key:
#                     status = defect.get("status", "null")
#                     if status in ["BLOCKED", "FAIL"]:
#                         for defect_item in defect.get("defects", []):
#                             defect_id = defect_item.get("id", "null")

#                             # Recherche de la priorité dans les issuelinks du testKey.json
#                             priority = "null"
#                             for link in test_case_data.get("fields", {}).get("issuelinks", []):
#                                 outward_issue = link.get("outwardIssue", {})
#                                 outward_issue_id = outward_issue.get("id", "null")

#                                 # Debugging : Afficher les valeurs pour vérifier
#                                 print(f"Test Key: {test_key}, Defect ID: {defect_id}, Outward Issue ID: {outward_issue_id}")

#                                 # Comparaison des IDs
#                                 if str(outward_issue_id) == str(defect_id):  # Convertir en chaîne pour éviter les erreurs de type
#                                     priority = outward_issue.get("fields", {}).get("priority", {}).get("name", "null")
#                                     print(f"Priorité trouvée : {priority} pour Defect ID: {defect_id}")
#                                     break

#                             defect_to_testkey[defect_id].add(test_key)
#                             defect_counts[defect_id] += 1

#                             defects_info.append({
#                                 "id": defect_id,
#                                 "summary": defect_item.get("summary", "null"),
#                                 "priority": priority  # Priorité trouvée
#                             })
#                     break

#         output_data.append({
#             "input_file": file_name,
#             "testKey": test_key,
#             "testRunId": test_run_id,
#             "feature": feature,  # Utilise la feature sans les crochets
#             "status": status,
#             "defects": defects_info
#         })

#     # Sauvegarde dans un fichier JSON
#     with open(output_file, "w", encoding="utf-8") as f:
#         json.dump(output_data, f, ensure_ascii=False, indent=4)

#     return output_data

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print(json.dumps({"error": "Usage : python app.py <NOM_DU_FICHIER> <OUTPUT_JSON>"}))
#         sys.exit(1)

#     file_name = sys.argv[1]
#     output_file = sys.argv[2]

#     test_execution_folder = "test execution"
#     test_cases_folder = "test cases"
#     defects_folder = "testCase Defects"

#     for folder in [test_execution_folder, test_cases_folder, defects_folder]:
#         if not os.path.exists(folder):
#             print(json.dumps({"error": f"Le dossier '{folder}' n'existe pas."}))
#             sys.exit(1)

#     result = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name, output_file)

#     # print(json.dumps(result, ensure_ascii=False, indent=4))

import os
import json
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

def read_json_file(file_path):
    """Lit un fichier JSON et retourne son contenu sous forme de dictionnaire."""
    if not os.path.exists(file_path):
        return {"error": f"Fichier non trouvé : {file_path}"}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {"error": f"Erreur de lecture du fichier JSON : {file_path}"}

def extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name, output_file):
    """Extrait les données des tests et des défauts associés."""
    execution_file_path = os.path.join(test_execution_folder, f"{file_name}.json")
    execution_data = read_json_file(execution_file_path)

    if "error" in execution_data:
        return execution_data

    customfield_data = execution_data.get("fields", {}).get("customfield_12219", [])
    
    # Extraction de la version sans les crochets
    version_field = execution_data.get("fields", {}).get("customfield_13301", "null")
    if isinstance(version_field, list) and len(version_field) > 0:
        version = version_field[0]  # Prendre la première valeur de la liste
    else:
        version = version_field  # Utiliser la valeur telle quelle
    
    if not customfield_data:
        return {"error": f"Le champ 'customfield_12219' est vide ou absent dans {execution_file_path}"}

    # Récupération du champ "project" à partir de customfield_13305
    project_field = execution_data.get("fields", {}).get("customfield_13305", [])
    project = "null"  # Valeur par défaut

    # Si project_field est une liste non vide, on extrait la valeur de "value"
    if isinstance(project_field, list) and len(project_field) > 0:
        project = project_field[0].get("value", "null")

    output_data = []
    defect_to_testkey = defaultdict(set)
    defect_counts = defaultdict(int)

    for item in customfield_data:
        test_key = item.get("testKey")
        test_run_id = item.get("testRunId")

        if not test_key:
            continue

        test_case_file_path = os.path.join(test_cases_folder, f"{test_key}.json")
        test_case_data = read_json_file(test_case_file_path)

        # Extraction de la feature sans les crochets
        feature = test_case_data.get("fields", {}).get("customfield_13601", "null")
        if isinstance(feature, list) and feature:
            feature = feature[0]
        
        # Ajout du champ "testcase" contenant "summary"
        testcase_summary = test_case_data.get("fields", {}).get("summary", "null")

        defects_file_path = os.path.join(defects_folder, f"{file_name}.json")
        defects_data = read_json_file(defects_file_path)

        status = "null"
        defects_info = []

        if isinstance(defects_data, list):
            for defect in defects_data:
                if defect.get("key") == test_key:
                    status = defect.get("status", "null")
                    if status in ["BLOCKED", "FAIL"]:
                        for defect_item in defect.get("defects", []):
                            defect_id = defect_item.get("id", "null")
                            
                            priority = "null"
                            for link in test_case_data.get("fields", {}).get("issuelinks", []):
                                outward_issue = link.get("outwardIssue", {})
                                outward_issue_id = outward_issue.get("id", "null")
                                
                                if str(outward_issue_id) == str(defect_id):
                                    priority = outward_issue.get("fields", {}).get("priority", {}).get("name", "null")
                                    break

                            defect_to_testkey[defect_id].add(test_key)
                            defect_counts[defect_id] += 1

                            defects_info.append({
                                "id": defect_id,
                                "summary": defect_item.get("summary", "null"),
                                "priority": priority
                            })
                    break

        result = "null"
        if status == "PASS":
            result = "ok"
        elif status in ["TODO", "ABORTED"]:
            result = "NOT EXECUTED"
        elif status in ["FAIL", "BLOCKED"]:
            if any(defect.get("priority", "").lower() in ["medium", "high"] for defect in defects_info):
                result = "NOK MINOR"
            elif any(defect.get("priority", "").lower() in ["very high", "blocker"] for defect in defects_info):
                result = "NOK MAJOR"

        output_data.append({
            "input_file": file_name,
            "testKey": test_key,
            "testRunId": test_run_id,
            "feature": feature,
            "status": status,
            "testcase": testcase_summary,  # Ajout du champ "testcase"
            "version": version,  # Ajout du champ "version" sans crochets
            "project": project,  # Ajout du champ "project"
            "defects": defects_info,
            "result": result
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

    return output_data

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage : python app.py <NOM_DU_FICHIER> <OUTPUT_JSON>"}))
        sys.exit(1)

    file_name = sys.argv[1]
    output_file = sys.argv[2]

    test_execution_folder = "test execution"
    test_cases_folder = "test cases"
    defects_folder = "testCase Defects"

    for folder in [test_execution_folder, test_cases_folder, defects_folder]:
        if not os.path.exists(folder):
            print(json.dumps({"error": f"Le dossier '{folder}' n'existe pas."}))
            sys.exit(1)

    result = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file_name, output_file)