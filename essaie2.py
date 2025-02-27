# import os
# import json
# from collections import defaultdict

# def get_user_input():
#     user_input = input("Entrez le nom du fichier (format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX') : ")
#     if not user_input.startswith("HGWXRAY-") or not (len(user_input.split("-")[-1]) in [4, 5]):
#         print("Format invalide. Le nom doit être sous le format 'HGWXRAY-XXXXX' ou 'HGWXRAY-XXXX'.")
#         exit(1)
#     return user_input

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

#                             print(f"ID de défaut trouvé : {defect_id} associé au testKey : {test_key} avec priorité : {priority}")

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
#             "feature": feature,
#             "status": status,
#             "defects": defects_info
#         })

#     return output_data, defect_to_testkey, defect_counts

# def save_output_to_json(output_data, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         json.dump(output_data, file, ensure_ascii=False, indent=4)
#     print(f"Les données ont été enregistrées dans le fichier {output_file}.")

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
#     display_defect_summary(defect_to_testkey, defect_counts)



# ******************************************************
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

from flask import Flask, jsonify, render_template, abort, send_file
import json
import os
import csv

app = Flask(__name__)

json_folder = "PFE json files"
main_json_file = "HGWXRAY-93121.json"
runId = "testrunIDs.json"
csv_output_file = "json_statuses.csv"
defect="testCaseDefects.json"