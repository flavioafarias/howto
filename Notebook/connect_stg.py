# Databricks notebook source
# DBTITLE 1,Conexão e Montagem do Volume no Storage Account
# MAGIC %python
# MAGIC 
# MAGIC dbutils.fs.mount(
# MAGIC   source = "wasbs://stg-ss-databricks@dp200stg.blob.core.windows.net",
# MAGIC   mount_point = "/mnt/stg-ss-databricks",
# MAGIC   extra_configs = {"fs.azure.account.key.dp200stg.blob.core.windows.net":
# MAGIC                    dbutils.secrets.get(
# MAGIC                      scope = "secret-scope-databricks", 
# MAGIC                      key = "secret-databricks")})

# COMMAND ----------

# DBTITLE 1,Validando os objetos no Volume
display(dbutils.fs.ls("/mnt/stg-ss-databricks"))

# COMMAND ----------

# DBTITLE 1,Removendo a conexão com o Volume
dbutils.fs.unmount("/mnt/stg-ss-databricks")
