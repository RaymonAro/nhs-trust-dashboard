import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from io import StringIO

# Set up page configurations
st.set_page_config(page_title="NHS Trust Advanced Analytics & Forecasting", layout="wide")
st.title("🏥 NHS Trust Advanced Analytics & Predictive Hub")

# 1. Load Data
@st.cache_data
def load_data():
    raw_data = """TRUST_CD,TRUST_NM,TRUST_NM_LONG,CAL_CD,CAL_NM,ICB_CD,ICB_NM,NHSER_CD,NHSER_NM,LAT,LONG,country
NYG,Sussex Dermatology Service,SUSSEX DERMATOLOGY SERVICE,E56000011,Kent and Medway,E54000032,Kent and Medway,E40000005,South East,50.81932,-0.36458,United Kingdom
R0A,Manchester University,MANCHESTER UNIVERSITY NHS FOUNDATION TRUST,E56000032,Greater Manchester,E54000057,Greater Manchester,E40000010,North West,53.46244,-2.22771,United Kingdom
R0B,South Tyneside and Sunderland,SOUTH TYNESIDE AND SUNDERLAND NHS FOUNDATION TRUST,E56000029,Northern,E54000050,North East and North Cumbria,E40000012,North East and Yorkshire,54.90221,-1.41033,United Kingdom
R0D,University Dorset,UNIVERSITY HOSPITALS DORSET NHS FOUNDATION TRUST,E56000016,Wessex,E54000041,Dorset,E40000006,South West,50.72199,-1.97312,United Kingdom
R1F,Isle of Wight,ISLE OF WIGHT NHS TRUST,E56000016,Wessex,E54000042,Hampshire and Isle of Wight,E40000005,South East,50.71084,-1.30133,United Kingdom
R1H,Barts,BARTS HEALTH NHS TRUST,E56000028,North East London,E54000029,North East London,E40000003,London,51.51717,-0.05605,United Kingdom
R1K,London North West University,LONDON NORTH WEST UNIVERSITY HEALTHCARE NHS TRUST,E56000021,RM Partners West London,E54000027,North West London,E40000003,London,51.57541,-0.32204,United Kingdom
RA2,Royal Surrey County,ROYAL SURREY COUNTY HOSPITAL NHS FOUNDATION TRUST,E56000012,Surrey and Sussex,E54000063,Surrey Heartlands,E40000005,South East,51.24102,-0.60746,United Kingdom
RA7,Bristol Trusts (Combined),BRISTOL TRUSTS (COMBINED SUBMISSION),E56000033,"Somerset, Wiltshire, Avon and Gloucestershire",E54000039,"Bristol, North Somerset and South Gloucestershire",E40000006,South West,51.45948,-2.59302,United Kingdom
RA9,Torbay and South Devon,TORBAY AND SOUTH DEVON NHS FOUNDATION TRUST,E56000014,Peninsula,E54000037,Devon,E40000006,South West,50.48232,-3.5538,United Kingdom
RAE,Bradford,BRADFORD TEACHING HOSPITALS NHS FOUNDATION TRUST,E56000030,West Yorkshire and Harrogate,E54000054,West Yorkshire,E40000012,North East and Yorkshire,53.80598,-1.7947,United Kingdom
RAJ,Mid and South Essex,MID AND SOUTH ESSEX NHS FOUNDATION TRUST,E56000035,East of England,E54000026,Mid and South Essex,E40000007,East of England,51.55384,0.688617,United Kingdom
RAL,Royal Free London,ROYAL FREE LONDON NHS FOUNDATION TRUST,E56000027,North Central London,E54000028,North Central London,E40000003,London,51.55322,-0.16532,United Kingdom
RAN,Royal National Orthopaedic,ROYAL NATIONAL ORTHOPAEDIC HOSPITAL NHS TRUST,E56000027,North Central London,E54000028,North Central London,E40000003,London,51.63256,-0.31044,United Kingdom
RAS,Hillingdon,THE HILLINGDON HOSPITALS NHS FOUNDATION TRUST,E56000021,RM Partners West London,E54000027,North West London,E40000003,London,51.52608,-0.46117,United Kingdom
RAX,Kingston,KINGSTON HOSPITAL NHS FOUNDATION TRUST,E56000021,RM Partners West London,E54000031,South West London,E40000003,London,51.41483,-0.2826,United Kingdom
RBD,Dorset County,DORSET COUNTY HOSPITAL NHS FOUNDATION TRUST,E56000016,Wessex,E54000041,Dorset,E40000006,South West,50.71294,-2.44694,United Kingdom
RBK,Walsall,WALSALL HEALTHCARE NHS TRUST,E56000007,West Midlands,E54000062,Black Country,E40000011,Midlands,52.58233,-1.99892,United Kingdom
RBL,Wirral University,WIRRAL UNIVERSITY TEACHING HOSPITAL NHS FOUNDATION TRUST,E56000005,Cheshire and Merseyside,E54000008,Cheshire and Merseyside,E40000010,North West,53.36964,-3.09682,United Kingdom
RBN,Mersey and West Lancashire,MERSEY AND WEST LANCASHIRE TEACHING HOSPITALS NHS TRUST,E56000005,Cheshire and Merseyside,E54000008,Cheshire and Merseyside,E40000010,North West,53.42047,-2.78495,United Kingdom
RBS,Alder Hey Children's,ALDER HEY CHILDREN'S NHS FOUNDATION TRUST,E56000005,Cheshire and Merseyside,E54000008,Cheshire and Merseyside,E40000010,North West,53.42024,-2.89872,United Kingdom
RBT,Mid Cheshire,MID CHESHIRE HOSPITALS NHS FOUNDATION TRUST,E56000005,Cheshire and Merseyside,E54000008,Cheshire and Merseyside,E40000010,North West,53.11768,-2.47586,United Kingdom
RBV,Christie,THE CHRISTIE NHS FOUNDATION TRUST,E56000032,Greater Manchester,E54000057,Greater Manchester,E40000010,North West,53.42977,-2.23012,United Kingdom
RC9,Bedfordshire,BEDFORDSHIRE HOSPITALS NHS FOUNDATION TRUST,E56000035,East of England,E54000024,"Bedfordshire, Luton and Milton Keynes",E40000007,East of England,51.89415,-0.4744,United Kingdom
RCB,York and Scarborough,YORK AND SCARBOROUGH TEACHING HOSPITALS NHS FOUNDATION TRUST,E56000026,Humber and North Yorkshire,E54000051,Humber and North Yorkshire,E40000012,North East and Yorkshire,53.96895,-1.08429,United Kingdom
RCD,Harrogate and District,HARROGATE AND DISTRICT NHS FOUNDATION TRUST,E56000030,West Yorkshire and Harrogate,E54000051,Humber and North Yorkshire,E40000012,North East and Yorkshire,53.99381,-1.51757,United Kingdom
RCF,Airedale,AIREDALE NHS FOUNDATION TRUST,E56000030,West Yorkshire and Harrogate,E54000054,West Yorkshire,E40000012,North East and Yorkshire,53.89801,-1.9627,United Kingdom
RCU,Sheffield Children's,SHEFFIELD CHILDREN'S NHS FOUNDATION TRUST,E56000025,South Yorkshire and Bassetlaw,E54000061,South Yorkshire,E40000012,North East and Yorkshire,53.3806,-1.49063,United Kingdom
RCX,Queen Elizabeth (King's Lynn),THE QUEEN ELIZABETH HOSPITAL, KING'S LYNN, NHS FOUNDATION TRUST,E56000035,East of England,E54000022,Norfolk and Waveney,E40000007,East of England,52.75663,0.446694,United Kingdom
RD1,Royal United Bath,ROYAL UNITED HOSPITALS BATH NHS FOUNDATION TRUST,E56000033,"Somerset, Wiltshire, Avon and Gloucestershire",E54000040,"Bath and North East Somerset, Swindon And Wiltshire",E40000006,South West,51.39167,-2.39122,United Kingdom
RD8,Milton Keynes University,MILTON KEYNES UNIVERSITY HOSPITAL NHS FOUNDATION TRUST,E56000035,East of England,E54000024,"Bedfordshire, Luton and Milton Keynes",E40000007,East of England,52.02638,-0.73576,United Kingdom
RDE,East Suffolk and North Essex,EAST SUFFOLK AND NORTH ESSEX NHS FOUNDATION TRUST,E56000035,East of England,E54000023,Suffolk and North East Essex,E40000007,East of England,51.91016,0.899182,United Kingdom
RDU,Frimley,FRIMLEY HEALTH NHS FOUNDATION TRUST,E56000034,Thames Valley,E54000034,Frimley,E40000005,South East,51.31967,-0.74203,United Kingdom
REF,Royal Cornwall,ROYAL CORNWALL HOSPITALS NHS TRUST,E56000014,Peninsula,E54000036,Cornwall and The Isles of Scilly,E40000006,South West,50.26669,-5.09146,United Kingdom
REM,Liverpool University,LIVERPOOL UNIVERSITY HOSPITALS NHS FOUNDATION TRUST,E56000005,Cheshire and Merseyside,E54000008,Cheshire and Merseyside,E40000010,North West,53.40951,-2.96481,United Kingdom
REN,Clatterbridge,THE CLATTERBRIDGE CANCER CENTRE NHS FOUNDATION TRUST,E56000005,Cheshire and Merseyside,E54000008,Cheshire and Merseyside,E40000010,North West,53.33289,-3.02414,United Kingdom
REP,Liverpool Women's,LIVERPOOL WOMEN'S NHS FOUNDATION TRUST,E56000005,Cheshire and Merseyside,E54000008,Cheshire and Merseyside,E40000010,North West,53.39846,-2.96008,United Kingdom
RF4,"Barking, Havering and Redbridge University",BARKING, HAVERING AND REDBRIDGE UNIVERSITY HOSPITALS NHS TRUST,E56000028,North East London,E54000029,North East London,E40000003,London,51.56865,0.179031,United Kingdom
RFF,Barnsley,BARNSLEY HOSPITAL NHS FOUNDATION TRUST,E56000025,South Yorkshire and Bassetlaw,E54000061,South Yorkshire,E40000012,North East and Yorkshire,53.55913,-1.49949,United Kingdom
RFR,Rotherham,THE ROTHERHAM NHS FOUNDATION TRUST,E56000025,South Yorkshire and Bassetlaw,E54000061,South Yorkshire,E40000012,North East and Yorkshire,53.41397,-1.34288,United Kingdom
RFS,Chesterfield Royal,CHESTERFIELD ROYAL HOSPITAL NHS FOUNDATION TRUST,E56000031,East Midlands,E54000058,Derby and Derbyshire,E40000011,Midlands,53.23621,-1.40005,United Kingdom
RGM,Royal Papworth,ROYAL PAPWORTH HOSPITAL NHS FOUNDATION TRUST,E56000035,East of England,E54000056,Cambridgeshire and Peterborough,E40000007,East of England,52.17352,0.136046,United Kingdom
RGN,North West Anglia,NORTH WEST ANGLIA NHS FOUNDATION TRUST,E56000035,East of England,E54000056,Cambridgeshire and Peterborough,E40000007,East of England,52.58392,-0.27939,United Kingdom
RGP,James Paget University,JAMES PAGET UNIVERSITY HOSPITALS NHS FOUNDATION TRUST,E56000035,East of England,E54000022,Norfolk and Waveney,E40000007,East of England,52.56167,1.71798,United Kingdom
RGR,West Suffolk,WEST SUFFOLK NHS FOUNDATION TRUST,E56000035,East of England,E54000023,Suffolk and North East Essex,E40000007,East of England,52.23166,0.709176,United Kingdom
RGT,Cambridge University,CAMBRIDGE UNIVERSITY HOSPITALS NHS FOUNDATION TRUST,E56000035,East of England,E54000056,Cambridgeshire and Peterborough,E40000007,East of England,52.17374,0.139114,United Kingdom
RH5,Somerset,SOMERSET NHS FOUNDATION TRUST,E56000033,"Somerset, Wiltshire, Avon and Gloucestershire",E54000038,Somerset,E40000006,South West,51.01157,-3.1217,United Kingdom
RH8,Royal Devon University,ROYAL DEVON UNIVERSITY HEALTHCARE NHS FOUNDATION TRUST,E56000014,Peninsula,E54000037,Devon,E40000006,South West,50.7167,-3.50668,United Kingdom
RHM,University Southampton,UNIVERSITY HOSPITAL SOUTHAMPTON NHS FOUNDATION TRUST,E56000016,Wessex,E54000042,Hampshire and Isle of Wight,E40000005,South East,50.93302,-1.4351,United Kingdom
RHQ,Sheffield,SHEFFIELD TEACHING HOSPITALS NHS FOUNDATION TRUST,E56000025,South Yorkshire and Bassetlaw,E54000061,South Yorkshire,E40000012,North East and Yorkshire,53.40982,-1.45597,United Kingdom
