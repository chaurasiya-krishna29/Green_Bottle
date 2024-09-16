# echo "BUILD START"
# python3 -m pip install -r requirements.txt
# python3 manage.py collectstatic --noinput --clear
# echo "BUILD END"

echo "BUILD START"
apt-get update && apt-get install -y libsqlite3-dev  # Install SQLite dependency
python3 -m pip install -r requirements.txt  # Install Python dependencies
python3 manage.py collectstatic --noinput --clear  # Collect static files
echo "BUILD END"
