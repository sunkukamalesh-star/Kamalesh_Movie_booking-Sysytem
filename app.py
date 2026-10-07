import streamlit as st
from datetime import datetime
import random


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Kamal_CineVerse",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# MOVIE DATA
# =========================================================

MOVIES = {
    "RRR": {
        "genre": "Action • Drama",
        "language": "Telugu",
        "duration": "3h 7m",
        "rating": "U/A",
        "description": "A fictional story of two legendary revolutionaries."
    },

    "Pushpa 2": {
        "genre": "Action • Drama",
        "language": "Telugu",
        "duration": "3h 21m",
        "rating": "A",
        "description": "Pushpa continues his journey against powerful enemies."
    },

    "Avengers: Endgame": {
        "genre": "Action • Sci-Fi",
        "language": "English",
        "duration": "3h 2m",
        "rating": "U/A",
        "description": "The Avengers unite for their final battle to save the universe."
    },

    "Interstellar": {
        "genre": "Sci-Fi • Adventure",
        "language": "English",
        "duration": "2h 49m",
        "rating": "U/A",
        "description": "Explorers travel through space searching for a new home."
    },

    "Jawan": {
        "genre": "Action • Thriller",
        "language": "Hindi",
        "duration": "2h 49m",
        "rating": "U/A",
        "description": "An action-packed story about justice and redemption."
    },

    "KGF Chapter 2": {
        "genre": "Action • Crime",
        "language": "Kannada",
        "duration": "2h 48m",
        "rating": "A",
        "description": "Rocky faces powerful enemies while protecting his empire."
    }
}


# =========================================================
# TICKET PRICES
# =========================================================

TICKET_PRICES = {
    "Regular": 180,
    "Premium": 280,
    "Recliner": 420
}


# =========================================================
# SHOW TIMES
# =========================================================

SHOW_TIMES = [
    "10:00 AM",
    "01:30 PM",
    "04:30 PM",
    "07:30 PM",
    "10:30 PM"
]


# =========================================================
# SCREENS
# =========================================================

SCREENS = [
    "Screen 1",
    "Screen 2",
    "Screen 3",
    "IMAX"
]


# =========================================================
# SESSION STATE
# =========================================================

if "booking" not in st.session_state:
    st.session_state.booking = None


# =========================================================
# FUNCTIONS
# =========================================================

def money(amount):
    return f"₹{amount:,.2f}"


def generate_booking_id():
    return f"CV-{random.randint(10000, 99999)}"


def reset_booking():
    st.session_state.booking = None


# =========================================================
# SIMPLE CINEMA STYLE
# =========================================================

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TOP HEADER
# =========================================================

top_left, top_right = st.columns([4, 1])

with top_left:
    st.title("🎬 kamalesh  CineVerse")
    st.caption("Your Movie. Your Seat. Your Experience.")

with top_right:
    st.metric("🎟️ Ticket Types", "3")


st.divider()


# =========================================================
# HERO / MOVIE SELECTION
# =========================================================

st.header("🍿 What's Playing?")

movie_names = list(MOVIES.keys())

selected_movie = st.selectbox(
    "Select Movie",
    movie_names
)

movie = MOVIES[selected_movie]


# =========================================================
# MOVIE INFORMATION
# =========================================================

movie_info_1, movie_info_2 = st.columns(
    [2, 1],
    gap="large"
)


with movie_info_1:

    with st.container(border=True):

        st.subheader(f"🎞️ {selected_movie}")

        st.write(movie["description"])

        st.divider()

        info1, info2, info3, info4 = st.columns(4)

        with info1:
            st.caption("GENRE")
            st.write(movie["genre"])

        with info2:
            st.caption("LANGUAGE")
            st.write(movie["language"])

        with info3:
            st.caption("DURATION")
            st.write(movie["duration"])

        with info4:
            st.caption("RATING")
            st.write(movie["rating"])


with movie_info_2:

    with st.container(border=True):

        st.subheader("⭐ Movie Details")

        st.write(f"**🎬 Movie**")
        st.write(selected_movie)

        st.write(f"**🌐 Language**")
        st.write(movie["language"])

        st.write(f"**⏱️ Duration**")
        st.write(movie["duration"])

        st.write(f"**🔞 Rating**")
        st.write(movie["rating"])


# =========================================================
# BOOKING AREA
# =========================================================

st.divider()

st.header("🎟️ Book Your Tickets")


booking_left, booking_right = st.columns(
    [1.5, 1],
    gap="large"
)


# =========================================================
# LEFT - SHOW DETAILS
# =========================================================

with booking_left:

    st.subheader("📅 Show Details")

    date_col, screen_col = st.columns(2)

    with date_col:

        selected_date = st.date_input(
            "Select Date"
        )

    with screen_col:

        selected_screen = st.selectbox(
            "Select Screen",
            SCREENS
        )


    st.write("### 🕐 Select Showtime")

    selected_time = st.radio(
        "Available Shows",
        SHOW_TIMES,
        horizontal=True
    )


    st.divider()

    st.subheader("💺 Choose Ticket Category")

    ticket_type = st.radio(
        "Ticket Category",
        list(TICKET_PRICES.keys()),
        horizontal=True
    )

    ticket_price = TICKET_PRICES[ticket_type]


    # Ticket information
    price1, price2, price3 = st.columns(3)

    with price1:

        st.metric(
            "Regular",
            money(TICKET_PRICES["Regular"])
        )

    with price2:

        st.metric(
            "Premium",
            money(TICKET_PRICES["Premium"])
        )

    with price3:

        st.metric(
            "Recliner",
            money(TICKET_PRICES["Recliner"])
        )


    st.divider()

    st.subheader("🔢 Number of Tickets")

    ticket_count = st.number_input(
        "How many tickets?",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )


