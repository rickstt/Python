import pymysql 
import matplotlib.pyplot as plt

# Estabelecer a comunicação com o banco de dados que está no container
con = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="senac@123",
    database="dignadb",
    port=6556
    )

dep = []
vlr = []

cur = con.cursor()
cur.execute("""
SELECT depSolicitado, COUNT(depSolicitado) AS `status` FROM chamado WHERE statusChamado='Pendente' GROUP BY depSolicitado
""")
resultado = cur.fetchall()
for i in resultado:
    dep.append(i[0])
    vlr.append(i[1])

cur.close

plt.figure().set_figwidth(30)
plt.figure().set_figheight(5)
plt.bar(dep,vlr)
plt.xlabel("Departamento")
plt.ylabel("Valores")
plt.savefig("/usr/share/nginx/html/dep_vlr.png")


pagina = """
<html>
    <head>
    <title>Gráfico de Produto</title>
    </head>
    <body>
        <img src="dep_vlr.png">
    </body>
</html>
"""

arquivo = open('/usr/share/nginx/html/dep_vlr.html','w')
arquivo.write(pagina)
arquivo.close()