import pandas as pd
#from bokeh.plotting import figure, output_file, show,output_notebook, output_notebook()

links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

gdp_data = pd.read_csv(links['GDP'])

print(gdp_data)