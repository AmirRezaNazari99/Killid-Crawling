
def query_locations(data):
    loaction_counts = data["Location"].value_counts()
    print("Count of Every Location:")
    print(loaction_counts)
    print("#############################")
    print("\n")
    df = data[data["Price"] != 'قیمت']
    df = df.astype({"Price": float})
    print("Average Price per each location:")
    print(df.groupby('Location')['Price'].mean())
