
#%%
import pymongo
import pandas as pd
client=pymongo.MongoClient()
db=client['sbp']
projects=db['projects']
data7=pd.read_csv('title.akas.tsv',sep='\t')
data7.rename(columns={'titleId': 'tconst'}, inplace=True)
#%%
for data4 in pd.read_csv('title.ratings.tsv',sep='\t', chunksize=10000):
    data7=pd.read_csv('title.akas.tsv',sep='\t')
    data7.rename(columns={'titleId': 'tconst'}, inplace=True)
    data8=pd.merge(data4,data7,on='tconst',how='left')
    del data7
    data=pd.read_csv('title.basics.tsv',sep='\t')
    data4=pd.merge(data4, data,on='tconst')
    del data
    data4.to_csv('filmovisaocenom.csv')
        
    data3=pd.read_csv('title.principals.tsv',sep='\t')
    data4=pd.merge(data4,data3,on='tconst')
    del data3
    data2=pd.read_csv('name.basics.tsv',sep='\t')
    data2=pd.merge(data4,data2,on='nconst',how='left')
    del data4
    
    #%%
    
    
    actorsList = []
    all_actors_jsons=[]
    regioni=[]
    for data in pd.read_csv("filmovisaocenom.csv", chunksize=1):
            for index,row in data.iterrows():
                
                datax=data8.loc[data8['tconst'] == row['tconst']]
                for index2,row2 in datax.iterrows():
            
                                regioni.append({
                                    'region':row2['region']
                                    })
                               
                
                datay=data2.loc[data2['tconst'] == row['tconst']]
                for index2,row2 in datay.iterrows():
                    
                                                            
                                                            actorsList.append({
                                                                'primaryName':row2['primaryName'],
                                                                'live':{
                                                                'birthYear':row2['birthYear'],
                                                                'deathYear':row2['deathYear']
                                                                },
                                                                'category':row2['category'],
                                                                'job':row2['job'],
                                                                'characters':row2['characters'],
                                                                'primaryProfession':str(row2['primaryProfession']).split(',')
                                                        })
            all_actors_jsons.append({
                                                                    'primaryTitle':row['primaryTitle'],
                                                                    'titleType':row['titleType'],
                                                                    'originalTitle':row['originalTitle'],
                                                                    'isAdult':row['isAdult'],
                                                                    'genres':str(row['genres']).split(","),
                                                                    'runtime':{
                                                                        'startYear':row['startYear'],
                                                                        'endYear':row['endYear'],
                                                                        'runtimeMinutes':row['runtimeMinutes']
                                                                        
                                                                    },
                                                                    'ratings':{
                                                                        'averageRating':row['averageRating'],
                                                                        'numVotes':row['numVotes']
                                                                        },
                                                                    'actor':actorsList,
                                                                    'regioni':regioni
                                                                    
                                                                    
                                                                
                                                        })
           
            projects.insert_many(all_actors_jsons)
            actorsList=[]
            all_actors_jsons=[]
            regioni=[]                                               