import json
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

class TicketGenerator:
    def __init__(self, stadiums_file, events_file, tickets_file, background_image_path, output_folder="tickets"):
        self.stadiums_file = stadiums_file
        self.events_file = events_file
        self.tickets_file = tickets_file
        self.background_image_path = background_image_path
        self.output_folder = output_folder

    def load_json(self, file_path):
        """Charge les données depuis un fichier JSON."""
        with open(file_path, 'r') as file:
            return json.load(file)

    def load_image(self, image_path):
        """Charge l'image de fond du billet."""
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"L'image de fond '{image_path}' n'existe pas.")
        return Image.open(image_path)

    def generate_ticket(self, ticket_data, background_image):
        """Génère un billet avec les informations fournies."""

        # Crée une copie de l'image de fond
        ticket_image = background_image.copy()
        draw = ImageDraw.Draw(ticket_image)

        # fonts
        paris_font = ImageFont.truetype("fonts/Paris2024.ttf", 22)
        Akshar = ImageFont.truetype("fonts/Akshar.ttf", 22)

        # Couleurs
        couleur_bleue = (51, 19, 104)
        couleur_blanche = (255, 255, 255)

       
        # Dessine sur le billet
        draw.text((40, 428), ticket_data['equipe_1'], fill=couleur_bleue, font=Akshar)
        draw.text((120, 502), ticket_data['equipe_2'], fill=couleur_bleue, font=Akshar)
        draw.text((70, 590), ticket_data['lieu'], fill=couleur_blanche, font=paris_font)
        draw.text((70, 657), ticket_data['start_datetime'].strftime("%Y-%m-%d %H:%M:%S"), fill=couleur_blanche, font=paris_font)
        
         # QR Code
        qr = qrcode.QRCode(box_size=4)
        qr.add_data(ticket_data['id'])
        qr.make(fit=True)
        qr_im = qr.make_image(fill_color=couleur_bleue, back_color=couleur_blanche)
        ticket_image.paste(qr_im, (126, 835))

        return ticket_image

    def generate_tickets(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # Chargement des données depuis les fichiers JSON
        stadiums_data = self.load_json(self.stadiums_file)
        events_data = self.load_json(self.events_file)
        tickets_data = self.load_json(self.tickets_file)

        # Chargement de l'image de fond du billet
        background_image = self.load_image(self.background_image_path)

        # Boucle sur chaque billet
        for ticket in tickets_data:
            event_id = ticket['event_id']
            
            event = next((event for event in events_data if event['id'] == event_id), None)
            if event:
                # Récupérer le stade associé à cet événement
                stadium_id = event['stadium_id']
                stadium = next((stadium for stadium in stadiums_data if stadium['id'] == stadium_id), None)
                if stadium:
                    # Date au format ISO
                    start_iso = event['start']
                    start_datetime = datetime.fromisoformat(start_iso)

                    # Ajout dans le dictionnaire du billet
                    ticket['equipe_1'] = event['team_home']
                    ticket['equipe_2'] = event['team_away']
                    ticket['lieu'] = f"{stadium['name']} - {stadium['location']}"
                    ticket['start_datetime'] = start_datetime

                    # Générer et sauvegarder le billet dans le dossier "tickets"
                    ticket_image = self.generate_ticket(ticket, background_image)
                    ticket_image.save(f"{self.output_folder}/{ticket['id']}.png")

# Utilisation de la classe TicketGenerator
if __name__ == "__main__":
    generator = TicketGenerator("stadiums.json", "events.json", "tickets.json", "ticketJo.png")
    generator.generate_tickets()
