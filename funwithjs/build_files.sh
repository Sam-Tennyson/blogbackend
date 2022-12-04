echo "BUILD START"
python 3.9 -m pip install -r requirements.txt
python 3.9 manage.py collectstatic --no-input --clear
echo "BUILD END"