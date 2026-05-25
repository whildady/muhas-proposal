#%%
%%writefile app.py
import os
import yaml
import streamlit as st

# 1. Lazimisha mradi ukae kwenye folda lako la JIMMY
folder_path = r"C:\Users\user\Desktop\JIMMY"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
os.chdir(folder_path)

# Maandishi kamili ya YAML yaliyoboreshwa kwa taarifa zako binafsi
yaml_content = """# ======================================================================================
# TECHNICAL FIELD PLACEMENT PROPOSAL - DATA SCIENCE & ANALYTICS DEPLOYMENT
# Applicant: JIMSON JOHN KITINUSA
# Institution: EASTERN AFRICA STATISTICAL TRAINING CENTRE (EASTC)
# ======================================================================================
---
muhas_placement_blueprint:
  metadata:
    applicant_name: "JIMSON JOHN KITINUSA"
    academic_institution: "EASTERN AFRICA STATISTICAL TRAINING CENTRE (EASTC)"
    course_of_study: "Bachelor of  Data Science"
    academic_year: "Second Year (Year 2)"
    target_institution: "Muhimbili University of Health and Allied Sciences (MUHAS)"
    deployment_scope: "Institutional Research, Academic Informatics, & Administrative Automation"
    contact_phone: "0753207386"
    contact_email: "jimsonjohn014@gmail.com"

  core_value_propositions:
    biostatistics_and_clinical_analytics:
      objective: "Transform raw healthcare, demographic, and clinical trial datasets into publication-ready medical insights."
      capabilities:
        - "Advanced data sanitization, structural missingness handling, and algorithmic data imputation."
        - "Implementation of multivariate statistical models, survival analysis (Kaplan-Meier curves, Cox Proportional Hazards), and epidemiological trend stratification."
        - "Refactoring code bases, variables, and analytical scripts into standard English documentation to align seamlessly with international journal publication standards."
      tooling: ["Python (Pandas, NumPy, SciPy)", "R-Programming (Tidyverse)", "Statsmodels"]

    automated_big_data_pipelines:
      objective: "Develop scalable scripts to ingest, normalize, and parse large-scale institutional, regional, and national datasets."
      capabilities:
        - "Engineering automated ETL (Extract, Transform, Load) pipelines to seamlessly handle massive demographic registries, student center codes, and multi-facility public health data."
        - "Eliminating manual file entry bottlenecks by writing scalable regular expression (Regex) parsers capable of consuming unstructured multi-format spreadsheets."
        - "Structuring legacy, chaotic multi-indexed Excel matrices into optimized, clean relational database paradigms."
      tooling: ["Python Core (OS, Sys, Re)", "Power Query Architecture", "OpenPyXL / XlsxWriter"]

    interactive_data_visualization_and_bi:
      objective: "Bridge the gap between raw unstructured data and executive academic decision-making via responsive business intelligence dashboards."
      capabilities:
        - "Designing reactive, low-latency analytical dashboards for real-time tracking of research grant progress, multi-department budget consumption, or student performance indices."
        - "Building custom-tailored programmatic web applications to host institutional key performance indicators (KPIs) for department heads."
      tooling: ["Streamlit Framework", "Plotly / Dash", "Advanced Excel (Power Pivot)", "Tableau"]

    legacy_modernization_and_office_automation:
      objective: "Refactor slow, manual, error-prone desktop workflows into robust programmatic execution scripts."
      capabilities:
        - "Automating multi-sheet complex report generation across university registries using Python-to-Excel abstraction layers."
        - "Writing script routines to batch-process, cross-verify, and audit hundreds of independent local student or medical center data files simultaneously, completely eliminating human typographical errors."
      tooling: ["VBA / Macros", "Python Subprocess & File Interfacing", "Excel Object Models"]

    predictive_modeling_and_machine_learning:
      objective: "Deploy statistical learning algorithms to support predictive public health and institutional forecasting."
      capabilities:
        - "Training machine learning algorithms to map disease outbreak velocities, epidemiological micro-trends, or patient re-admission risks based on historical healthcare vectors."
        - "Developing predictive analytics for academic management to optimize enrollment targets, forecast student attrition rates, and balance resource distribution."
      tooling: ["Scikit-Learn", "XGBoost", "Supervised / Unsupervised Learning Topologies"]

  institutional_dividends:
    temporal_efficiency: "Drastic reduction of data compilation and auditing windows from standard multi-day manual periods down to instantaneous, single-click programmatic executions."
    scientific_rigor: "Enhancement of institutional research validation through reproducible code notebooks (Jupyter/RMarkdown), leaving a clean audit trail for international funding bodies."
    data_integrity: "Enforcement of hard-coded programmatic validation constraints, ensuring zero tolerance for manual entry corruptions or malformed indices."
..."""

