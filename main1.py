from pyscript import document

club_info = {
    "guitar": {
        "description": "A fun and friendly space to jam, learn chords, and improve your guitar skills.",
        "meeting_time": "Every Monday, 2:00 to 3:00 PM",
        "location": "Room 221"
    }
}

def show_club_info(e=None):
    info = club_info["guitar"]

    document.querySelector(".club-description").innerHTML = "<div class='category-title'>Description</div>" + info["description"]
    document.querySelector(".club-time").innerHTML = "<div class='category-title'>Meeting Time</div>" + info["meeting_time"]
    document.querySelector(".club-location").innerHTML = "<div class='category-title'>Location</div>" + info["location"]


