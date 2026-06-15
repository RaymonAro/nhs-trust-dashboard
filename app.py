import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Enforce Clean App Page Setup
st.set_page_config(page_title="NHS Trust Advanced Analytics Hub", layout="wide")
st.title("🏥 NHS Trust Advanced Analytics & Predictive Hub")

# 2. Complete Independent Local Data Processing Matrix
@st.cache_data
def load_data():
    columns = ["TRUST_CD", "TRUST_NM", "TRUST_NM_LONG", "CAL_CD", "CAL_NM", "ICB_CD", "ICB_NM", "NHSER_CD", "NHSER_NM", "LAT", "LONG", "country"]
    data_rows = [
        ["NYG","Sussex Dermatology Service","SUSSEX DERMATOLOGY SERVICE","E56000011","Kent and Medway","E54000032","Kent and Medway","E40000005","South East",50.81932,-0.36458,"United Kingdom"],
        ["R0A","Manchester University","MANCHESTER UNIVERSITY NHS FOUNDATION TRUST","E56000032","Greater Manchester","E54000057","Greater Manchester","E40000010","North West",53.46244,-2.22771,"United Kingdom"],
        ["R0B","South Tyneside and Sunderland","SOUTH TYNESIDE AND SUNDERLAND NHS FOUNDATION TRUST","E56000029","Northern","E54000050","North East and North Cumbria","E40000012","North East and Yorkshire",54.90221,-1.41033,"United Kingdom"],
        ["R0D","University Dorset","UNIVERSITY HOSPITALS DORSET NHS FOUNDATION TRUST","E56000016","Wessex","E54000041","Dorset","E40000006","South West",50.72199,-1.97312,"United Kingdom"],
        ["R1F","Isle of Wight","ISLE OF WIGHT NHS TRUST","E56000016","Wessex","E54000042","Hampshire and Isle of Wight","E40000005","South East",50.71084,-1.30133,"United Kingdom"],
        ["R1H","Barts","BARTS HEALTH NHS TRUST","E56000028","North East London","E54000029","North East London","E40000003","London",51.51717,-0.05605,"United Kingdom"],
        ["R1K","London North West University","LONDON NORTH WEST UNIVERSITY HEALTHCARE NHS TRUST","E56000021","RM Partners West London","E54000027","North West London","E40000003","London",51.57541,-0.32204,"United Kingdom"],
        ["RA2","Royal Surrey County","ROYAL SURREY COUNTY HOSPITAL NHS FOUNDATION TRUST","E56000012","Surrey and Sussex","E54000063","Surrey Heartlands","E40000005","South East",51.24102,-0.60746,"United Kingdom"],
        ["RA7","Bristol Trusts (Combined)","BRISTOL TRUSTS (COMBINED SUBMISSION)","E56000033","Somerset, Wiltshire, Avon and Gloucestershire","E54000039","Bristol North Somerset and South Gloucestershire","E40000006","South West",51.45948,-2.59302,"United Kingdom"],
        ["RA9","Torbay and South Devon","TORBAY AND SOUTH DEVON NHS FOUNDATION TRUST","E56000014","Peninsula","E54000037","Devon","E40000006","South West",50.48232,-3.5538,"United Kingdom"],
        ["RAE","Bradford","BRADFORD TEACHING HOSPITALS NHS FOUNDATION TRUST","E56000030","West Yorkshire and Harrogate","E54000054","West Yorkshire","E40000012","North East and Yorkshire",53.80598,-1.7947,"United Kingdom"],
        ["RAJ","Mid and South Essex","MID AND SOUTH ESSEX NHS FOUNDATION TRUST","E56000035","East of England","E54000026","Mid and South Essex","E40000007","East of England",51.55384,0.688617,"United Kingdom"],
        ["RAL","Royal Free London","ROYAL FREE LONDON NHS FOUNDATION TRUST","E56000027","North Central London","E54000028","North Central London","E40000003","London",51.55322,-0.16532,"United Kingdom"],
        ["RAN","Royal National Orthopaedic","ROYAL NATIONAL ORTHOPAEDIC HOSPITAL NHS TRUST","E56000027","North Central London","E54000028","North Central London","E40000003","London",51.63256,-0.31044,"United Kingdom"],
        ["RAS","Hillingdon","THE HILLINGDON HOSPITALS NHS FOUNDATION TRUST","E56000021","RM Partners West London","E54000027","North West London","E40000003","London",51.52608,-0.46117,"United Kingdom"],
        ["RAX","Kingston","KINGSTON HOSPITAL NHS FOUNDATION TRUST","E56000021","RM Partners West London","E54000031","South West London","E40000003","London",51.41483,-0.2826,"United Kingdom"],
        ["RBD","Dorset County","DORSET COUNTY HOSPITAL NHS FOUNDATION TRUST","E56000016","Wessex","E54000041","Dorset","E40000006","South West",50.71294,-2.44694,"United Kingdom"],
        ["RBK","Walsall","WALSALL HEALTHCARE NHS TRUST","E56000007","West Midlands","E54000062","Black Country","E40000011","Midlands",52.58233,-1.99892,"United Kingdom"],
        ["RBL","Wirral University","WIRRAL UNIVERSITY TEACHING HOSPITAL NHS FOUNDATION TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.36964,-3.09682,"United Kingdom"],
        ["RBN","Mersey and West Lancashire","MERSEY AND WEST LANCASHIRE TEACHING HOSPITALS NHS TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.42047,-2.78495,"United Kingdom"],
        ["RBS","Alder Hey Children's","ALDER HEY CHILDREN'S NHS FOUNDATION TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.42024,-2.89872,"United Kingdom"],
        ["RBT","Mid Cheshire","MID CHESHIRE HOSPITALS NHS FOUNDATION TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.11768,-2.47586,"United Kingdom"],
        ["RBV","Christie","THE CHRISTIE NHS FOUNDATION TRUST","E56000032","Greater Manchester","E54000057","Greater Manchester","E40000010","North West",53.42977,-2.23012,"United Kingdom"],
        ["RC9","Bedfordshire","BEDFORDSHIRE HOSPITALS NHS FOUNDATION TRUST","E56000035","East of England","E54000024","Bedfordshire Luton and Milton Keynes","E40000007","East of England",51.89415,-0.4744,"United Kingdom"],
        ["RCB","York and Scarborough","YORK AND SCARBOROUGH TEACHING HOSPITALS NHS FOUNDATION TRUST","E56000026","Humber and North Yorkshire","E54000051","Humber and North Yorkshire","E40000012","North East and Yorkshire",53.96895,-1.08429,"United Kingdom"],
        ["RCD","Harrogate and District","HARROGATE AND DISTRICT NHS FOUNDATION TRUST","E56000030","West Yorkshire and Harrogate","E54000051","Humber and North Yorkshire","E40000012","North East and Yorkshire",53.99381,-1.51757,"United Kingdom"],
        ["RCF","Airedale","AIREDALE NHS FOUNDATION TRUST","E56000030","West Yorkshire and Harrogate","E54000054","West Yorkshire","E40000012","North East and Yorkshire",53.89801,-1.9627,"United Kingdom"],
        ["RCU","Sheffield Children's","SHEFFIELD CHILDREN'S NHS FOUNDATION TRUST","E56000025","South Yorkshire and Bassetlaw","E54000061","South Yorkshire","E40000012","North East and Yorkshire",53.3806,-1.49063,"United Kingdom"],
        ["RCX","Queen Elizabeth (King's Lynn)","THE QUEEN ELIZABETH HOSPITAL, KING'S LYNN, NHS FOUNDATION TRUST","E56000035","East of England","E54000022","Norfolk and Waveney","E40000007","East of England",52.75663,0.446694,"United Kingdom"],
        ["RD1","Royal United Bath","ROYAL UNITED HOSPITALS BATH NHS FOUNDATION TRUST","E56000033","Somerset, Wiltshire, Avon and Gloucestershire","E54000040","Bath and North East Somerset, Swindon And Wiltshire","E40000006","South West",51.39167,-2.39122,"United Kingdom"],
        ["RD8","Milton Keynes University","MILTON KEYNES UNIVERSITY HOSPITAL NHS FOUNDATION TRUST","E56000035","East of England","E54000024","Bedfordshire Luton and Milton Keynes","E40000007","East of England",52.02638,-0.73576,"United Kingdom"],
        ["RDE","East Suffolk and North Essex","EAST SUFFOLK AND NORTH ESSEX NHS FOUNDATION TRUST","E56000035","East of England","E54000023","Suffolk and North East Essex","E40000007","East of England",51.91016,0.899182,"United Kingdom"],
        ["RDU","Frimley","FRIMLEY HEALTH NHS FOUNDATION TRUST","E56000034","Thames Valley","E54000034","Frimley","E40000005","South East",51.31967,-0.74203,"United Kingdom"],
        ["REF","Royal Cornwall","ROYAL CORNWALL HOSPITALS NHS TRUST","E56000014","Peninsula","E54000036","Cornwall and The Isles of Scilly","E40000006","South West",50.26669,-5.09146,"United Kingdom"],
        ["REM","Liverpool University","LIVERPOOL UNIVERSITY HOSPITALS NHS FOUNDATION TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.40951,-2.96481,"United Kingdom"],
        ["REN","Clatterbridge","THE CLATTERBRIDGE CANCER CENTRE NHS FOUNDATION TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.33289,-3.02414,"United Kingdom"],
        ["REP","Liverpool Women's","LIVERPOOL WOMEN'S NHS FOUNDATION TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.39846,-2.96008,"United Kingdom"],
        ["RF4","Barking, Havering and Redbridge University","BARKING, HAVERING AND REDBRIDGE UNIVERSITY HOSPITALS NHS TRUST","E56000028","North East London","E54000029","North East London","E40000003","London",51.56865,0.179031,"United Kingdom"],
        ["RFF","Barnsley","BARNSLEY HOSPITAL NHS FOUNDATION TRUST","E56000025","South Yorkshire and Bassetlaw","E54000061","South Yorkshire","E40000012","North East and Yorkshire",53.55913,-1.49949,"United Kingdom"],
        ["RFR","Rotherham","THE ROTHERHAM NHS FOUNDATION TRUST","E56000025","South Yorkshire and Bassetlaw","E54000061","South Yorkshire","E40000012","North East and Yorkshire",53.41397,-1.34288,"United Kingdom"],
        ["RFS","Chesterfield Royal","CHESTERFIELD ROYAL HOSPITAL NHS FOUNDATION TRUST","E56000031","East Midlands","E54000058","Derby and Derbyshire","E40000011","Midlands",53.23621,-1.40005,"United Kingdom"],
        ["RGM","Royal Papworth","ROYAL PAPWORTH HOSPITAL NHS FOUNDATION TRUST","E56000035","East of England","E54000056","Cambridgeshire and Peterborough","E40000007","East of England",52.17352,0.136046,"United Kingdom"],
        ["RGN","North West Anglia","NORTH WEST ANGLIA NHS FOUNDATION TRUST","E56000035","East of England","E54000056","Cambridgeshire and Peterborough","E40000007","East of England",52.58392,-0.27939,"United Kingdom"],
		["RGP","James Paget University","JAMES PAGET UNIVERSITY HOSPITALS NHS FOUNDATION TRUST","E56000035","East of England","E54000022","Norfolk and Waveney","E40000007","East of England",52.56167,1.71798,"United Kingdom"],
		["RGR","West Suffolk","WEST SUFFOLK NHS FOUNDATION TRUST","E56000035","East of England","E54000023","Suffolk and North East Essex","E40000007","East of England",52.23166,0.709176,"United Kingdom"],
		["RGR","West Suffolk","WEST SUFFOLK NHS FOUNDATION TRUST","E56000035","East of England","E54000023","Suffolk and North East Essex","E40000007","East of England",52.23166,0.709176,"United Kingdom"],
		["RGT","Cambridge University","CAMBRIDGE UNIVERSITY HOSPITALS NHS FOUNDATION TRUST","E56000035","East of England","E54000056","Cambridgeshire and Peterborough","E40000007","East of England",52.17374,0.139114,"United Kingdom"],
		["RH5","Somerset","SOMERSET NHS FOUNDATION TRUST","E56000033","Somerset, Wiltshire, Avon and Gloucestershire","E54000038","Somerset","E40000006","South West",51.01157,-3.1217,"United Kingdom"],
		["RH8","Royal Devon University","ROYAL DEVON UNIVERSITY HEALTHCARE NHS FOUNDATION TRUST","E56000014","Peninsula","E54000037","Devon","E40000006","South West",50.7167,-3.50668,"United Kingdom"],
		["RHM","University Southampton","UNIVERSITY HOSPITAL SOUTHAMPTON NHS FOUNDATION TRUST","E56000016","Wessex","E54000042","Hampshire and Isle of Wight","E40000005","South East",50.93302,-1.4351,"United Kingdom"],
		["RHQ","Sheffield","SHEFFIELD TEACHING HOSPITALS NHS FOUNDATION TRUST","E56000025","South Yorkshire and Bassetlaw","E54000061","South Yorkshire","E40000012","North East and Yorkshire",53.40982,-1.45597,"United Kingdom"],
		["RHU","Portsmouth University","PORTSMOUTH HOSPITALS UNIVERSITY NATIONAL HEALTH SERVICE TRUST","E56000016","Wessex","E54000042","Hampshire and Isle of Wight","E40000005","South East",50.8503,-1.06993,"United Kingdom"],
		["RHW","Royal Berkshire","ROYAL BERKSHIRE NHS FOUNDATION TRUST","E56000034","Thames Valley","E54000044","Buckinghamshire, Oxfordshire and Berkshire West","E40000005","South East",51.45102,-0.95933,"United Kingdom"],
		["RJ1","Guy's and St Thomas'","GUY'S AND ST THOMAS' NHS FOUNDATION TRUST","E56000010","South East London","E54000030","South East London","E40000003","London",51.49796,-0.11891,"United Kingdom"],
		["RJ2","Lewisham and Greenwich","LEWISHAM AND GREENWICH NHS TRUST","E56000010","South East London","E54000030","South East London","E40000003","London",51.45302,-0.01792,"United Kingdom"],
		["RJ6","Croydon Health Services","CROYDON HEALTH SERVICES NHS TRUST","E56000021","RM Partners West London","E54000031","South West London","E40000003","London",51.38913,-0.10876,"United Kingdom"],
		["RJ7","St George's University","ST GEORGE'S UNIVERSITY HOSPITALS NHS FOUNDATION TRUST","E56000021","RM Partners West London","E54000031","South West London","E40000003","London",51.42668,-0.17569,"United Kingdom"],
		["RJC","South Warwickshire University","SOUTH WARWICKSHIRE UNIVERSITY NHS FOUNDATION TRUST","E56000007","West Midlands","E54000018","Coventry and Warwickshire","E40000011","Midlands",52.28997,-1.5832,"United Kingdom"],
		["RJE","University of North Midlands","UNIVERSITY HOSPITALS OF NORTH MIDLANDS NHS TRUST","E56000007","West Midlands","E54000010","Staffordshire and Stoke-On-Trent","E40000011","Midlands",53.00326,-2.2118,"United Kingdom"],
		["RJL","Northern Lincolnshire and Goole","NORTHERN LINCOLNSHIRE AND GOOLE NHS FOUNDATION TRUST","E56000026","Humber and North Yorkshire","E54000051","Humber and North Yorkshire","E40000012","North East and Yorkshire",53.54488,-0.09623,"United Kingdom"],
		["RJN","East Cheshire","EAST CHESHIRE NHS TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.26232,-2.14107,"United Kingdom"],
		["RJR","Countess of Chester","COUNTESS OF CHESTER HOSPITAL NHS FOUNDATION TRUST","E56000005","Cheshire and Merseyside","E54000008","Cheshire and Merseyside","E40000010","North West",53.2088,-2.89788,"United Kingdom"],
		["RJZ","King's College","KING'S COLLEGE HOSPITAL NHS FOUNDATION TRUST","E56000010","South East London","E54000030","South East London","E40000003","London",51.46808,-0.09392,"United Kingdom"],
		["RK5","Sherwood Forest","SHERWOOD FOREST HOSPITALS NHS FOUNDATION TRUST","E56000031","East Midlands","E54000060","Nottingham and Nottinghamshire","E40000011","Midlands",53.13457,-1.23358,"United Kingdom"],
		["RK9","University Plymouth","UNIVERSITY HOSPITALS PLYMOUTH NHS TRUST","E56000014","Peninsula","E54000037","Devon","E40000006","South West",50.41672,-4.11368,"United Kingdom"],
		["RKB","University Coventry and Warwickshire","UNIVERSITY HOSPITALS COVENTRY AND WARWICKSHIRE NHS TRUST","E56000007","West Midlands","E54000018","Coventry and Warwickshire","E40000011","Midlands",52.42121,-1.4384,"United Kingdom"],
		["RKE","Whittington","WHITTINGTON HEALTH NHS TRUST","E56000027","North Central London","E54000028","North Central London","E40000003","London",51.56648,-0.13907,"United Kingdom"]]

df = pd.DataFrame(data_rows, columns=columns)

def classify_trust(name):
name_upper = str(name).upper()
if "CHILDREN" in name_upper: return "Pediatrics & Children's"
elif "CANCER" in name_upper or "CHRISTIE" in name_upper: return "Oncology"
elif "ORTHOPAEDIC" in name_upper: return "Orthopedics"
elif "DERMATOLOGY" in name_upper: return "Dermatology"
elif "WOMEN" in name_upper: return "Women's Health"
else: return "General Acute Care"

df["Specialism_Group"] = df["TRUST_NM_LONG"].apply(classify_trust)

np.random.seed(42)
df["Est_Regional_Population_M"] = np.round(np.random.uniform(0.8, 2.5, len(df)), 2)
df["Deprivation_Index_Score"] = np.round(np.random.uniform(15.0, 45.0, len(df)), 1)
df["Baseline_Annual_Admissions_K"] = np.round(df["Est_Regional_Population_M"] * 120 + 
df["Deprivation_Index_Score"] * 1.5, 1)
return df

#3. Check Data Load State Nativelytry:
df = load_data()
except Exception as e:
st.error(f"Data loading failed: {e}")
st.stop()

#4. Sidebar Controls Strategy
st.sidebar.header("🎛️ Filter Workspace")
regions = sorted(df["NHSER_NM"].unique().tolist())
selected_regions = st.sidebar.multiselect("Filter by NHS Region:", options=regions, 
default=regions)

if not selected_regions:
    filtered_df = df.copy()
else:
    filtered_df = df[df["NHSER_NM"].isin(selected_regions)]

# 5. Display Analytical KPI Metrics
st.subheader("📊 Operational Baseline Matrix")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Selected Health Providers", len(filtered_df))
k2.metric("Est. Population Covered", f"{filtered_df['Est_Regional_Population_M'].sum():.1f}M")
k3.metric("Avg Deprivation Index", f"{filtered_df['Deprivation_Index_Score'].mean():.1f}")
k4.metric("Total Annual Admissions Base", f"{filtered_df['Baseline_Annual_Admissions_K'].sum():.1f}K")


st.markdown("---")

#6. Modernized Non-Crash Map Component
st.subheader("🌐 Regional Densities & Facility Mapping")
if not filtered_df.empty:
fig_map = px.scatter_map(
    filtered_df,
    lat="LAT",
    lon="LONG",
    hover_name="TRUST_NM",
    hover_data=["TRUST_CD", "Specialism_Group"],
    color="NHSER_NM",
    zoom=5,
    height=500
    )
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig_map, use_container_width=True)
else:
st.warning("No coordinates to plot.")

st.markdown("---")

#7. Predictive Algorithm Framework
st.subheader("🔮 Predictive Forecasting Dashboard Panel")
growth_rate = st.slider("Select Projected Annual Population Growth Rate (%):", 
                        min_value=0.0, max_value=10.0, value=2.5, step=0.5)

if not filtered_df.empty:
    x_base = filtered_df["Est_Regional_Population_M"].values
    y_base = filtered_df["Baseline_Annual_Admissions_K"].values
    n = len(x_base)

if n > 1:
    m = (n * np.sum(x_base * y_base) - np.sum(x_base) * np.sum(y_base)) / (n * 
    np.sum(x_base**2) - (np.sum(x_base))**2)
    c = (np.sum(y_base) - m * np.sum(x_base)) / n
else:
    m, c = 120.0, 30.0

x_forecasted = x_base * (1 + (growth_rate / 100.0))
y_forecasted = m * x_forecasted + c

forecast_df = pd.DataFrame({
    "Trust Code": filtered_df["TRUST_CD"],
    "Current Capacity (K)": y_base,
    "Projected Demand (K)": np.round(y_forecasted, 1)
    })

fig_forecast = px.scatter(
    forecast_df, x="Current Capacity (K)", y="Projected Demand (K)", text="Trust Code",
    title="Mathematical Shift Projection Grid",
    labels={"Current Capacity (K)": "Current Capacity", "Projected Demand (K)": "Forecasted Clinical Demand"}
)

cf1, cf2 = st.columns(2)
with cf1:
    st.plotly_chart(fig_forecast, use_container_width=True)
    with cf2:
        st.markdown("#### Top 5 Highest Risk Growth Vectors")
        st.dataframe(forecast_df.sort_values(by="Projected Demand (K)", 
        ascending=False).head(5), use_container_width=True, hide_index=True)
