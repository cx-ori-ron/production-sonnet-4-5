def asdff(string: str) -> str: 
    con = pyodbc.connect(Trusted_Connection='yes', driver='{SQL Server}', server='MACHINE\SQLEXPRESS', database='Testing') 
    cursor = con.cursor() 
    cursor.execute("SELECT @@VERSION;") 
    version_info = cursor.fetchone() 
    print(f"SQL Server Version: {version_info[0]}") 
    f = open("capitallog.log", "w") 
    f.write(f"SQL Server Version: {version_info[0]}") 
    f.close() 
