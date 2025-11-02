#!/bin/#!/bin/bash
# intră în folderul frontend
cd frontend

# instalează toate dependențele
pip install -r requirements.txt

# pornește aplicația Streamlit
streamlit run app.py --server.port $PORT --server.address 0.0.0.0