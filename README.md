# CSV Merger
 Simple tool to merge CSV files.

## Example Usage

```bash
csv_merger -h
usage: csv_merger.py [-h] -i INPUT [-o OUTPUT]

Merge CSV files together.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input files to merge.
  -o OUTPUT, --output OUTPUT
                        Output file path.
```

## Build
To build a local python package (tested on Mac OS 10.2).

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
# Virtual env bundled with MacOS is faulty.
pip install --upgrade virtualenv
pip install --upgrade build
python3 -m build
# This will output a Tar file in dist/csv-merger-*.tar.gz
deactivate
```

To wrap the local python package in into a Docker image run
```bash
docker build --tag csv-merger .
```

To push to docker hub
```bash
# List runing docker image to get the Image ID
docker images

docker tag $IMAGE_ID $DOCKERHUB_USERNAME/csv-merger:latest

docker login --username=$DOCKERHUB_USERNAME

docker push $DOCKERHUB_USERNAME/csv-merger
```

## Install
Install from a local tar file.

```bash
# Optionally install in local virtual env.
source venv/bin/activate
pip install dist/csv-merger-*.tar.gz
# Reload the virtual environment to make the tool available.
deactivate; source venv/bin/activate
```