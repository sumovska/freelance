echo on
pushd src
call "%1\kivy.bat" "tests/runner.py"
popd