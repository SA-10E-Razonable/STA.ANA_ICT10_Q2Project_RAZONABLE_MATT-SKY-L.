from pyscript import display, document

club_info = {
    "guitar": {
        "description": "A fun and friendly space to jam, learn chords, and improve your guitar skills.",
        "meeting_time": "Every Monday, 2:00 to 3:00 PM",
        "location": "Room 221"
    }
}

def show_club_info(e):
    info = club_info["guitar"]
    
    output = (
        "<div style='display:flex; font-family:Playfair Display, serif;'>"
            
            "<div style='width:50%; padding-right:30px;'>"
                "<div style='color:#FF5733; font-size:36px; font-weight:bold; margin-bottom:10px;'>Description</div>"
                f"<div style='font-size:28px; color:#1C1C1C;'>{info['description']}</div>"
            "</div>"

            "<div style='width:50%; padding-left:30px;'>"
                "<div style='color:#FF5733; font-size:32px; font-weight:bold; margin-bottom:5px;'>Meeting Time</div>"
                f"<div style='font-size:26px; color:#1C1C1C;'>{info['meeting_time']}</div>"
                
                "<div style='color:#FF5733; font-size:32px; font-weight:bold; margin-top:15px; margin-bottom:5px;'>Location</div>"
                f"<div style='font-size:26px; color:#1C1C1C;'>{info['location']}</div>"
            "</div>"
        "</div>"
    )
    
    display(output, target="club-info-container")

js.populateClubInfo = populateClubInfo

