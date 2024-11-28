from pyspark.dbutils import DBUtils
import json
import requests

def delete_blobs(path):
    try:
        if not path.endswith('/'):
            path += '/'
        
        dbutils_instance = DBUtils(spark)
        blobs = dbutils_instance.fs.ls(path)
        
        for blob in blobs:
            blob_path = blob.path
            if blob.isDir():
                delete_blobs(blob_path)
            dbutils_instance.fs.rm(blob_path)
        
        # Remove the directory itself after its contents have been deleted
        dbutils_instance.fs.rm(path)
        
        return {"status": "success", "message": f"Blobs deletados no caminho: {path}"}
    
    except Exception as e:
        return {"status": "error", "message": f"Erro ao deletar blobs: {str(e)[:200]}..."}

def send_status_to_webhook(status, message):
    webhook_url = "" ##put your webhook URL, you can find this in a stateless logicapp

    data = {
        "status": status,
        "message": message,
        "zona": zona,
        "pais": pais,
        "dominio": dominio,
        "subdominio": subdominio,
        "caminho": caminho,
        "approver": approver,
        "filler": filler,
        "timestamp": timestamp,
        "reason": reason
    }
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        return data
    except requests.exceptions.RequestException as e:
        error_message = f"Erro ao enviar para o webhook: {str(e)}..."  
        print(error_message)
        return {"status": "error", "message": error_message}

mnt = "mnt"
zona = dbutils.widgets.get("zona")
pais = dbutils.widgets.get("pais")
dominio = dbutils.widgets.get("dominio")
subdominio = dbutils.widgets.get("subdominio")
caminho = dbutils.widgets.get("caminho").replace(" ", "")
approver = dbutils.widgets.get("approver")
filler = dbutils.widgets.get("filler")
timestamp = dbutils.widgets.get("timestamp")
reason = dbutils.widgets.get("reason")

if not caminho:
    result = {"status": "error", "message": "O caminho não foi preenchido. Não é permitido apagar a nível de subdominio. Operação abortada."}
else:
    if caminho.startswith('/'):
        caminho = caminho[1:]

    relative_path = f"{mnt}/{zona}/{pais}/{dominio}/{subdominio}/{caminho}"
    result = delete_blobs(relative_path)

status = result["status"]
message = result["message"]

webhook_response = send_status_to_webhook(status, message)

print(json.dumps(webhook_response))