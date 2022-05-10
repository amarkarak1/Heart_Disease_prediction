FROM python:3.7

WORKDIR /final

COPY requirements.txt ./requirements.txt

RUN pip install -r requiremts.txt

EXPOSE 8501

COPY ./final

ENTRYPOINT ["streamlit", "run"]

CMD ["final.py"]




