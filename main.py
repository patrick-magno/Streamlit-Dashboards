import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="HBR - UBER Case Study Dashboard",
    page_icon="🚗",
    layout="wide"
)

# =============================================================================
# HEADER SECTION
# =============================================================================
col_left, col_center, col_right = st.columns([1, 3, 1])

with col_left:
    # Replace with your actual logo path or URL
    st.image("Uber-logo.png", width=120)
    st.markdown("**[Left Logo]**")

with col_center:
    st.markdown("<h1 style='text-align: center;'>HBR - UBER Case Study Dashboard</h1>", unsafe_allow_html=True)

with col_right:
    # Replace with your actual logo path or URL
    st.image("rice-logo.jpg", width=120)
    # st.markdown("**[Right Logo]**")

st.divider()

# =============================================================================
# TABS SECTION
# =============================================================================
tab1, tab2, tab3 = st.tabs(["📋 Metadata", "📖 Data Dictionary", "📊 Visualizations"])

# -----------------------------------------------------------------------------
# TAB 1: METADATA
# -----------------------------------------------------------------------------
with tab1:
    st.header("Case Study Metadata")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("General Information")
        metadata = {
            "Title": "Uber: Changing the Way the World Moves",
            "Publisher": "Harvard Business Review",
            "Case Number": "716-463",
            "Publication Date": "June 2016",
            "Revision Date": "August 2019",
            "Authors": "John Doe, Jane Smith",
            "Industry": "Transportation / Technology",
            "Geographic Scope": "Global"
        }
        
        for key, value in metadata.items():
            st.markdown(f"**{key}:** {value}")
    
    with col2:
        st.subheader("Study Overview")
        st.markdown("""
        This case study examines Uber's disruptive business model and its impact 
        on the traditional transportation industry. Key topics include:
        
        - Platform economics and network effects
        - Regulatory challenges and market entry strategies
        - Driver and rider dynamics
        - Competitive landscape analysis
        - Growth and expansion strategies
        """)
        
        st.subheader("Key Metrics")
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        metric_col1.metric("Data Points", "10,000+")
        metric_col2.metric("Time Period", "2010-2023")
        metric_col3.metric("Markets Covered", "50+")

# -----------------------------------------------------------------------------
# TAB 2: DATA DICTIONARY
# -----------------------------------------------------------------------------
with tab2:
    st.header("Data Dictionary")
    
    st.markdown("This section provides definitions and descriptions for all variables in the dataset.")
    
    data_dict = pd.DataFrame({
        "Variable Name": [
            "trip_id",
            "driver_id",
            "rider_id",
            "pickup_datetime",
            "dropoff_datetime",
            "pickup_location",
            "dropoff_location",
            "trip_distance",
            "fare_amount",
            "surge_multiplier",
            "payment_type",
            "rating"
        ],
        "Data Type": [
            "String",
            "String",
            "String",
            "Datetime",
            "Datetime",
            "String (Lat/Long)",
            "String (Lat/Long)",
            "Float",
            "Float",
            "Float",
            "Categorical",
            "Integer"
        ],
        "Description": [
            "Unique identifier for each trip",
            "Unique identifier for the driver",
            "Unique identifier for the rider",
            "Date and time when the trip started",
            "Date and time when the trip ended",
            "GPS coordinates of pickup point",
            "GPS coordinates of dropoff point",
            "Total distance traveled in miles",
            "Total fare charged in USD",
            "Dynamic pricing multiplier (1.0 = no surge)",
            "Payment method used (Card, Cash, Wallet)",
            "Rider rating for the trip (1-5 stars)"
        ],
        "Example Values": [
            "TRP_001234",
            "DRV_5678",
            "RDR_9012",
            "2023-01-15 08:30:00",
            "2023-01-15 08:52:00",
            "40.7128, -74.0060",
            "40.7580, -73.9855",
            "5.2",
            "24.50",
            "1.5",
            "Card",
            "5"
        ]
    })
    
    st.dataframe(data_dict, use_container_width=True, hide_index=True)
    
    st.subheader("Notes")
    st.info("""
    - All datetime fields are in UTC timezone
    - Distance is calculated using GPS coordinates
    - Fare amount includes base fare, distance, time, and surge pricing
    - Ratings are optional and may be null for some trips
    """)

# -----------------------------------------------------------------------------
# TAB 3: VISUALIZATIONS
# -----------------------------------------------------------------------------
with tab3:
    st.header("Data Visualizations")
    
    # Sample data for visualizations
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    trips_data = pd.DataFrame({
        'Month': months,
        'Total Trips': [95000, 102000, 98000, 115000, 125000, 140000,
                       135000, 142000, 130000, 120000, 118000, 145000],
        'Revenue ($M)': [3.2, 3.5, 3.3, 3.8, 4.1, 4.6, 
                        4.4, 4.7, 4.3, 4.0, 3.9, 4.8]
    })
    trips_data = trips_data.set_index('Month')
    
    # Row 1: Key Metrics
    st.subheader("Key Performance Indicators")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Trips", "1.2M", "+12%")
    kpi2.metric("Active Drivers", "45,230", "+8%")
    kpi3.metric("Avg Trip Duration", "18 min", "-2 min")
    kpi4.metric("Customer Satisfaction", "4.7/5", "+0.2")
    
    st.divider()
    
    # Row 2: Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Monthly Trip Volume")
        st.line_chart(trips_data['Total Trips'])
    
    with col2:
        st.subheader("Monthly Revenue")
        st.bar_chart(trips_data['Revenue ($M)'])
    
    # Row 3: Additional Charts
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Trip Distribution by Type")
        trip_types = pd.DataFrame({
            'Type': ['UberX', 'UberXL', 'Uber Black', 'Uber Pool', 'Uber Comfort'],
            'Trips': [450000, 200000, 100000, 150000, 100000]
        })
        trip_types = trip_types.set_index('Type')
        st.bar_chart(trip_types)
    
    with col4:
        st.subheader("Peak Hours Analysis")
        hours = [f"{h}:00" for h in range(24)]
        demand = [20, 15, 10, 8, 12, 25, 55, 85, 95, 75, 60, 55, 
                  65, 60, 55, 60, 75, 90, 95, 85, 70, 55, 40, 30]
        
        hourly_data = pd.DataFrame({
            'Hour': hours,
            'Demand Index': demand
        })
        hourly_data = hourly_data.set_index('Hour')
        st.area_chart(hourly_data)

# =============================================================================
# FOOTER
# =============================================================================
st.divider()
st.markdown(
    "<p style='text-align: center; color: #888;'>HBR - UBER Case Study Dashboard | Built with Streamlit</p>",
    unsafe_allow_html=True
)
