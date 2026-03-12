import streamlit as st

st.set_page_config(
    page_title="The Fantasy Book Oracle",
    page_icon="🐉",
    layout="centered"
)

# --- CUSTOM FANTASY CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Cormorant+Garamond:wght@400;500;600&display=swap');

/* Main app background */
.stApp {
    background: radial-gradient(circle at top, #1a1a1a 0%, #0b0b0b 45%, #000000 100%);
    color: #f5e6b3;
    font-family: 'Cormorant Garamond', serif;
}

/* Main content block */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

/* Headers */
h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: #d4af37 !important;
    text-align: center;
    letter-spacing: 1px;
}

h1 {
    font-size: 3rem !important;
    text-shadow: 0 0 12px rgba(212, 175, 55, 0.35);
    margin-bottom: 0.2rem;
}

h2, h3 {
    text-shadow: 0 0 8px rgba(212, 175, 55, 0.2);
}

/* Paragraph text */
p, label, div, span {
    font-family: 'Cormorant Garamond', serif !important;
    color: #f5e6b3 !important;
    font-size: 1.1rem;
}

/* Dropdowns */
div[data-baseweb="select"] > div {
    background-color: #111111 !important;
    border: 1px solid #5c4720 !important;
    border-radius: 10px !important;
    color: #f5e6b3 !important;
}

/* Slider */
.stSlider > div > div > div > div {
    color: #d4af37 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #1a1a1a, #2c220f);
    color: #f5e6b3;
    border: 1px solid #d4af37;
    border-radius: 12px;
    padding: 0.6rem 1.4rem;
    font-size: 1.05rem;
    font-family: 'Cinzel', serif;
    box-shadow: 0 0 12px rgba(212, 175, 55, 0.18);
    transition: all 0.25s ease-in-out;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #d4af37, #8f6b16);
    color: #000000 !important;
    border: 1px solid #f5e6b3;
    box-shadow: 0 0 18px rgba(212, 175, 55, 0.4);
}

/* Success / info boxes */
div[data-testid="stAlert"] {
    background-color: #111111 !important;
    border: 1px solid #5c4720 !important;
    border-radius: 12px !important;
    color: #f5e6b3 !important;
}

/* Horizontal line */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #d4af37, transparent);
    margin-top: 2rem;
    margin-bottom: 2rem;
}

/* Custom card styling */
.fantasy-card {
    background: linear-gradient(180deg, rgba(20,20,20,0.96), rgba(9,9,9,0.98));
    border: 1px solid #5c4720;
    border-radius: 18px;
    padding: 1.2rem 1.2rem 1rem 1.2rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 0 14px rgba(212, 175, 55, 0.08);
}

.fantasy-card h3 {
    text-align: left !important;
    margin-top: 0;
    margin-bottom: 0.5rem;
}

.oracle-intro {
    text-align: center;
    font-size: 1.25rem;
    color: #f3deb0;
    margin-bottom: 1.5rem;
}

