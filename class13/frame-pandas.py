import pandas as pd

list = [["Metin",60], ["Ali",35], ["Günaydın",55], ["Servet",33]]
dict = {"Name": ["Metin","Ali","Günaydın","Servet"], "Age": [60,35,55,33]}
dict_list = [
                {"Name":"Metin","Age":60},
                {"Name":"Ali","Age":35},
                {"Name":"Günaydın","Age":55},
                {"Name":"Servet","Age":33}
            ]

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(list, index = [1,2,3,4], columns = ['Name','Age'], dtype = float)
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ["28","34","35","6"])
# df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list,index = ["28","34","35","6"])

print(df)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(bananas = b1 , kiwies = b2)

# df = pd.DataFrame(data)

# print(df)