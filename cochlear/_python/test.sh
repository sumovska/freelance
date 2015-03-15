cd src

coverage run -m tests.runner
echo
echo 'Coverage Report:'
echo '================'
coverage report --omit '*site-packages*','cochlear*','generated*','*kivy*'
