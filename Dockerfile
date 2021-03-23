FROM python:3.6
COPY dist/csv-merger-*.tar.gz ./csv-merger.tar.gz
WORKDIR ./
RUN pip install csv-merger.tar.gz
CMD bash