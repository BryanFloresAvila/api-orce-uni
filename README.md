# API ORCE UNI
A small API made in Flask, to get grades and information from a UNI student. This API was made thanks to web scrapping using the tabula-py and bs4 libraries.
# TEST SERVER
You can try to make requests at the following link: https://api-orce-uni.jeedx.repl.co
## EXAMPLES
Any of the requests returns the information in JSON form.
- To obtain information about a student with his or her code: https://api-orce-uni.jeedx.repl.co/getInformation/?code=CODIGO
- To obtain grades for a student with his or her code: https://api-orce-uni.jeedx.repl.co/getScores/?code=CODIGO&cycle=CICLO
- The format of the cycle should be: año+[1|2|3] (20191 or 20192 or 20193)
  - 1: first half of the year
  - 2: second half of the year
  - 3: summer cycle

# WARNING
This API was made quickly, so it can have multiple bugs.
