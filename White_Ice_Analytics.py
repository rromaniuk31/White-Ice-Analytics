## Import Things
import pandas as pd
import numpy as np

## Get Data
def get_data():
    df1918 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1918Goalies.csv")
    df1919 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1919Goalies.csv")
    df1920 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1920Goalies.csv")
    df1921 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1921Goalies.csv")
    df1922 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1922Goalies.csv")
    df1923 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1923Goalies.csv")
    df1924 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1924Goalies.csv")
    df1925 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1925Goalies.csv")
    df1926 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1926Goalies.csv")
    df1927 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1927Goalies.csv")
    df1928 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1928Goalies.csv")
    df1929 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1929Goalies.csv")
    df1930 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1930Goalies.csv")
    df1931 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1931Goalies.csv")
    df1932 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1932Goalies.csv")
    df1933 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1933Goalies.csv")
    df1934 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1934Goalies.csv")
    df1935 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1935Goalies.csv")
    df1936 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1936Goalies.csv")
    df1937 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1937Goalies.csv")
    df1938 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1938Goalies.csv")
    df1939 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1939Goalies.csv")
    df1940 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1940Goalies.csv")
    df1941 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1941Goalies.csv")
    df1942 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1942Goalies.csv")
    df1943 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1943Goalies.csv")
    df1944 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1944Goalies.csv")
    df1945 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1945Goalies.csv")
    df1946 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1946Goalies.csv")
    df1947 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1947Goalies.csv")
    df1948 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1948Goalies.csv")
    df1949 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1949Goalies.csv")
    df1950 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1950Goalies.csv")
    df1951 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1951Goalies.csv")
    df1952 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1952Goalies.csv")
    df1953 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1953Goalies.csv")
    df1954 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1954Goalies.csv")
    df1955 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1955Goalies.csv")
    df1956 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1956Goalies.csv")
    df1957 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1957Goalies.csv")
    df1958 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1958Goalies.csv")
    df1959 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1959Goalies.csv")
    df1960 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1960Goalies.csv")
    df1961 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1961Goalies.csv")
    df1962 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1962Goalies.csv")
    df1963 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1963Goalies.csv")
    df1964 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1964Goalies.csv")
    df1965 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1965Goalies.csv")
    df1966 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1966Goalies.csv")
    df1967 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1967Goalies.csv")
    df1968 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1968Goalies.csv")
    df1969 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1969Goalies.csv")
    df1970 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1970Goalies.csv")
    df1971 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1971Goalies.csv")
    df1972 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1972Goalies.csv")
    df1973 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1973Goalies.csv")
    df1974 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1974Goalies.csv")
    df1975 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1975Goalies.csv")
    df1976 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1976Goalies.csv")
    df1977 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1977Goalies.csv")
    df1978 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1978Goalies.csv")
    df1979 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1979Goalies.csv")
    df1980 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1980Goalies.csv")
    df1981 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1981Goalies.csv")
    df1982 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1982Goalies.csv")
    df1983 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1983Goalies.csv")
    df1984 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1984Goalies.csv")
    df1985 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1985Goalies.csv")
    df1986 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1986Goalies.csv")
    df1987 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1987Goalies.csv")
    df1988 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1988Goalies.csv")
    df1989 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1989Goalies.csv")
    df1990 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1990Goalies.csv")
    df1991 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1991Goalies.csv")
    df1992 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1992Goalies.csv")
    df1993 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1993Goalies.csv")
    df1994 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1994Goalies.csv")
    df1995 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1995Goalies.csv")
    df1996 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1996Goalies.csv")
    df1997 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1997Goalies.csv")
    df1998 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1998Goalies.csv")
    df1999 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\1999Goalies.csv")
    df2000 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2000Goalies.csv")
    df2001 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2001Goalies.csv")
    df2002 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2002Goalies.csv")
    df2003 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2003Goalies.csv")
    df2004 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2004Goalies.csv")
    df2006 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2006Goalies.csv")
    df2007 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2007Goalies.csv")
    df2008 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2008Goalies.csv")
    df2009 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2009Goalies.csv")
    df2010 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2010Goalies.csv")
    df2011 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2011Goalies.csv")
    df2012 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2012Goalies.csv")
    df2013 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2013Goalies.csv")
    df2014 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2014Goalies.csv")
    df2015 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2015Goalies.csv")
    df2016 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2016Goalies.csv")
    df2017 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2017Goalies.csv")
    df2018 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2018Goalies.csv")
    df2019 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2019Goalies.csv")
    df2020 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2020Goalies.csv")
    df2021 = pd.read_csv("D:\\White Ice Analytics\\Historical Goalie Stats\\Regular Season\\2021Goalies.csv")

    return (df1918, df1919, df1920, df1921, df1922, df1923, df1924, df1925, df1926, df1927, df1928, df1929, df1930, df1931, df1932, df1933, df1934, df1935, df1936, df1937, df1938, df1939, df1940, df1941, df1942, df1943, df1944, df1945, df1946, df1947, df1948, df1949, df1950, df1951, df1952, df1953, df1954, df1955, df1956, df1957, df1958, df1959, df1960, df1961, df1962, df1963, df1964, df1965, df1966, df1967, df1968, df1969, df1970, df1971, df1972, df1973, df1974, df1975, df1976, df1977, df1978, df1979, df1980, df1981, df1982, df1983, df1984, df1985, df1986, df1987, df1988, df1989, df1990, df1991, df1992, df1993, df1994, df1995, df1996, df1997, df1998, df1999, df2000, df2001, df2002, df2003, df2004, df2006, df2007, df2008, df2009, df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021)

