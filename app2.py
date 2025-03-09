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

def check_customfield_13303(file1, file2):
    """Vérifie si le champ customfield_13303 est identique dans les deux fichiers."""
    data1 = read_json_file(file1)
    data2 = read_json_file(file2)

    if "error" in data1:
        return data1
    if "error" in data2:
        return data2

    customfield_13303_1 = data1.get("fields", {}).get("customfield_13303", "null")
    customfield_13303_2 = data2.get("fields", {}).get("customfield_13303", "null")

    return customfield_13303_1 == customfield_13303_2

def check_customfield_13601(file1, file2):
    """Vérifie si le champ customfield_13601 est égal à 'SANITY' dans les deux fichiers."""
    data1 = read_json_file(file1)
    data2 = read_json_file(file2)

    if "error" in data1:
        return data1
    if "error" in data2:
        return data2

    customfield_13601_1 = data1.get("fields", {}).get("customfield_13601", "null")
    customfield_13601_2 = data2.get("fields", {}).get("customfield_13601", "null")

    if isinstance(customfield_13601_1, list):
        customfield_13601_1 = customfield_13601_1[0] if customfield_13601_1 else "null"
    if isinstance(customfield_13601_2, list):
        customfield_13601_2 = customfield_13601_2[0] if customfield_13601_2 else "null"

    return customfield_13601_1 == "SANITY" and customfield_13601_2 == "SANITY"

def compare_test_statuses(file1, file2, output_comparison_file):
    """Compare les statuts des testKey entre deux fichiers JSON et génère un fichier de comparaison."""
    data1 = read_json_file(file1)
    data2 = read_json_file(file2)

    if "error" in data1:
        return data1
    if "error" in data2:
        return data2

    # Créer un dictionnaire pour stocker les statuts par testKey
    status_dict1 = {item["testKey"]: item["status"] for item in data1}
    status_dict2 = {item["testKey"]: item["status"] for item in data2}

    # Identifier les testKey dont le statut a changé
    comparison_data = []
    for test_key in status_dict1:
        if test_key in status_dict2:
            if status_dict1[test_key] != status_dict2[test_key]:
                comparison_data.append({
                    "testKey": test_key,
                    "status_file1": status_dict1[test_key],
                    "status_file2": status_dict2[test_key]
                })

    # Écrire les résultats de la comparaison dans un fichier JSON
    with open(output_comparison_file, "w", encoding="utf-8") as f:
        json.dump(comparison_data, f, ensure_ascii=False, indent=4)

    return comparison_data

def process_dashboard2(file1, file2, output_file1, output_file2, output_comparison_file):
    """Traite les fichiers d'exécution pour le deuxième dashboard et génère un fichier de comparaison."""
    test_execution_folder = "test execution"
    test_cases_folder = "test cases"
    defects_folder = "testCase Defects"

    for folder in [test_execution_folder, test_cases_folder, defects_folder]:
        if not os.path.exists(folder):
            return {"error": f"Le dossier '{folder}' n'existe pas."}

    # Vérification des champs customfield_13303 et customfield_13601
    if not check_customfield_13303(file1, file2):
        return {"error": "Le champ customfield_13303 n'est pas identique dans les deux fichiers."}
    
    if not check_customfield_13601(file1, file2):
        return {"error": "Le champ customfield_13601 n'est pas égal à 'SANITY' dans les deux fichiers."}

    # Traitement des fichiers d'exécution
    result1 = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file1, output_file1)
    result2 = extract_test_data(test_execution_folder, test_cases_folder, defects_folder, file2, output_file2)

    # Comparaison des statuts entre les deux fichiers
    comparison_result = compare_test_statuses(output_file1, output_file2, output_comparison_file)

    return result1, result2, comparison_result

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print(json.dumps({"error": "Usage : python app.py <FILE1> <FILE2> <OUTPUT_JSON1> <OUTPUT_JSON2> <OUTPUT_COMPARISON_JSON>"}))
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file1 = sys.argv[3]
    output_file2 = sys.argv[4]
    output_comparison_file = sys.argv[5]

    result = process_dashboard2(file1, file2, output_file1, output_file2, output_comparison_file)
    print(json.dumps(result, ensure_ascii=False, indent=4))