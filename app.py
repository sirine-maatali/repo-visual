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
            feature = feature.upper()
        
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