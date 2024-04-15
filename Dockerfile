FROM python:3.8-slim
RUN apt-get update && \
    apt-get install -y git sqlite3 && \
    apt-get clean
RUN git clone https://github.com/Symbolexe/VulnersX VulnersX

# COPY VulnersX.py .

RUN pip install requests
RUN chmod +x VulnersX/VulnersX.py
EXPOSE 80
ENTRYPOINT ["python", "VulnersX/VulnersX.py"]
CMD []
