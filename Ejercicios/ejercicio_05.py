heroes_info = [
    {
                "Nombre":"Super Girl",
                "ID": 1,
                "Origen": "Krypton",
                "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
                "Identidad": "Kara Zor-El"
    },
    {
                "Nombre":"Shazam",
                "ID": 25,
                "Origen": "Tierra",
                "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
                "Identidad": "Billy Batson",
    },
    {
                "Nombre":"Power Girl",
                "ID": 14,
                "Origen": "Krypton",
                "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
                "Identidad": "Karen Starr"
    },
    {
                "Nombre":"Wonder Woman",
                "ID": 29,
                "Origen": "Amazonia",
                "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
                "Identidad": "Diana Prince"
    }
]



for heroe in heroes_info:
    id = heroe ["ID"]
    nombre = heroe["Nombre"]
    identidad = heroe["Identidad"]
    origen = heroe["Origen"]
    s = set (heroe["Habilidades"])
    habilidad = heroe["Habilidades"]

    print(f"ID: {id}, Codename: {nombre}\nIdentidad: {identidad} Su origen es: {origen}\nHabilidades: {s}")




