#!/usr/bin/bash

day_num=$1
echo "> Creating "${day_num}
DAY_FOLDER="day"${day_num}

echo "> Copying template"
cp -r a_day_template/ ${DAY_FOLDER}

echo ">> Moving files"
DAY_SOL=${DAY_FOLDER}"/solution_day_"${day_num}".py"
DAY_TEST=${DAY_FOLDER}"/test_day_"${day_num}".py"
mv ${DAY_FOLDER}"/solution_day_.py" ${DAY_SOL}
mv ${DAY_FOLDER}/test_day_.py ${DAY_TEST}

echo ">> Changing strings"
sed -i "s|CURRENT_DAY = None|CURRENT_DAY = ${day_num}|" ${DAY_SOL}
sed -i "s|xxx|day${day_num}|" ${DAY_TEST}
