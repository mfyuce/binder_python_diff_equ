import webdav3.client as wc
from os import getenv, path
from dotenv import load_dotenv

_EXPORT_FILE = "./export.csv"
_IMPORT_FILE = "./import.csv"

load_dotenv()

options = {
    'webdav_hostname': getenv("WEB_DAV_HOSTNAME"),
    'webdav_login': getenv("WEB_DAV_LOGIN"),
    'webdav_password': getenv("WEB_DAV_PASSWORD"),
    'webdav_disable_check': True
}


def download_import_file():
    client = wc.Client(options)
    client.download_file(getenv("IMPORT_FILE"), _IMPORT_FILE)


def upload_export_file():
    if path.isfile(_EXPORT_FILE):
        client = wc.Client(options)
        client.upload_sync(remote_path=getenv("EXPORT_FILE"), local_path=_EXPORT_FILE)


if __name__ == '__main__':
    download_import_file()
