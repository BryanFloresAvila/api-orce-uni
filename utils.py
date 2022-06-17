import os
import tabula
import pandas as pd
import json
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ftfy
def getScores(cycle,codeUNI):
    url = os.environ['url']+'{0}/{1}'.format(cycle,codeUNI)
    dfs =  tabula.read_pdf(url, area = (195.326,84.827,759.354,436.787), columns = [198.675, 312.15, 374.654], pandas_options={'header': None}, pages = 'all')
    dfs = list(map(lambda df: df.drop([2,3],axis=1),dfs))
    dfScores = pd.DataFrame()

    for i in range(len(dfs)):
        if i in range(1,len(dfs)):
            dfs[i] = dfs[i].drop([0,1])
            dfScores = pd.concat([dfScores,dfs[i]],ignore_index=True)
        else:
            dfScores = pd.concat([dfScores,dfs[i]],ignore_index=True)

    dfScores = dfScores.drop([dfScores.shape[0]-1,dfScores.shape[0]-2])

    dfScores['border'] = dfScores.apply(lambda x: 1 if (len(str(x[0]))==5) else 0, axis = 1)
    dfScores['row'] =dfScores['border'].transform('cumsum')
    groupCourses = dfScores.groupby(dfScores.row,sort=False)
    courses = {}
    numCourses = dfScores.iloc[-1]['row']

    for i in range(1,numCourses+1):
        dtTemp = groupCourses.get_group(i).drop(['border','row'],axis=1).reset_index().drop(['index'],axis=1)
        course = dtTemp.iloc[0][0]
        dtTemp.columns = list(dtTemp.iloc[1])
        dtTemp =  dtTemp.drop([0,1]).reset_index().drop(['index'],axis=1)
        courses[course] = dtTemp.to_dict('records')
    courses =json.dumps(courses)
    return courses


def getInformation(codeUNI):
  url = 'https://www.orce.uni.edu.pe/detaalu.php?id={0}&op=detalu'.format(codeUNI)
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')
  trTags = soup.find_all('tr')
  information = {}
  for tr in trTags:
    tdTags = tr.find_all('td')
    if len(tdTags)==2:
      if len(tdTags[0].contents) == 1 and len(tdTags[1].contents) == 1:
        clave = ftfy.fix_text(str(tdTags[0].string))
        valor = ftfy.fix_text(str(tdTags[1].string))
        information[clave] = valor
  information =json.dumps(information)
  return information