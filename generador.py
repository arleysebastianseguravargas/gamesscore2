class Generador:
    def generaTabla(self, itemTabla):
        tabla=""
        td=""
        for i in itemTabla:
            tr1= "<tr>"
            for j in i.split(","):
                td = td + "<td>" + j + "</td>"
            tr2 =  "</tr>"

            tabla = tabla + tr1 +td + tr2
            td = ""
        return "<table>" + tabla + "</table>"