.small-note {
    text-align: center;
    color: #c9b37a;
    font-size: 1rem;
    margin-top: -0.5rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("<h1>🐉 The Fantasy Book Oracle</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='oracle-intro'>Choose your fate, and the oracle will reveal your next obsession.</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='small-note'>Exact matches rise first, but near-matches may still be foretold.</div>",
    unsafe_allow_html=True
)

# --- BOOK DATA ---
books = [
    {"title": "Fourth Wing", "author": "Rebecca Yarros", "type": "Dragon", "mood": "Intense", "length": "Long", "romance": "High", "description": "Brutal training, dragons, danger, and addictive romance."},
    {"title": "Iron Flame", "author": "Rebecca Yarros", "type": "Dragon", "mood": "Intense", "length": "Long", "romance": "High", "description": "Higher stakes, bigger secrets, and even more emotional chaos."},
    {"title": "Onyx Storm", "author": "Rebecca Yarros", "type": "Dragon", "mood": "Epic", "length": "Long", "romance": "High", "description": "More dragons, more danger, and more emotional tension in the Empyrean world."},
    {"title": "A Court of Thorns and Roses", "author": "Sarah J. Maas", "type": "Fae", "mood": "Romantic", "length": "Medium", "romance": "High", "description": "A magical fae world full of tension, danger, and romance."},
    {"title": "A Court of Mist and Fury", "author": "Sarah J. Maas", "type": "Fae", "mood": "Emotional", "length": "Long", "romance": "High", "description": "Healing, power, emotional depth, and iconic romance."},
    {"title": "A Court of Wings and Ruin", "author": "Sarah J. Maas", "type": "Fae", "mood": "Epic", "length": "Long", "romance": "High", "description": "War, alliances, and huge fantasy stakes wrapped in romance."},
    {"title": "Throne of Glass", "author": "Sarah J. Maas", "type": "Epic", "mood": "Adventurous", "length": "Medium", "romance": "Medium", "description": "An assassin, a competition, and the start of a giant fantasy journey."},
    {"title": "Crown of Midnight", "author": "Sarah J. Maas", "type": "Epic", "mood": "Intense", "length": "Medium", "romance": "Medium", "description": "Darker secrets, rising danger, and emotional tension."},
    {"title": "Heir of Fire", "author": "Sarah J. Maas", "type": "Epic", "mood": "Emotional", "length": "Long", "romance": "Medium", "description": "Transformation, grief, growth, and power."},
    {"title": "Queen of Shadows", "author": "Sarah J. Maas", "type": "Epic", "mood": "Intense", "length": "Long", "romance": "Medium", "description": "Revenge, power, and a darker fantasy edge."},
    {"title": "Empire of Storms", "author": "Sarah J. Maas", "type": "Epic", "mood": "Epic", "length": "Long", "romance": "Medium", "description": "Massive world-building, war, alliances, and magic."},
    {"title": "Kingdom of Ash", "author": "Sarah J. Maas", "type": "Epic", "mood": "Emotional", "length": "Long", "romance": "Medium", "description": "A huge emotional finale with sacrifice, war, and heart."},
    {"title": "House of Earth and Blood", "author": "Sarah J. Maas", "type": "Urban Fantasy", "mood": "Emotional", "length": "Long", "romance": "Medium", "description": "A modern fantasy mystery with grief, friendship, and magic."},
    {"title": "House of Sky and Breath", "author": "Sarah J. Maas", "type": "Urban Fantasy", "mood": "Intense", "length": "Long", "romance": "Medium", "description": "Danger, emotional tension, and high-stakes urban fantasy."},
    {"title": "The Serpent and the Wings of Night", "author": "Carissa Broadbent", "type": "Dark Fantasy", "mood": "Intense", "length": "Medium", "romance": "High", "description": "Deadly trials, vampires, and dark romantic tension."},
    {"title": "The Ashes and the Star-Cursed King", "author": "Carissa Broadbent", "type": "Dark Fantasy", "mood": "Emotional", "length": "Long", "romance": "High", "description": "Longing, grief, power struggles, and dark emotion."},
    {"title": "Daughter of No Worlds", "author": "Carissa Broadbent", "type": "Dark Fantasy", "mood": "Emotional", "length": "Long", "romance": "High", "description": "Healing, magic, trauma, and deeply emotional fantasy."},
    {"title": "Powerless", "author": "Lauren Roberts", "type": "Romantasy", "mood": "Romantic", "length": "Medium", "romance": "High", "description": "Competition, banter, danger, and strong romantic tension."},
    {"title": "Reckless", "author": "Lauren Roberts", "type": "Romantasy", "mood": "Intense", "length": "Medium", "romance": "High", "description": "A dramatic continuation full of chemistry and danger."},
    {"title": "Divine Rivals", "author": "Rebecca Ross", "type": "Fantasy Romance", "mood": "Emotional", "length": "Medium", "romance": "High", "description": "War, magical letters, lyrical writing, and heartfelt romance."},
    {"title": "Ruthless Vows", "author": "Rebecca Ross", "type": "Fantasy Romance", "mood": "Emotional", "length": "Medium", "romance": "High", "description": "A beautiful sequel with longing, conflict, and heart."},
    {"title": "Once Upon a Broken Heart", "author": "Stephanie Garber", "type": "Magical", "mood": "Dreamy", "length": "Medium", "romance": "High", "description": "Whimsical magic, curses, fate, and fairytale energy."},
    {"title": "The Ballad of Never After", "author": "Stephanie Garber", "type": "Magical", "mood": "Romantic", "length": "Medium", "romance": "High", "description": "Charm, longing, and magical fantasy romance."},
    {"title": "Caraval", "author": "Stephanie Garber", "type": "Magical", "mood": "Dreamy", "length": "Medium", "romance": "Medium", "description": "Mystery, illusion, and whimsical fantasy spectacle."},
    {"title": "Legendary", "author": "Stephanie Garber", "type": "Magical", "mood": "Dreamy", "length": "Medium", "romance": "Medium", "description": "Glamour, mystery, and magical sequel energy."},
    {"title": "A Game of Thrones", "author": "George R. R. Martin", "type": "Epic", "mood": "Dark", "length": "Long", "romance": "Low", "description": "Political fantasy packed with betrayal, war, and power."},
    {"title": "A Clash of Kings", "author": "George R. R. Martin", "type": "Epic", "mood": "Dark", "length": "Long", "romance": "Low", "description": "Kingdoms collide in a brutal political war."},
    {"title": "Fire & Blood", "author": "George R. R. Martin", "type": "Dragon", "mood": "Dark", "length": "Long", "romance": "Low", "description": "The Targaryen history behind House of the Dragon."},
    {"title": "The Hobbit", "author": "J. R. R. Tolkien", "type": "Adventure", "mood": "Cozy", "length": "Medium", "romance": "Low", "description": "A warm, magical adventure with comfort and wonder."},
    {"title": "The Fellowship of the Ring", "author": "J. R. R. Tolkien", "type": "Epic", "mood": "Adventurous", "length": "Long", "romance": "Low", "description": "A legendary quest full of depth, heart, and world-building."},
    {"title": "The Two Towers", "author": "J. R. R. Tolkien", "type": "Epic", "mood": "Adventurous", "length": "Long", "romance": "Low", "description": "A sweeping continuation of an epic fantasy journey."},
    {"title": "The Return of the King", "author": "J. R. R. Tolkien", "type": "Epic", "mood": "Epic", "length": "Long", "romance": "Low", "description": "A triumphant and emotional fantasy conclusion."},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "type": "Epic", "mood": "Dreamy", "length": "Long", "romance": "Medium", "description": "Lyrical storytelling, legend, talent, and mystery."},
    {"title": "The Priory of the Orange Tree", "author": "Samantha Shannon", "type": "Dragon", "mood": "Epic", "length": "Long", "romance": "Medium", "description": "Dragons, politics, powerful women, and a sweeping fantasy world."},
    {"title": "A Day of Fallen Night", "author": "Samantha Shannon", "type": "Dragon", "mood": "Epic", "length": "Long", "romance": "Medium", "description": "Rich world-building, dragons, and high-stakes fantasy."},
    {"title": "One Dark Window", "author": "Rachel Gillig", "type": "Dark Fantasy", "mood": "Dark", "length": "Medium", "romance": "Medium", "description": "Gothic atmosphere, eerie magic, and haunting tension."},
    {"title": "Two Twisted Crowns", "author": "Rachel Gillig", "type": "Dark Fantasy", "mood": "Dark", "length": "Medium", "romance": "Medium", "description": "Dark magic, gothic vibes, and a haunting sequel."},
    {"title": "An Ember in the Ashes", "author": "Sabaa Tahir", "type": "Epic", "mood": "Intense", "length": "Medium", "romance": "Medium", "description": "Brutal stakes, resistance, and emotional intensity."},
    {"title": "From Blood and Ash", "author": "Jennifer L. Armentrout", "type": "Romantasy", "mood": "Romantic", "length": "Long", "romance": "High", "description": "Secrets, danger, fantasy politics, and intense chemistry."},
    {"title": "The Cruel Prince", "author": "Holly Black", "type": "Fae", "mood": "Dark", "length": "Medium", "romance": "Medium", "description": "Cruel court politics, tension, and sharp fantasy intrigue."},
    {"title": "The Wicked King", "author": "Holly Black", "type": "Fae", "mood": "Dark", "length": "Medium", "romance": "Medium", "description": "Manipulation, attraction, and dangerous power games."},
    {"title": "The Queen of Nothing", "author": "Holly Black", "type": "Fae", "mood": "Romantic", "length": "Medium", "romance": "Medium", "description": "A satisfying fae finale with politics and romance."},
    {"title": "The Invisible Life of Addie LaRue", "author": "V. E. Schwab", "type": "Fantasy Romance", "mood": "Dreamy", "length": "Long", "romance": "Medium", "description": "A haunting, beautiful fantasy about memory, art, and loneliness."},
    {"title": "Sorcery of Thorns", "author": "Margaret Rogerson", "type": "Magical", "mood": "Adventurous", "length": "Medium", "romance": "Medium", "description": "Living grimoires, sorcery, and charming magical adventure."},
    {"title": "Belladonna", "author": "Adalyn Grace", "type": "Dark Fantasy", "mood": "Dreamy", "length": "Medium", "romance": "Medium", "description": "Gothic mystery, deathly magic, and romantic tension."},
    {"title": "Emily Wilde's Encyclopaedia of Faeries", "author": "Heather Fawcett", "type": "Fae", "mood": "Cozy", "length": "Medium", "romance": "Medium", "description": "Cozy, clever, and magical with scholarly faerie charm."},
    {"title": "When the Moon Hatched", "author": "Sarah A. Parker", "type": "Dragon", "mood": "Dreamy", "length": "Long", "romance": "High", "description": "Lush fantasy atmosphere, dragons, and romantic ache."}
]

