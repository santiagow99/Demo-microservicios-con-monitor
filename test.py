from collections import Counter
candidatos = [{"nombre":"andres", "profesion":"profesor"}, {"nombre":"santiago", "profesion":"profesor"},
              {"nombre":"thomas", "profesion":"doctor"}, {"nombre":"pablo", "profesion":"doctor"}, {"nombre":"yesica", "profesion":"escritor"}]


profesiones = min([x["age"] for x in candidatos])
print(profesiones)