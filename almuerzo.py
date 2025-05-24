import random

almuerzos = [
    "Milanesas con papas fritas", "Fideos con salsa bolognesa", "Arroz con pollo",
    "Ensalada César con pollo grillado", "Hamburguesas caseras", "Empanadas de carne",
    "Pizza de muzzarella", "Tacos de carne", "Sopa de verduras con croutons", "Lentejas guisadas",
    "Tarta de jamón y queso", "Pollo al horno con batatas", "Papas rellenas", "Wok de verduras y pollo",
    "Filet de merluza con puré", "Sándwich de milanesa", "Ñoquis con tuco", "Burritos vegetarianos",
    "Churrasco con ensalada mixta", "Polenta con salsa y queso", "Tortilla de papas", "Wraps de pollo y vegetales",
    "Lasagna de carne", "Fajitas mexicanas", "Arroz chaufa", "Pechuga grillada con arroz y ensalada",
    "Ravioles de ricota con crema", "Chili con carne", "Risotto de hongos", "Sopa de pollo con fideos"
]

print("🥗 Bienvenido al sugeridor de almuerzos.")
print("Presiona Enter para recibir una sugerencia, o escribí 'salir' para terminar.")

while True:
    entrada = input("👉 ")
    if entrada.lower() == "salir":
        print("¡Buen provecho! 🍽️")
        break
    else:
        print("😋 Hoy podés almorzar:", random.choice(almuerzos))