# --- USER INPUTS ---
fantasy_type = st.selectbox(
    "Choose a fantasy type:",
    ["Any", "Dragon", "Fae", "Epic", "Dark Fantasy", "Urban Fantasy", "Romantasy", "Adventure", "Magical", "Fantasy Romance"]
)

mood = st.selectbox(
    "Choose a mood:",
    ["Any", "Intense", "Romantic", "Emotional", "Adventurous", "Dark", "Cozy", "Dreamy", "Epic"]
)

length = st.selectbox(
    "Choose a book length:",
    ["Any", "Medium", "Long"]
)

romance = st.selectbox(
    "Choose a romance level:",
    ["Any", "High", "Medium", "Low"]
)

num_results = st.slider("How many prophecies do you want?", 1, 10, 5)

# --- MATCHING LOGIC ---
if st.button("🔮 Reveal My Books"):
    selected_preferences = {
        "type": fantasy_type,
        "mood": mood,
        "length": length,
        "romance": romance
    }

    active_preferences = {k: v for k, v in selected_preferences.items() if v != "Any"}
    total_possible = len(active_preferences)

    scored_books = []

    for book in books:
        score = 0
        matched_categories = []

        for category, user_choice in active_preferences.items():
            if book[category] == user_choice:
                score += 1
                matched_categories.append(category)

        if total_possible == 0:
            match_percent = 100
        else:
            match_percent = int((score / total_possible) * 100)

        if total_possible == 0 or score > 0:
            scored_books.append((score, match_percent, book, matched_categories))

    scored_books.sort(
        key=lambda x: (x[0], x[1], x[2]["title"]),
        reverse=True
    )

    top_books = scored_books[:num_results]

    st.markdown("---")
    st.subheader("✨ The Oracle Speaks")

    if top_books:
        if total_possible == 0:
            st.info("You left every category open, so the oracle pulled a general selection from the realm.")
        else:
            st.info(f"Your books are ranked by how well they match your chosen preferences.")

        category_labels = {
            "type": "Fantasy Type",
            "mood": "Mood",
            "length": "Length",
            "romance": "Romance"
        }

        for score, match_percent, book, matched_categories in top_books:
            if matched_categories:
                matched_text = ", ".join(category_labels[c] for c in matched_categories)
            else:
                matched_text = "General realm recommendation"

            st.markdown(
                f"""
                <div class="fantasy-card">
                    <h3>📖 {book['title']}</h3>
                    <p><strong>Author:</strong> {book['author']}</p>
                    <p><strong>Fantasy Type:</strong> {book['type']}</p>
                    <p><strong>Mood:</strong> {book['mood']}</p>
                    <p><strong>Length:</strong> {book['length']}</p>
                    <p><strong>Romance Level:</strong> {book['romance']}</p>
                    <p><em>{book['description']}</em></p>
                    <p>✨ <strong>Match:</strong> {match_percent}%</p>
                    <p>🔖 <strong>Matched:</strong> {matched_text}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.warning("The oracle found nothing. Try choosing different preferences.")