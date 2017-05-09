#!/bin/bash

echo "I will now activate or create a virtualenv named \"myproject\"."
echo "This requires virtualenvwrapper to be installed, so if you don't have"
echo "it, press CTRL-C and install virtualenvwrapper first"
read -n 1 -p "Press a key to continue"
FAIL=0
source `dpkg -L virtualenvwrapper|grep virtualenvwrapper.sh`
workon myproject || mkvirtualenv --no-site-packages myproject || export FAIL=1
if [ $FAIL -eq 1 ] ; then
    echo "Please install virtualenvwrapper first."
    echo "Note: I'm assuming a .deb based distro. If you get errors about dpkg,"
    echo "edit this script and change the \"source\" line to source your"
    echo "virtualenvwrapper's bash script."
    exit 1
fi
echo -ne '\n'
echo "Also setting PYTHONPATH to $PWD"
export PYTHONPATH=$PWD
echo -ne '\n\n'

echo "Installing Pylint, if necessary"
read -n 1 -p "Press a key to continue"
pip install pylint
echo -ne '\n\n'

echo "Running the code to demonstrate it works perfectly fine as far as Python's concerned."
read -n 1 -p "Press a key to continue"
echo -ne "    "
./myproject/apps/myapp/commands/mycommand.py
echo -ne '\n'

echo "If the import is valid, this should've produced the output \"Hello\"."
echo "For the record, the import line was:"
echo -ne "    "
grep import myproject/apps/myapp/commands/mycommand.py
echo -ne '\n'

echo "Finally, let's see what Pylint makes of this..."
read -n 1 -p "Press a key to continue"
pylint myproject/apps/myapp/commands/mycommand.py
echo -ne '\n\n'

echo "That wasn't too good... The import that clearly works for Python, is"
echo "misinterpreted by pylint. The reason is there's a __init__.py in this"
echo "folder. Pylint thinks the \"myproject\" in the import line refers to"
echo "${PWD}, rather than ${PWD}/myproject"
echo -ne "\n"
echo "Let's see what the result is after we remove __init__.py"
read -n 1 -p "Press a key to continue"

rm __init__.py
pylint myproject/apps/myapp/commands/mycommand.py
touch __init__.py
echo "Without the top-level __init__.py, things work out fine. It also works ifi the"
echo "import line is changed to \"from myproject.myproject.classes import MyClass\"."
echo "But of course, that would not work in Python."


echo -ne "\n\n"
read -p "Would you like me to remove the \"myproject\" virtualenv now? (y/N) " remove_venv
case "$remove_venv" in
    y|Y ) deactivate && rmvirtualenv myproject;;
    * ) echo "OK, leaving intact";;
esac
