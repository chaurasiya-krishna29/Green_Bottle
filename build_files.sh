echo "BUILD START"
python3.12.3 -m pip install -r requirements.txt
python3.12.3 manage.py collectstatic --noinput --clear
echo "BUILD END"