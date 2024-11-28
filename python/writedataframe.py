#### LOG AUDITORIA 
from pyspark.sql import functions as F
from pyspark.sql.functions import col

data = []
data.append(
    {
        "timestamp": timestamp,
        "filler": filler,
        "approver": approver,
        "path": caminho,
        "subdomain": subdominio,
        "domain": dominio,
        "country": pais,
        "zone": zona,
        "status": status,
        "message": message,
        "reason": reason
    }
)
               
df = spark.createDataFrame(data)

ordered_df = df.select("filler", "approver", "zone", "country", "domain", "subdomain", "path", "timestamp", "status", "message", "reason")