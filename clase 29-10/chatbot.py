class  Chatbot:
    def __init__(self):
        self.options ={
            "inicio":{
                "mensaje": "Bienvenidos al chat de las hojitas ¿En que te puedo ayudar?"
                "opciones":[
                    "1. Producto",
                    "2. Contacto",
                    "3. Ubicacion",
                    "4. FAQ"
                ]
            },
            "productos":{
                "Hojas de Primavera",
                "Hoja de Otoño",
                "Hoja de Verano"
                },
            "Hojas de Verano":{
                "Hoja de Roble",
                "hojas de Sauce",
                },
            "Hojas de Primavera":{
                "Hojas de Sakura",
                "Hoja de Jacaranda",
                },
            "Hojas de Otoño" :{
                "Hoja de Palo Borracho",
                "Hoja de Abedul"
            }
        }
self.respuetas = {
    "producto_Roble" : "$8",
    "producto_Sauce" : "$7",
    "producto_Sakura" : "$14",
    "producto_Jacaranda" : "$12",
    "producto_PaloBorracho" : "$2",
    "producto_Abedul" : "$3",

}
    self.estado_actual = "inicio"



                    "1. No entiendo para que sirve la pagina",
                    "2. Cuantas hojas puedo comprar"