FROM python:3.7

cmd mkdir /final

copy . /final

WORKDIR /final

EXPOSE 8501


RUN pip3 install -r requirements.txt



CMD streamlit run final.py



