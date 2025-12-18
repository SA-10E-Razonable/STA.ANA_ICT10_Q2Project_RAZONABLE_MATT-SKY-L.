from pyscript import display, document

# Guitar Club Information
guitar_club_info = {
    "description": "A friendly space to jam and learn new chords!",
    "time": "Every Monday, 2:00 to 3:00 PM",
    "location": "Room 221"
}

# Function to populate and display the Guitar Club info
def populateClubInfo():
    # Prepare content for the yellow box
    content = f"""
    <div style="font-size: 20px; color: black;">
        <p style="font-weight: bold; color: #5D16B5;"><strong>Description:</strong> {guitar_club_info['description']}</p>
        <p style="font-weight: bold; color: #5D16B5;"><strong>Time:</strong> {guitar_club_info['time']}</p>
        <p style="font-weight: bold; color: #5D16B5;"><strong>Location:</strong> {guitar_club_info['location']}</p>
    </div>
    <a href="#" class="btn" style="background-color: #ffde59; color: black; padding: 12px 25px; font-weight: bold; font-size: 18px; text-decoration: none; border-radius: 5px; display: block; margin-top: 15px; text-align: center;">
        Join the Club
    </a>
    """

    # Insert the content into the yellow box
    document.getElementById("club-info-container").innerHTML = content

# Call the function to populate and display the content when the page loads
populateClubInfo()