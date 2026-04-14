import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SkyBook — Airline Seats",
    page_icon="✈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
#  STYLES
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0e1a !important;
    color: #e8eaf0 !important;
    font-family: 'Syne', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at 20% 10%, #1a2040 0%, #0a0e1a 60%) !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 2rem 2rem 4rem !important; max-width: 1200px !important; }

/* ── TYPOGRAPHY ── */
h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; }

/* ── FORM INPUTS ── */
input[type="text"], input[type="number"],
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] select,
div[data-baseweb="select"] {
    background: #111827 !important;
    border: 1px solid #2a3352 !important;
    border-radius: 8px !important;
    color: #e8eaf0 !important;
    font-family: 'DM Mono', monospace !important;
}

[data-testid="stTextInput"] > label,
[data-testid="stNumberInput"] > label,
[data-testid="stSelectbox"] > label,
[data-testid="stRadio"] > label {
    color: #7b8db0 !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    font-family: 'DM Mono', monospace !important;
}

/* ── BUTTONS ── */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}
[data-testid="stButton"] > button:hover {
    background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(37,99,235,0.4) !important;
}

/* ── DIVIDER ── */
hr { border-color: #1e2d4a !important; }

/* ── METRIC ── */
[data-testid="stMetric"] {
    background: #0f1729 !important;
    border: 1px solid #1e2d4a !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}
[data-testid="stMetricValue"] { color: #60a5fa !important; font-family: 'DM Mono', monospace !important; }
[data-testid="stMetricLabel"] { color: #7b8db0 !important; font-size: 0.75rem !important; }

/* ── RADIO ── */
[data-testid="stRadio"] div[role="radiogroup"] label {
    background: #111827 !important;
    border: 1px solid #2a3352 !important;
    border-radius: 8px !important;
    padding: 0.4rem 0.8rem !important;
    margin: 2px !important;
    color: #e8eaf0 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
}

/* ── SUCCESS / ERROR ── */
[data-testid="stSuccess"] { background: #052e16 !important; border: 1px solid #166534 !important; border-radius: 10px !important; }
[data-testid="stError"]   { background: #2d0a0a !important; border: 1px solid #7f1d1d !important; border-radius: 10px !important; }
[data-testid="stInfo"]    { background: #0c1a3a !important; border: 1px solid #1e3a6e !important; border-radius: 10px !important; }
[data-testid="stWarning"] { background: #2d1f00 !important; border: 1px solid #78350f !important; border-radius: 10px !important; }

/* ── EXPANDER ── */
[data-testid="stExpander"] {
    background: #0f1729 !important;
    border: 1px solid #1e2d4a !important;
    border-radius: 12px !important;
}

/* ── SEAT GRID ── */
.seat-grid-wrap {
    background: linear-gradient(180deg, #0f1729 0%, #0a0e1a 100%);
    border: 1px solid #1e2d4a;
    border-radius: 20px;
    padding: 2rem;
    position: relative;
    overflow: hidden;
}
.seat-grid-wrap::before {
    content: '';
    position: absolute;
    top: 0; left: 50%; transform: translateX(-50%);
    width: 120px; height: 6px;
    background: linear-gradient(90deg, transparent, #2563eb, transparent);
    border-radius: 0 0 50% 50%;
}
.plane-nose {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 1rem;
    filter: drop-shadow(0 0 12px rgba(96,165,250,0.5));
}
.col-labels {
    display: flex;
    justify-content: center;
    gap: 6px;
    margin-bottom: 8px;
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    color: #7b8db0;
    letter-spacing: 0.1em;
}
.col-label { width: 54px; text-align: center; }
.col-spacer { width: 28px; }
.seat-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    margin: 4px 0;
}
.row-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    color: #3d5280;
    width: 20px;
    text-align: right;
}
.aisle-gap { width: 28px; display: flex; align-items: center; justify-content: center; }
.aisle-line { width: 1px; height: 40px; background: linear-gradient(180deg, transparent, #1e2d4a, transparent); }

/* ── SEAT BUTTON ── */
.seat-btn {
    width: 54px; height: 44px;
    border-radius: 10px 10px 6px 6px;
    border: 1.5px solid transparent;
    cursor: pointer;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 1px;
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    transition: all 0.15s ease;
    position: relative;
    outline: none;
}
.seat-btn:hover:not(.seat-booked):not(.seat-selected) {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}
.seat-available {
    background: #1a2744;
    border-color: #2a3d6a;
    color: #8ba3cc;
}
.seat-available:hover {
    background: #1e3055 !important;
    border-color: #3b5ea6 !important;
    color: #c0d4f5 !important;
}
.seat-selected {
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    border-color: #60a5fa;
    color: white;
    box-shadow: 0 0 16px rgba(37,99,235,0.5);
    cursor: pointer;
}
.seat-booked {
    background: #1a0f0f;
    border-color: #3d1515;
    color: #5a2020;
    cursor: not-allowed;
}
.seat-free {
    background: linear-gradient(135deg, #064e3b, #065f46);
    border-color: #10b981;
    color: #6ee7b7;
}
.seat-free-selected {
    background: linear-gradient(135deg, #065f46, #047857);
    border-color: #34d399;
    color: white;
    box-shadow: 0 0 16px rgba(16,185,129,0.5);
    cursor: pointer;
}
.seat-id { font-size: 0.6rem; opacity: 0.8; }
.seat-price { font-size: 0.55rem; font-weight: 600; }

/* ── LEGEND ── */
.legend-grid {
    display: flex; gap: 16px; flex-wrap: wrap;
    justify-content: center;
    margin-top: 1.2rem;
    padding-top: 1.2rem;
    border-top: 1px solid #1e2d4a;
}
.legend-item {
    display: flex; align-items: center; gap: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem; color: #7b8db0;
}
.legend-dot {
    width: 14px; height: 14px;
    border-radius: 4px;
    border: 1.5px solid;
}

/* ── CART ── */
.cart-item {
    background: #0f1729;
    border: 1px solid #1e2d4a;
    border-radius: 10px;
    padding: 0.7rem 1rem;
    margin: 0.4rem 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
}
.cart-seat-id { color: #60a5fa; font-weight: 500; }
.cart-type    { color: #7b8db0; font-size: 0.72rem; }
.cart-price   { color: #34d399; font-weight: 600; }

/* ── HEADER ── */
.page-header {
    text-align: center;
    padding: 2.5rem 0 2rem;
}
.page-header h1 {
    font-size: 3rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #60a5fa, #818cf8, #a78bfa);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    letter-spacing: -0.02em !important;
}
.page-header p {
    color: #4a6080 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
    margin-top: 0.4rem !important;
    letter-spacing: 0.08em !important;
}

/* ── SECTION LABEL ── */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #3b5280;
    margin-bottom: 0.6rem;
}

/* ── STEP INDICATOR ── */
.step-pill {
    display: inline-block;
    background: #2563eb22;
    border: 1px solid #2563eb44;
    color: #60a5fa;
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 0.8rem;
}

/* ── TOTAL BAR ── */
.total-bar {
    background: linear-gradient(135deg, #0f1f3d, #0a1628);
    border: 1px solid #1e3a6e;
    border-radius: 14px;
    padding: 1.2rem 1.5rem;
    display: flex; justify-content: space-between; align-items: center;
}
.total-label { font-family: 'DM Mono', monospace; font-size: 0.75rem; color: #4a6080; letter-spacing: 0.1em; text-transform: uppercase; }
.total-amount { font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 800; color: #60a5fa; }

/* ── CONFIRMATION ── */
.confirm-card {
    background: linear-gradient(135deg, #052e16, #042015);
    border: 1px solid #166534;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
}
.confirm-card h2 { color: #4ade80; font-size: 1.5rem; font-weight: 800; }
.confirm-card p  { color: #86efac; font-family: 'DM Mono', monospace; font-size: 0.85rem; margin-top: 0.4rem; }
.booking-ref {
    font-family: 'DM Mono', monospace;
    font-size: 1.1rem;
    color: #34d399;
    background: #064e3b;
    border: 1px solid #10b981;
    border-radius: 8px;
    padding: 0.4rem 1rem;
    display: inline-block;
    margin-top: 0.8rem;
    letter-spacing: 0.15em;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  DATA  (same HashMap + UnionFind + 2D Array from Python script)
# ─────────────────────────────────────────────────────────────────────────────
ROWS = 5
COLS = ["A", "B", "C", "D", "E", "F"]
COL_TYPE = {"A": "window", "B": "middle", "C": "aisle", "D": "aisle", "E": "middle", "F": "window"}
SEAT_PRICES = {"window": 1500, "middle": 0, "aisle": 1200}   # middle = FREE

# Class-specific configs: fewer rows + fewer cols for premium classes
CLASS_CONFIG = {
    "Economy":     {"rows": 5, "cols": ["A","B","C","D","E","F"]},
    "Business":    {"rows": 3, "cols": ["A","C","D","F"]},    # skip middle seats; 4 cols
    "First Class": {"rows": 2, "cols": ["A","F"]},            # only window seats; 2 cols
}

def get_class_config(travel_class):
    return CLASS_CONFIG.get(travel_class, CLASS_CONFIG["Economy"])

def make_seats():
    """HashMap: seat_id -> seat_dict"""
    seats = {}
    for r in range(1, ROWS + 1):
        for c in COLS:
            sid = f"{r}{c}"
            t = COL_TYPE[c]
            seats[sid] = {
                "id":       sid,
                "row":      r,
                "col":      c,
                "type":     t,
                "price":    SEAT_PRICES[t],
                "booked":   False,
                "passenger": None,
            }
    return seats

def make_layout():
    """2D Array: layout[row][col_index] — full Economy layout"""
    return [[f"{r}{c}" for c in COLS] for r in range(1, ROWS + 1)]

def make_class_layout(travel_class):
    """2D Array filtered for the selected travel class"""
    cfg = get_class_config(travel_class)
    rows = cfg["rows"]
    cols = cfg["cols"]
    return [[f"{r}{c}" for c in cols] for r in range(1, rows + 1)]

# ── UnionFind ──────────────────────────────
class UF:
    def __init__(self): self.p = {}; self.rank = {}
    def make(self, x):
        if x not in self.p: self.p[x] = x; self.rank[x] = 0
    def find(self, x):
        if self.p[x] != x: self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return
        if self.rank[rx] < self.rank[ry]: rx, ry = ry, rx
        self.p[ry] = rx
        if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1
    def group(self, x):
        root = self.find(x)
        return [k for k in self.p if self.find(k) == root]

# ─────────────────────────────────────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def init_state():
    if "seats"              not in st.session_state: st.session_state.seats              = make_seats()
    if "layout"             not in st.session_state: st.session_state.layout             = make_layout()
    if "uf"                 not in st.session_state: st.session_state.uf                 = UF()
    if "step"               not in st.session_state: st.session_state.step               = 1
    if "user"               not in st.session_state: st.session_state.user               = {}
    if "selected"           not in st.session_state: st.session_state.selected           = set()
    if "bookings"           not in st.session_state: st.session_state.bookings           = []
    if "ref"                not in st.session_state: st.session_state.ref                = None
    if "all_booking_groups" not in st.session_state: st.session_state.all_booking_groups = []

init_state()

seats   = st.session_state.seats
layout  = st.session_state.layout
uf      = st.session_state.uf
sel     = st.session_state.selected
user    = st.session_state.user

# ─────────────────────────────────────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <h1>✈ SkyBook</h1>
  <p>AIRLINE SEAT RESERVATION SYSTEM</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  STEP 1 — USER DETAILS
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.step == 1:
    st.markdown('<div class="step-pill">STEP 01 / 03 — PASSENGER DETAILS</div>', unsafe_allow_html=True)

    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown('<div class="section-label">Flight Information</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            origin = st.selectbox("Origin", ["Mumbai (BOM)", "Delhi (DEL)", "Bangalore (BLR)", "Chennai (MAA)", "Hyderabad (HYD)", "Kolkata (CCU)"])
        with c2:
            dest   = st.selectbox("Destination", ["Dubai (DXB)", "Singapore (SIN)", "London (LHR)", "New York (JFK)", "Bangkok (BKK)", "Sydney (SYD)"])

        c3, c4 = st.columns(2)
        with c3:
            flight_no = st.text_input("Flight Number", value="SK-401")
        with c4:
            travel_class = st.selectbox("Class", ["Economy", "Business", "First Class"])

        st.markdown('<div class="section-label" style="margin-top:1.2rem">Passenger Details</div>', unsafe_allow_html=True)

        p_count = st.number_input("Number of Passengers", min_value=1, max_value=6, value=1)
        names = []
        for i in range(int(p_count)):
            n = st.text_input(f"Passenger {i+1} Full Name", key=f"pname_{i}", placeholder=f"e.g. {'Arul Kumar' if i==0 else 'Rahul Sharma'}")
            names.append(n)

        is_group = p_count > 1
        if is_group:
            pref = st.radio("Seat Preference for Group", ["No Preference", "Window", "Aisle", "Middle (Free!)"], horizontal=True)
        else:
            pref = st.radio("Seat Preference", ["No Preference", "Window", "Aisle", "Middle (Free!)"], horizontal=True)

        if st.button("Continue to Seat Selection →"):
            if all(n.strip() for n in names):
                st.session_state.user = {
                    "names": [n.strip() for n in names],
                    "origin": origin, "dest": dest,
                    "flight": flight_no, "class": travel_class,
                    "pref": pref.replace(" (Free!)", "").lower(),
                    "is_group": is_group,
                    "count": int(p_count),
                }
                st.session_state.step = 2
                st.rerun()
            else:
                st.error("Please fill in all passenger names.")

    with right:
        st.markdown('<div class="section-label">Seat Pricing</div>', unsafe_allow_html=True)
        st.markdown("""
<div style="background:#0f1729;border:1px solid #1e2d4a;border-radius:14px;padding:1.4rem;font-family:'DM Mono',monospace;">
  <div style="display:flex;justify-content:space-between;align-items:center;padding:0.7rem 0;border-bottom:1px solid #1e2d4a;">
    <div>
      <div style="color:#a78bfa;font-size:0.8rem;font-weight:600;">WINDOW</div>
      <div style="color:#4a6080;font-size:0.68rem;margin-top:2px;">Columns A &amp; F</div>
    </div>
    <div style="color:#e8eaf0;font-size:1.1rem;font-weight:700;">₹1,500</div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;padding:0.7rem 0;border-bottom:1px solid #1e2d4a;">
    <div>
      <div style="color:#f59e0b;font-size:0.8rem;font-weight:600;">AISLE</div>
      <div style="color:#4a6080;font-size:0.68rem;margin-top:2px;">Columns C &amp; D</div>
    </div>
    <div style="color:#e8eaf0;font-size:1.1rem;font-weight:700;">₹1,200</div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;padding:0.7rem 0;">
    <div>
      <div style="color:#10b981;font-size:0.8rem;font-weight:600;">MIDDLE</div>
      <div style="color:#4a6080;font-size:0.68rem;margin-top:2px;">Columns B &amp; E</div>
    </div>
    <div>
      <span style="color:#4ade80;font-size:1.1rem;font-weight:700;">FREE</span>
      <span style="color:#4a6080;font-size:0.65rem;margin-left:6px;">₹0</span>
    </div>
  </div>
</div>
<div style="margin-top:1rem;background:#0c1a3a;border:1px solid #1e3a6e;border-radius:12px;padding:1rem;font-family:'DM Mono',monospace;font-size:0.75rem;color:#4a6080;">
  <div style="color:#60a5fa;font-size:0.72rem;font-weight:600;margin-bottom:6px;">DATA STRUCTURES</div>
  <div style="margin:4px 0;">→ HashMap: O(1) seat lookup</div>
  <div style="margin:4px 0;">→ UnionFind: group clustering</div>
  <div style="margin:4px 0;">→ 2D Array: O(n²) map render</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  STEP 2 — SEAT MAP
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.step == 2:
    st.markdown('<div class="step-pill">STEP 02 / 03 — SELECT YOUR SEATS</div>', unsafe_allow_html=True)

    u = st.session_state.user
    needed = u["count"]

    # Flight info strip
    st.markdown(f"""
<div style="background:#0f1729;border:1px solid #1e2d4a;border-radius:12px;padding:0.9rem 1.4rem;
     display:flex;gap:2rem;flex-wrap:wrap;font-family:'DM Mono',monospace;font-size:0.78rem;color:#7b8db0;margin-bottom:1.4rem;">
  <span>✈ <b style="color:#e8eaf0">{u['flight']}</b></span>
  <span>🛫 <b style="color:#e8eaf0">{u['origin'].split('(')[0].strip()}</b> → <b style="color:#e8eaf0">{u['dest'].split('(')[0].strip()}</b></span>
  <span>🎫 <b style="color:#e8eaf0">{u['class']}</b></span>
  <span>👥 <b style="color:#e8eaf0">{', '.join(u['names'])}</b></span>
  <span>💺 Select <b style="color:#60a5fa">{needed}</b> seat(s)</span>
</div>
""", unsafe_allow_html=True)

    map_col, cart_col = st.columns([3, 2], gap="large")

    with map_col:
        # ── Determine layout based on travel class ──────────────
        travel_class = u.get("class", "Economy")
        cfg = get_class_config(travel_class)
        class_cols = cfg["cols"]
        class_layout = make_class_layout(travel_class)

        # Class section label & spacing hint
        class_labels = {
            "Economy":     ("ECONOMY CLASS", "5 rows · 6 seats per row", "#60a5fa"),
            "Business":    ("BUSINESS CLASS", "3 rows · 4 seats per row · extra legroom", "#a78bfa"),
            "First Class": ("FIRST CLASS", "2 rows · 2 seats per row · private suite", "#f59e0b"),
        }
        cls_title, cls_sub, cls_color = class_labels.get(travel_class, class_labels["Economy"])

        # Draw seat map using buttons
        st.markdown(f'''<div class="seat-grid-wrap">
<div style="text-align:center;margin-bottom:0.8rem;">
  <span style="font-family:\'DM Mono\',monospace;font-size:0.7rem;letter-spacing:0.15em;
    color:{cls_color};text-transform:uppercase;border:1px solid {cls_color}44;
    background:{cls_color}11;padding:3px 12px;border-radius:20px;">{cls_title}</span>
  <div style="font-family:\'DM Mono\',monospace;font-size:0.65rem;color:#3d5280;margin-top:6px;">{cls_sub}</div>
</div>''', unsafe_allow_html=True)
        st.markdown('<div class="plane-nose">✈</div>', unsafe_allow_html=True)

        # Column headers — only for the active class cols
        # Determine if there's an aisle gap (only when both C and D are present)
        has_aisle = "C" in class_cols and "D" in class_cols
        aisle_after = class_cols.index("C") if has_aisle else -1

        header_html = '<div class="col-labels">'
        header_html += '<div style="width:20px"></div>'  # row num spacer
        for i, c in enumerate(class_cols):
            header_html += f'<div class="col-label">{c}</div>'
            if has_aisle and i == aisle_after:
                header_html += '<div class="col-spacer"></div>'
        header_html += '</div>'
        st.markdown(header_html, unsafe_allow_html=True)

        # Build streamlit column widths based on class
        if travel_class == "Economy":
            col_widths = [0.4] + [1]*3 + [0.5] + [1]*3
        elif travel_class == "Business":
            # A  C | D  F  with wider gaps for spacing
            col_widths = [0.4, 1, 1, 0.8, 1, 1]
        else:
            # First Class: A  (big gap)  F
            col_widths = [0.4, 1, 2, 1]

        # Build seat_col_map: maps seat index in row → col index in cols_ui
        # For Economy: skip index 4 (aisle spacer)
        # For Business: skip index 3 (aisle spacer)
        # For First Class: skip index 2 (spacer)
        if travel_class == "Economy":
            seat_col_map = [1, 2, 3, 5, 6, 7]
        elif travel_class == "Business":
            seat_col_map = [1, 2, 4, 5]
        else:
            seat_col_map = [1, 3]

        # Row spacing: add vertical margin between rows for premium classes
        row_margin = {"Economy": "4px", "Business": "12px", "First Class": "22px"}.get(travel_class, "4px")

        for r_idx, row in enumerate(class_layout):
            row_num = r_idx + 1
            st.markdown(f'<div style="margin-top:{row_margin}"></div>', unsafe_allow_html=True)
            cols_ui = st.columns(col_widths, gap="small")

            cols_ui[0].markdown(
                f'<div style="text-align:right;font-family:DM Mono,monospace;font-size:0.75rem;color:#3d5280;padding-top:8px">{row_num}</div>',
                unsafe_allow_html=True
            )

            for c_idx, sid in enumerate(row):
                seat = seats[sid]
                ui_col = cols_ui[seat_col_map[c_idx]]

                is_sel    = sid in sel
                is_booked = seat["booked"]
                is_middle = seat["type"] == "middle"
                price_str = "(free)" if is_middle else f"₹{seat['price']}"

                if is_booked:
                    ui_col.button(f"✗\n{sid}", key=f"s_{sid}", disabled=True, help="Booked")
                else:
                    label = f"{'✓' if is_sel else sid}\n{price_str}"
                    if ui_col.button(label, key=f"s_{sid}", help=f"Seat {sid} | {seat['type'].title()} | {price_str}"):
                        if sid in sel:
                            sel.discard(sid)
                        else:
                            if len(sel) < needed:
                                sel.add(sid)
                            else:
                                st.warning(f"You can only select {needed} seat(s). Deselect one first.")
                        st.rerun()

        # Legend
        st.markdown("""
<div class="legend-grid">
  <div class="legend-item"><div class="legend-dot" style="background:#1a2744;border-color:#2a3d6a"></div>Available</div>
  <div class="legend-item"><div class="legend-dot" style="background:#1d4ed8;border-color:#60a5fa"></div>Selected</div>
  <div class="legend-item"><div class="legend-dot" style="background:#1a0f0f;border-color:#3d1515"></div>Booked</div>
  <div class="legend-item"><div class="legend-dot" style="background:#064e3b;border-color:#10b981"></div>Middle (Free)</div>
  <div class="legend-item" style="margin-left:8px;color:#4a6080;font-size:0.68rem;">A,F=Window · B,E=Middle · C,D=Aisle</div>
</div>
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)  # close seat-grid-wrap

        # ── Preferred auto-select button ──
        pref = u.get("pref", "no preference")
        valid_ids = {sid for row in class_layout for sid in row}
        if pref not in ("no preference", "") and len(sel) < needed:
            if st.button(f"⚡ Auto-select {pref} seats"):
                avail = [s for s in seats.values() if not s["booked"] and s["type"] == pref and s["id"] not in sel and s["id"] in valid_ids]
                for s in avail[:needed - len(sel)]:
                    sel.add(s["id"])
                st.rerun()

    with cart_col:
        st.markdown('<div class="section-label">Your Selection</div>', unsafe_allow_html=True)

        if not sel:
            st.markdown('<div style="color:#3d5280;font-family:DM Mono,monospace;font-size:0.82rem;text-align:center;padding:2rem 0;">No seats selected yet</div>', unsafe_allow_html=True)
        else:
            sel_list = sorted(sel)
            passengers = u["names"]
            total = 0
            for i, sid in enumerate(sel_list):
                s = seats[sid]
                pname = passengers[i] if i < len(passengers) else f"Passenger {i+1}"
                price = s["price"]
                total += price
                price_disp = "FREE" if price == 0 else f"₹{price:,}"
                type_badge_color = {"window":"#a78bfa","middle":"#10b981","aisle":"#f59e0b"}[s["type"]]
                st.markdown(f"""
<div class="cart-item">
  <div>
    <div class="cart-seat-id">{sid}</div>
    <div class="cart-type" style="color:{type_badge_color}">{s['type'].upper()}</div>
    <div style="color:#4a6080;font-size:0.7rem;margin-top:2px">{pname}</div>
  </div>
  <div class="cart-price">{price_disp}</div>
</div>
""", unsafe_allow_html=True)

            st.markdown(f"""
<div class="total-bar" style="margin-top:1rem">
  <div class="total-label">Total Amount</div>
  <div class="total-amount">₹{total:,}</div>
</div>
""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Savings note for middle seats
        middle_selected = [sid for sid in sel if seats[sid]["type"] == "middle"]
        if middle_selected:
            savings = len(middle_selected) * 1000
            st.info(f"🎉 You're saving **₹{savings:,}** by choosing middle seat(s)!")

        # Back button
        if st.button("← Back"):
            st.session_state.step = 1
            st.session_state.selected = set()
            st.rerun()

        # Confirm button
        if len(sel) == needed:
            if st.button("✅ Confirm Booking →"):
                import random, string
                ref = "SK" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
                booked_list = []
                sel_sorted = sorted(sel)
                for i, sid in enumerate(sel_sorted):
                    s = seats[sid]
                    s["booked"] = True
                    s["passenger"] = u["names"][i] if i < len(u["names"]) else f"P{i+1}"
                    uf.make(sid)
                    booked_list.append({"seat_id": sid, "passenger": s["passenger"], "price": s["price"], "type": s["type"]})

                # Union group
                if len(sel_sorted) > 1:
                    for i in range(1, len(sel_sorted)):
                        uf.union(sel_sorted[0], sel_sorted[i])

                st.session_state.bookings = booked_list
                st.session_state.ref = ref
                st.session_state.selected = set()

                # ── Persist group for UnionFind visualiser ──
                GROUP_COLORS = ["#6366f1","#10b981","#f59e0b","#ef4444","#a78bfa","#06b6d4","#f472b6","#84cc16"]
                color = GROUP_COLORS[len(st.session_state.all_booking_groups) % len(GROUP_COLORS)]
                st.session_state.all_booking_groups.append({
                    "ref":        ref,
                    "seats":      sel_sorted,
                    "passengers": [u["names"][i] if i < len(u["names"]) else f"P{i+1}" for i in range(len(sel_sorted))],
                    "root":       sel_sorted[0],
                    "color":      color,
                })

                st.session_state.step = 3
                st.rerun()
        else:
            remaining = needed - len(sel)
            st.markdown(f'<div style="color:#3d5280;font-family:DM Mono,monospace;font-size:0.78rem;text-align:center;padding:0.5rem">Select {remaining} more seat(s)</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  STEP 3 — CONFIRMATION
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.step == 3:
    st.markdown('<div class="step-pill">STEP 03 / 03 — BOOKING CONFIRMED</div>', unsafe_allow_html=True)

    bk   = st.session_state.bookings
    ref  = st.session_state.ref
    u    = st.session_state.user
    total = sum(b["price"] for b in bk)

    st.markdown(f"""
<div class="confirm-card">
  <h2>🎉 Booking Confirmed!</h2>
  <p>Your seats have been reserved successfully.</p>
  <div class="booking-ref">{ref}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown('<div class="section-label">Booking Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div style="background:#0f1729;border:1px solid #1e2d4a;border-radius:14px;padding:1.2rem 1.5rem;
     font-family:'DM Mono',monospace;font-size:0.8rem;color:#7b8db0;margin-bottom:1rem;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.6rem;">
    <div>Flight</div><div style="color:#e8eaf0">{u['flight']}</div>
    <div>Route</div><div style="color:#e8eaf0">{u['origin'].split('(')[0].strip()} → {u['dest'].split('(')[0].strip()}</div>
    <div>Class</div><div style="color:#e8eaf0">{u['class']}</div>
    <div>Reference</div><div style="color:#60a5fa">{ref}</div>
  </div>
</div>
""", unsafe_allow_html=True)

        for b in bk:
            type_color = {"window":"#a78bfa","middle":"#10b981","aisle":"#f59e0b"}[b["type"]]
            price_disp = "FREE" if b["price"] == 0 else f"₹{b['price']:,}"
            st.markdown(f"""
<div class="cart-item">
  <div>
    <div class="cart-seat-id">{b['seat_id']}</div>
    <div class="cart-type" style="color:{type_color}">{b['type'].upper()}</div>
    <div style="color:#4a6080;font-size:0.7rem;margin-top:2px">{b['passenger']}</div>
  </div>
  <div class="cart-price">{price_disp}</div>
</div>
""", unsafe_allow_html=True)

        st.markdown(f"""
<div class="total-bar" style="margin-top:1rem">
  <div class="total-label">Amount Paid</div>
  <div class="total-amount">₹{total:,}</div>
</div>
""", unsafe_allow_html=True)

        middle_count = sum(1 for b in bk if b["type"] == "middle")
        if middle_count:
            st.success(f"💚 You saved **₹{middle_count * 1000:,}** on middle seats (booked for free)!")

        # Group info via UnionFind
        if len(bk) > 1:
            root_seat = bk[0]["seat_id"]
            group_seats = uf.group(root_seat)
            st.info(f"👨‍👩‍👧 Group cluster (UnionFind): {', '.join(sorted(group_seats))}")

    with right:
        st.markdown('<div class="section-label">Seat Statistics</div>', unsafe_allow_html=True)
        total_booked = sum(1 for s in seats.values() if s["booked"])
        total_avail  = 30 - total_booked
        revenue      = sum(s["price"] for s in seats.values() if s["booked"])

        m1, m2 = st.columns(2)
        m1.metric("Seats Booked", total_booked)
        m2.metric("Seats Free", total_avail)
        st.metric("Total Revenue", f"₹{revenue:,}")

    # ── UnionFind Visual Cluster Panel ─────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label" style="font-size:0.8rem;color:#60a5fa;letter-spacing:0.12em;">⬡ UNIONFIND — GROUP CLUSTER VISUALISER</div>', unsafe_allow_html=True)

    all_groups = st.session_state.all_booking_groups
    if not all_groups:
        st.markdown('<div style="color:#3d5280;font-family:DM Mono,monospace;font-size:0.8rem;text-align:center;padding:1.5rem;background:#0f1729;border:1px solid #1e2d4a;border-radius:14px;">No group bookings yet — book 2+ seats to see clusters</div>', unsafe_allow_html=True)
    else:
        # Map seat → group color and root
        seat_color_map = {}
        seat_root_map  = {}
        for g in all_groups:
            for sid in g["seats"]:
                seat_color_map[sid] = g["color"]
                seat_root_map[sid]  = g["root"]

        # ── Section A: Mini plane seat grid coloured by group ──
        st.markdown("""
<div style="background:#0f1729;border:1px solid #1e2d4a;border-radius:16px;padding:1.5rem 1.5rem 1rem;">
  <div style="font-family:'DM Mono',monospace;font-size:0.68rem;letter-spacing:0.12em;color:#3b5280;text-transform:uppercase;margin-bottom:1rem;">
    ▸ Plane Seat Map — Group Colour Coding (&#9733; = Root)
  </div>
""", unsafe_allow_html=True)

        col_header = '<div style="display:flex;gap:5px;justify-content:center;font-family:DM Mono,monospace;font-size:0.65rem;color:#3d5280;margin-bottom:4px;">'
        col_header += '<div style="width:18px"></div>'
        for i, c in enumerate(COLS):
            col_header += f'<div style="width:36px;text-align:center;">{c}</div>'
            if i == 2: col_header += '<div style="width:12px"></div>'
        col_header += '</div>'
        st.markdown(col_header, unsafe_allow_html=True)

        for r in range(1, ROWS + 1):
            row_html = '<div style="display:flex;gap:5px;justify-content:center;align-items:center;margin:3px 0;">'
            row_html += f'<div style="width:18px;font-family:DM Mono,monospace;font-size:0.6rem;color:#3d5280;text-align:right;">{r}</div>'
            for i, c in enumerate(COLS):
                sid = f"{r}{c}"
                s   = seats[sid]
                if sid in seat_color_map:
                    col   = seat_color_map[sid]
                    is_rt = (sid == seat_root_map.get(sid))
                    border = f"2px solid white" if is_rt else f"2px solid {col}"
                    bg     = f"{col}55" if is_rt else f"{col}22"
                    label  = "★" if is_rt else sid
                    txt_col = "white" if is_rt else col
                    row_html += f'<div title="{sid}" style="width:36px;height:30px;border-radius:6px 6px 4px 4px;background:{bg};border:{border};display:flex;align-items:center;justify-content:center;font-family:DM Mono,monospace;font-size:0.55rem;color:{txt_col};font-weight:600;">{label}</div>'
                elif s["booked"]:
                    row_html += '<div style="width:36px;height:30px;border-radius:6px 6px 4px 4px;background:#1a0f0f;border:1.5px solid #3d1515;display:flex;align-items:center;justify-content:center;font-family:DM Mono,monospace;font-size:0.55rem;color:#5a2020;">✗</div>'
                else:
                    row_html += f'<div style="width:36px;height:30px;border-radius:6px 6px 4px 4px;background:#1a2744;border:1.5px solid #2a3d6a;display:flex;align-items:center;justify-content:center;font-family:DM Mono,monospace;font-size:0.55rem;color:#3d5280;">{sid}</div>'
                if i == 2: row_html += '<div style="width:12px"></div>'
            row_html += '</div>'
            st.markdown(row_html, unsafe_allow_html=True)

        legend_html = '<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:1rem;padding-top:0.8rem;border-top:1px solid #1e2d4a;">'
        for g in all_groups:
            names_short = ", ".join(n.split()[0] for n in g["passengers"])
            legend_html += f'<div style="display:flex;align-items:center;gap:5px;background:{g["color"]}18;border:1px solid {g["color"]}55;border-radius:20px;padding:3px 10px;">'
            legend_html += f'<div style="width:8px;height:8px;border-radius:50%;background:{g["color"]}"></div>'
            legend_html += f'<span style="font-family:DM Mono,monospace;font-size:0.65rem;color:{g["color"]};">{g["ref"]}</span>'
            legend_html += f'<span style="font-family:DM Mono,monospace;font-size:0.6rem;color:#4a6080;"> · {names_short}</span>'
            legend_html += '</div>'
        legend_html += '</div>'
        st.markdown(legend_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Section B: UnionFind Tree per group ──
        st.markdown("""
<div style="background:#0f1729;border:1px solid #1e2d4a;border-radius:16px;padding:1.5rem;">
  <div style="font-family:'DM Mono',monospace;font-size:0.68rem;letter-spacing:0.12em;color:#3b5280;text-transform:uppercase;margin-bottom:1.2rem;">
    ▸ UnionFind Tree Structure — Root Node &amp; Children
  </div>
""", unsafe_allow_html=True)

        for g in all_groups:
            seats_in_group = g["seats"]
            root           = g["root"]
            color          = g["color"]
            passengers     = g["passengers"]
            n              = len(seats_in_group)

            svg_w    = max(420, n * 100)
            svg_h    = 175
            cx_root  = svg_w // 2
            cy_root  = 42
            r_node   = 24
            cy_child = 125
            spacing  = svg_w / (n + 1)
            child_xs = [int(spacing * (i + 1)) for i in range(n)]

            edges_svg = ""
            nodes_svg = ""

            for i, sid in enumerate(seats_in_group):
                cx = child_xs[i]
                edges_svg += f'<line x1="{cx_root}" y1="{cy_root + r_node}" x2="{cx}" y2="{cy_child - r_node}" stroke="{color}" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="5 3"/>'

            pname_root = passengers[seats_in_group.index(root)].split()[0] if root in seats_in_group else ""
            nodes_svg += f"""
<circle cx="{cx_root}" cy="{cy_root}" r="{r_node}" fill="{color}44" stroke="{color}" stroke-width="2.5"/>
<text x="{cx_root}" y="{cy_root - 6}" text-anchor="middle" fill="{color}" font-family="DM Mono,monospace" font-size="11" font-weight="700">{root}</text>
<text x="{cx_root}" y="{cy_root + 9}" text-anchor="middle" fill="white" font-family="DM Mono,monospace" font-size="8">ROOT</text>
<text x="{cx_root}" y="{cy_root - 36}" text-anchor="middle" fill="{color}" font-family="DM Mono,monospace" font-size="9" opacity="0.8">{pname_root}</text>
"""

            for i, sid in enumerate(seats_in_group):
                cx      = child_xs[i]
                pname   = passengers[i].split()[0] if i < len(passengers) else ""
                is_rt   = sid == root
                fill_c  = f"{color}44" if is_rt else f"{color}1a"
                nodes_svg += f"""
<circle cx="{cx}" cy="{cy_child}" r="{r_node}" fill="{fill_c}" stroke="{color}" stroke-width="1.5"/>
<text x="{cx}" y="{cy_child - 5}" text-anchor="middle" fill="{color}" font-family="DM Mono,monospace" font-size="10" font-weight="600">{sid}</text>
<text x="{cx}" y="{cy_child + 9}" text-anchor="middle" fill="#7b8db0" font-family="DM Mono,monospace" font-size="8">{pname}</text>
<text x="{cx}" y="{cy_child + 38}" text-anchor="middle" fill="#3d5280" font-family="DM Mono,monospace" font-size="7.5">find()={root}</text>
"""

            svg = f'''<svg viewBox="0 0 {svg_w} {svg_h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:{svg_w}px;">{edges_svg}{nodes_svg}</svg>'''

            st.markdown(f"""
<div style="background:{color}0a;border:1px solid {color}2a;border-radius:12px;padding:1rem 1.2rem;margin-bottom:1rem;">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.4rem;">
    <div style="width:10px;height:10px;border-radius:50%;background:{color};flex-shrink:0;"></div>
    <span style="font-family:DM Mono,monospace;font-size:0.72rem;color:{color};letter-spacing:0.1em;">GROUP · {g["ref"]}</span>
    <span style="font-family:DM Mono,monospace;font-size:0.65rem;color:#3d5280;"> · {n} seat(s) · root = {root}</span>
  </div>
  {svg}
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="margin-top:0.8rem;padding:0.9rem 1rem;background:#0c1a3a;border:1px solid #1e3a6e;border-radius:10px;font-family:'DM Mono',monospace;font-size:0.72rem;color:#4a6080;line-height:1.6;">
  <span style="color:#60a5fa;font-weight:600;">UnionFind</span> uses
  <span style="color:#a78bfa;">path compression</span> + <span style="color:#a78bfa;">union by rank</span>
  → each find() runs in <span style="color:#34d399;">O(α(n)) ≈ O(1)</span> amortised time.
  Seats in the same booking share a <span style="color:#60a5fa;">root</span> after union operations.
  ★ marks the root node in the tree above.
</div>
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✈ Book Another Journey"):
        st.session_state.step = 1
        st.session_state.user = {}
        st.session_state.selected = set()
        st.session_state.bookings = []
        st.session_state.ref = None
        st.rerun()