# Hifadhi upya faili la YAML
with open("muhas_proposal.yml", "w", encoding="utf-8") as f:
    f.write(yaml_content)

# Na sasa tunaunda muonekano wa Streamlit Dashboard
st.set_page_config(page_title="MUHAS-Analytics-Proposal", layout="wide")

# CSS ya rangi za kitaalamu (Academic & Institutional Theme)
st.markdown("""
    <style>
    .main-title { color: #0f2c59; font-weight: bold; font-size: 28px; margin-top: 15px; margin-bottom: 5px; text-transform: uppercase; }
    .sub-title { color: #4a5568; font-size: 16px; font-style: italic; margin-bottom: 25px; }
    .student-card { background-color: #f8fafc; border-left: 6px solid #0f2c59; padding: 20px; border-radius: 4px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .student-card table { width: 100%; border-collapse: collapse; }
    .student-card td { padding: 6px 10px; font-size: 15px; vertical-align: top; }
    .student-label { font-weight: bold; color: #0f2c59; width: 20%; text-transform: uppercase; font-size: 13px; letter-spacing: 0.5px; }
    .contact-footer { background-color: #0f2c59; color: white; padding: 25px; border-radius: 6px; text-align: center; margin-top: 50px; font-size: 15px; }
    </style>
""", unsafe_allow_html=True)

data = yaml.safe_load(yaml_content)["muhas_placement_blueprint"]

# 1. TAARIFA ZAKO BINAFSI (Zinaanza Juu Kushoto kwa mpangilio sahihi)
st.markdown('<div class="student-card">', unsafe_allow_html=True)
col_meta_1, col_meta_2 = st.columns([3, 2])

with col_meta_1:
    st.markdown(f"""
    <table>
        <tr><td class="student-label">Applicant Name:</td><td><strong>{data['metadata']['applicant_name']}</strong></td></tr>
        <tr><td class="student-label">Institution:</td><td><strong>{data['metadata']['academic_institution']}</strong></td></tr>
        <tr><td class="student-label">Course:</td><td>{data['metadata']['course_of_study']}</td></tr>
        <tr><td class="student-label">Academic Year:</td><td>{data['metadata']['academic_year']}</td></tr>
    </table>
    """, unsafe_allow_html=True)

with col_meta_2:
    st.markdown(f"""
    <table>
        <tr><td class="student-label">Target Placement:</td><td>{data['metadata']['target_institution']}</td></tr>
        <tr><td class="student-label">Deployment Scope:</td><td>{data['metadata']['deployment_scope']}</td></tr>
    </table>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Kichwa cha Habari Kuu
st.markdown('<div class="main-title">FIELD PLACEMENT & TECHNICAL VALUE PROPOSAL</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Leveraging Data Science Frameworks, Biostatistics, and Automation Pipelines for Medical Research & Institutional Efficiency</div>', unsafe_allow_html=True)

st.markdown("---")

# 2. SEHEMU YA MAENEO YA MCHANGO (Core Deliverables)
st.subheader("🎯 Core Value Propositions & Technical Capabilities")
props = data["core_value_propositions"]

for key, val in props.items():
    title = key.replace("_", " ").title()
    with st.expander(f"🔮 {title}"):
        st.write(f"**Objective:** {val['objective']}")
        st.write("**Specific Capabilities to be Deployed:**")
        for capability in val["capabilities"]:
            st.write(f"- {capability}")
        st.write("**Technologies Stack:**")
        st.code(", ".join(val["tooling"]))

st.markdown("---")

# 3. FAIDA KWA CHUO (Institutional Dividends)
st.subheader("📈 Institutional ROI (What MUHAS Stands to Gain)")
divs = data["institutional_dividends"]
c1, c2, c3 = st.columns(3)
with c1:
    st.info(f"⏱️ **Temporal Efficiency**\\n\\n{divs['temporal_efficiency']}")
with c2:
    st.success(f"🔬 **Scientific Rigor**\\n\\n{divs['scientific_rigor']}")
with c3:
    st.warning(f"🛡️ **Data Integrity**\\n\\n{divs['data_integrity']}")

# 4. MAWASILIANO CHINI (Professional Footer)
st.markdown(f"""
    <div class="contact-footer">
        <strong style="letter-spacing:1px; font-size:16px;">CONTACT INFORMATION</strong><br><br>
        📞 Phone: <strong>{data['metadata']['contact_phone']}</strong> | ✉️ Email: <strong>{data['metadata']['contact_email']}</strong><br><br>
        <span style="font-size:12px; color:#cbd5e0; font-style:italic;">Designed with Professional Academic Deep Navy Colors & YAML Config Frameworks for MUHAS Placement Evaluation</span>
    </div>
""", unsafe_allow_html=True)
# %%
