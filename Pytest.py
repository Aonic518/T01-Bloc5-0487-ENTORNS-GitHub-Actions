import pytest as p
from prova_escrita import trobar_edat_maxima,trobar_producte_mes_car,comptar_empleats_per_departament,productes

# ===== DADES DE PROVA =====
persones_1 = [
    {'nom':'Anna Garcia','edat':25},
    {'nom':'Marc Puig','edat':42},
    {'nom':'Laura Martí','edat':35},
    {'nom':'Jordi Soler','edat':58},
    {'nom':'Marta Vidal','edat':29},
    {'nom':'Pere Català','edat':67},
    {'nom':'Sofia Roca','edat':31}
] # Llista completa de persones

persones_2 = [] # Llista buida

persones_3 = [
    {'nom':'Anna Garcia','edat':25},
    {'nom':'Marc Puig'},
    {'nom':'Laura Martí','edat':35}
] # Llista amb diccionari incomplet

empresa_de_prova = {
    'nom':'TechCorp',
    'departaments': [
        {'nom':'Informàtica','empleats':[
            {'nom':'Anna Garcia','càrrec':'Desenvolupadora'},
            {'nom':'Marc Puig','càrrec':'Analista'},
            {'nom':'Laura Martí','càrrec':'DevOps'}
        ]},
        {'nom':'Recursos Humans','empleats':[
            {'nom':'Jordi Soler','càrrec':'Director RRHH'},
            {'nom':'Marta Vidal','càrrec':'Tècnica de selecció'}
        ]},
        {'nom':'Vendes','empleats':[
            {'nom':'Pere Català','càrrec':'Comercial'},
            {'nom':'Sofia Roca','càrrec':'Comercial'},
            {'nom':'David Llop','càrrec':'Cap de vendes'},
            {'nom':'Carla Font','càrrec':'Comercial'}
        ]},
        {'nom':'Administració','empleats':[
            {'nom':'Joan Ferrer','càrrec':'Comptable'}
        ]}
    ]
} # Empresa amb departaments i empleats

# ===== TESTS =====

@p.mark.parametrize("persones,res_esperat",[(persones_1,67),(persones_2,-1),(persones_3,-1)])
def test_trobar_edat_maxima(persones,res_esperat):
    resultat = trobar_edat_maxima(persones) # Cridem la funció amb les dades de prova
    assert resultat == res_esperat          # Comprovem que el resultat és correcte

@p.mark.parametrize("llista_productes,preu_esperat",[
    (
        [
            {'nom':'Portàtil Dell XPS 15','preu':1299.99,'categoria':'Informàtica','stock':5},
            {'nom':'Ratolí Logitech MX Master','preu':89.99,'categoria':'Perifèrics','stock':15},
            {'nom':'Monitor Samsung 27"','preu':349.50,'categoria':'Monitors','stock':8}
        ],
        1299.99
    ),
    ([], None)
])
def test_trobar_producte_mes_car(llista_productes,preu_esperat):
    productes.clear()                     # Netejem la llista global
    productes.extend(llista_productes)    # Afegim els productes de prova
    resultat = trobar_producte_mes_car()  # Cridem la funció
    if preu_esperat is None:             # Si esperem None, comprovem això
        assert resultat is None
    else:                                # Altrament, comprovem el preu màxim
        assert resultat["preu"] == preu_esperat

@p.mark.parametrize("empresa,res_esperat",[
    (empresa_de_prova, {'Informàtica':3,'Recursos Humans':2,'Vendes':4,'Administració':1}),
    ({'nom':'Buida','departaments':[]}, {})
])
def test_comptar_empleats_per_departament(empresa,res_esperat):
    resultat = comptar_empleats_per_departament(empresa) # Cridem la funció amb l’empresa de prova
    assert resultat == res_esperat                         # Comprovem que el resultat coincideix amb l’esperat

def test_error_edat_maxima():
    resultat = trobar_edat_maxima(persones_1)
    assert resultat == 100  # ❌ incorrecte (hauria de ser 67)

def test_error_tipus():
    resultat = trobar_edat_maxima(persones_1)
    assert isinstance(resultat, str)  # ❌ hauria de ser int