df1918, df1919, df1920, df1921, df1922, df1923, df1924, df1925, df1926, df1927, df1928, df1929, df1930, df1931, df1932, df1933, df1934, df1935, df1936, df1937, df1938, df1939, df1940, df1941, df1942, df1943, df1944, df1945, df1946, df1947, df1948, df1949, df1950, df1951, df1952, df1953, df1954, df1955, df1956, df1957, df1958, df1959, df1960, df1961, df1962, df1963, df1964, df1965, df1966, df1967, df1968, df1969, df1970, df1971, df1972, df1973, df1974, df1975, df1976, df1977, df1978, df1979, df1980, df1981, df1982, df1983, df1984, df1985, df1986, df1987, df1988, df1989, df1990, df1991, df1992, df1993, df1994, df1995, df1996, df1997, df1998, df1999, df2000, df2001, df2002, df2003, df2004, df2006, df2007, df2008, df2009, df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021 = get_data()
df_list = [df1918, df1919, df1920, df1921, df1922, df1923, df1924, df1925, df1926, df1927, df1928, df1929, df1930, df1931, df1932, df1933, df1934, df1935, df1936, df1937, df1938, df1939, df1940, df1941, df1942, df1943, df1944, df1945, df1946, df1947, df1948, df1949, df1950, df1951, df1952, df1953, df1954, df1955, df1956, df1957, df1958, df1959, df1960, df1961, df1962, df1963, df1964, df1965, df1966, df1967, df1968, df1969, df1970, df1971, df1972, df1973, df1974, df1975, df1976, df1977, df1978, df1979, df1980, df1981, df1982, df1983, df1984, df1985, df1986, df1987, df1988, df1989, df1990, df1991, df1992, df1993, df1994, df1995, df1996, df1997, df1998, df1999, df2000, df2001, df2002, df2003, df2004, df2006, df2007, df2008, df2009, df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021]
## Get 2021 Averages
## Create Actual GP Column (TOI/60)
for df in df_list:
    df[['Minutes','Seconds']] = df['TOI'].str.split(':', expand = True)
    df['Actual GP'] = ''
    for i in range(0, len(df)):
        if ',' in df['Minutes'][i]:
            df[['Min1', 'Min2']] = df['Minutes'].str.split(',', expand = True)
            df['Minutes'][i] = df['Min1'][i] + df['Min2'][i]
            df = df.drop(columns = ['Min1', 'Min2'])

    df['Minutes'] = pd.to_numeric(df['Minutes'])
    df['Seconds'] = pd.to_numeric(df['Seconds'])
    
    for i in range(0, len(df)):
        df['TOI'][i] = df['Minutes'][i] + (df['Seconds'][i]/60)
        df['Actual GP'][i] = df['TOI'][i]/60
        
    ## Remove commas from SA & Svs
    for i in range(0, len(df)):
        if ',' in df['SA'][i]:
            df[['SA1', 'SA2']] = df['SA'].str.split(',', expand = True)
            df['SA'][i] = df['SA1'][i] + df['SA2'][i]
            df = df.drop(columns = ['SA1', 'SA2'])
            
        if ',' in df['Svs'][i]:
            df[['Svs1', 'Svs2']] = df['Svs'].str.split(',', expand = True)
            df['Svs'][i] = df['Svs1'][i] + df['Svs2'][i]
            df = df.drop(columns = ['Svs1', 'Svs2'])
    ## Change neceesaary columns to numeric
    for i in range(0, len(df)):
        if df['T'][i] == '--':
            df['T'][i] = 0

num_cols = ['GP', 'GS', 'W', 'L', 'T', 'OT', 'SA', 'Svs', 'GA', 'Sv%', 'GAA', 'TOI', 'SO', 'G', 'A', 'P', 'PIM', 'Actual GP']