# =========================================================
# RIGHT - LIVE ORDER SUMMARY
# =========================================================

with booking_right:

    st.subheader("🧾 Booking Summary")

    with st.container(border=True):

        st.write("### 🎬 Movie")

        st.write(
            f"**{selected_movie}**"
        )

        st.divider()

        st.write("📅 **Date**")

        st.write(
            selected_date.strftime("%d %B %Y")
        )

        st.write("🕐 **Show**")

        st.write(
            selected_time
        )

        st.write("🏢 **Screen**")

        st.write(
            selected_screen
        )

        st.write("💺 **Category**")

        st.write(
            ticket_type
        )

        st.write("🎟️ **Tickets**")

        st.write(
            ticket_count
        )

        st.divider()

        total_amount = ticket_price * ticket_count

        st.metric(
            "TOTAL",
            money(total_amount)
        )


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.divider()

st.header("👤 Customer Information")

customer_col1, customer_col2 = st.columns(2)

with customer_col1:

    customer_name = st.text_input(
        "Full Name",
        placeholder="Enter customer name"
    )

with customer_col2:

    customer_mobile = st.text_input(
        "Mobile Number",
        placeholder="Enter mobile number"
    )


# =========================================================
# CONFIRM BOOKING
# =========================================================

st.divider()

confirm_col1, confirm_col2, confirm_col3 = st.columns(
    [1, 2, 1]
)

with confirm_col2:

    if st.button(
        "🎫 CONFIRM & BOOK TICKETS",
        type="primary",
        use_container_width=True
    ):

        if not customer_name.strip():

            st.error(
                "Please enter customer name."
            )

        elif not customer_mobile.strip():

            st.error(
                "Please enter mobile number."
            )

        elif len(customer_mobile.strip()) < 10:

            st.error(
                "Please enter a valid mobile number."
            )

        else:

            booking_id = generate_booking_id()

            st.session_state.booking = {

                "booking_id": booking_id,

                "customer_name": customer_name,

                "customer_mobile": customer_mobile,

                "movie": selected_movie,

                "genre": movie["genre"],

                "language": movie["language"],

                "duration": movie["duration"],

                "rating": movie["rating"],

                "date": selected_date.strftime(
                    "%d %B %Y"
                ),

                "time": selected_time,

                "screen": selected_screen,

                "ticket_type": ticket_type,

                "ticket_price": ticket_price,

                "ticket_count": ticket_count,

                "total": total_amount,

                "created_at": datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                )
            }

            st.success(
                "🎉 Booking Confirmed!"
            )

            st.rerun()


# =========================================================
# CONFIRMED TICKET
# =========================================================

if st.session_state.booking is not None:

    booking = st.session_state.booking

    st.divider()

    st.header("🎫 Your Movie Ticket")

    ticket_left, ticket_right = st.columns(
        [2.5, 1],
        gap="large"
    )


    # =====================================================
    # TICKET INFORMATION
    # =====================================================

    with ticket_left:

        with st.container(border=True):

            st.title("🎬 CineVerse")

            st.subheader(
                booking["movie"]
            )

            st.caption(
                f"{booking['genre']} • "
                f"{booking['language']}"
            )

            st.divider()

            row1_col1, row1_col2 = st.columns(2)

            with row1_col1:

                st.write("**👤 CUSTOMER**")

                st.write(
                    booking["customer_name"]
                )

            with row1_col2:

                st.write("**📱 MOBILE**")

                st.write(
                    booking["customer_mobile"]
                )


            st.divider()


            row2_col1, row2_col2, row2_col3 = st.columns(3)

            with row2_col1:

                st.write("**📅 DATE**")

                st.write(
                    booking["date"]
                )

            with row2_col2:

                st.write("**🕐 SHOW**")

                st.write(
                    booking["time"]
                )

            with row2_col3:

                st.write("**🏢 SCREEN**")

                st.write(
                    booking["screen"]
                )


            st.divider()


            row3_col1, row3_col2, row3_col3 = st.columns(3)

            with row3_col1:

                st.write("**💺 CATEGORY**")

                st.write(
                    booking["ticket_type"]
                )

            with row3_col2:

                st.write("**🎟️ TICKETS**")

                st.write(
                    booking["ticket_count"]
                )

            with row3_col3:

                st.write("**💰 PRICE**")

                st.write(
                    money(booking["ticket_price"])
                )


    # =====================================================
    # TICKET SIDE PANEL
    # =====================================================

    with ticket_right:

        with st.container(border=True):

            st.subheader("🎟️ BOOKING ID")

            st.title(
                booking["booking_id"]
            )

            st.divider()

            st.caption("TOTAL PAYABLE")

            st.metric(
                "Amount",
                money(booking["total"])
            )

            st.divider()

            st.success(
                "✓ CONFIRMED"
            )

            st.caption(
                f"Booked on {booking['created_at']}"
            )


    # =====================================================
    # ACTIONS
    # =====================================================

    st.divider()

    action1, action2, action3 = st.columns(3)

    with action1:

        if st.button(
            "🖨️ Print Ticket",
            use_container_width=True
        ):

            st.info(
                "Use your browser Print option "
                "(Ctrl + P)."
            )

    with action2:

        if st.button(
            "📩 Booking Details",
            use_container_width=True
        ):

            st.info(
                f"Booking ID: {booking['booking_id']}"
            )

    with action3:

        if st.button(
            "🔄 New Booking",
            use_container_width=True
        ):

            reset_booking()
            st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎬 CineVerse • Movie Ticket Booking System"
)