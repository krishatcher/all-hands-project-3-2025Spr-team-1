echo " - -- --- ---- START ---- --- -- -"
echo " ~~~ ~~~ ~~~ Test 1 ~~~ ~~~ ~~~"
poetry run comparison -q -v 1250
echo " ~~~ ~~~ ~~~ Test 2 ~~~ ~~~ ~~~"
poetry run comparison -q -v 2500
echo " ~~~ ~~~ ~~~ Test 3 ~~~ ~~~ ~~~"
poetry run comparison -q -v 5000
echo " ~~~ ~~~ ~~~ Test 4 ~~~ ~~~ ~~~"
poetry run comparison -q -v 10000
echo " ~~~ ~~~ ~~~ Test 5 ~~~ ~~~ ~~~"
poetry run comparison -q -v 20000
echo " - -- --- ---- END ---- --- -- -"